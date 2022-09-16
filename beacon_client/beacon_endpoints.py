from typing import Union


class BeaconEndpoints:
    StateId = Union[str, int]

    @staticmethod
    def _check_state_id(state_id: StateId) -> None:
        if isinstance(state_id, str) and not state_id.startswith("0x"):
            assert state_id in [
                "head",
                "genesis",
                "finalized",
                "justified",
            ], "state_id must be in [head, genesis, finalized, justified] or block number (int) or start with 0x"

    def get_genesis(self) -> dict:
        """
        Retrieve details of the chain's genesis which can be used to identify chain.
        """
        return self._query_url("/eth/v1/beacon/genesis")

    def get_state_root(self, state_id: StateId) -> dict:
        """
        Calculates HashTreeRoot for state with given 'state_id'. If state_id is root, same value will be returned.
        """
        self._check_state_id(state_id)
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/root")

    def get_fork_from_state(self, state_id: StateId) -> dict:
        """
        Returns Fork object for state with given 'state_id'.
        """
        self._check_state_id(state_id)
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/fork")

    def get_finality_checkpoints_from_state(self, state_id: StateId) -> dict:
        """
        Returns finality checkpoints for state with given 'state_id'.
        In case finality is not yet achieved, checkpoint should return epoch 0 and ZERO_HASH as root.
        """
        self._check_state_id(state_id)
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/finality_checkpoints")

    def get_validators_from_state(
        self,
        state_id: StateId,
        validator_list: Union[list, None] = None,
        pending_initialized: bool = False,
        pending_queued: bool = False,
        active_ongoing: bool = False,
        active_exiting: bool = False,
        active_slashed: bool = False,
        exited_unslashed: bool = False,
        exited_slashed: bool = False,
        withdrawal_possible: bool = False,
        withdrawal_done: bool = False,
        active: bool = False,
        pending: bool = False,
        exited: bool = False,
        withdrawal: bool = False,
    ) -> dict:
        """
        Returns filterable list of validators with their balance, status and index.
        Information will be returned for all indices or public key that match known validators.
        If an index or public key does not match any known validator,
        no information will be returned but this will not cause an error.
        There are no guarantees for the returned data in terms of ordering;
        both the index and public key are returned for each validator,
        and can be used to confirm for which inputs a response has been returned.
        """
        self._check_state_id(state_id)
        status = []
        if pending_initialized:
            status.append("pending_initialized")
        if pending_queued:
            status.append("pending_queued")
        if active_ongoing:
            status.append("active_ongoing")
        if active_exiting:
            status.append("active_exiting")
        if active_slashed:
            status.append("active_slashed")
        if exited_unslashed:
            status.append("exited_unslashed")
        if exited_slashed:
            status.append("exited_slashed")
        if withdrawal_possible:
            status.append("withdrawal_possible")
        if withdrawal_done:
            status.append("withdrawal_done")
        if active:
            status.append("active")
        if pending:
            status.append("pending")
        if exited:
            status.append("exited")
        if withdrawal:
            status.append("withdrawal")
        assert len(status) > 0, "Select at least one validator condition"
        params = {"status": status, "id": validator_list}
        return self._query_url(
            f"/eth/v1/beacon/states/{state_id}/validators", params=params
        )

    def get_validators_from_state_by_id(self, state_id: StateId, validator_id) -> dict:
        """
        Returns validator specified by state and id or public key along with status and balance.
        """
        self._check_state_id(state_id)
        return self._query_url(
            f"/eth/v1/beacon/states/{state_id}/validators/{validator_id}"
        )

    def get_validators_balances_from_state(
        self, state_id: StateId, validator_list: Union[list, None] = None
    ) -> dict:
        """
        Returns filterable list of validators balances.
        Balances will be returned for all indices or public key that match known validators.
        If an index or public key does not match any known validator,
        no balance will be returned but this will not cause an error.
        There are no guarantees for the returned data in terms of ordering;
        the index and is returned for each balance,
        and can be used to confirm for which inputs a response has been returned.
        """
        params = {"id": validator_list}
        return self._query_url(
            f"/eth/v1/beacon/states/{state_id}/validator_balances", params=params
        )

    def get_committees_from_state(
        self,
        state_id: StateId,
        epoch: Union[int, None] = None,
        index: Union[int, None] = None,
        slot: Union[int, None] = None,
    ) -> dict:
        """
        Retrieves the committees for the given state.
        """
        params = {"epoch": epoch, "index": index, "slot": slot}
        return self._query_url(
            f"/eth/v1/beacon/states/{state_id}/committees", params=params
        )

    def get_sync_committees_from_state(
        self, state_id, epoch: Union[int, None] = None
    ) -> dict:
        """
        Retrieves the sync committees for the given state.
        """
        params = {
            "epoch": epoch,
        }
        return self._query_url(
            f"/eth/v1/beacon/states/{state_id}/sync_committees", params=params
        )

    def get_headers(
        self, slot: Union[int, None] = None, parent_root: Union[str, None] = None
    ) -> dict:
        """
        Retrieves block headers matching given query. By default it will fetch current head slot blocks.
        """
        params = {"slot": slot, "parent_root": parent_root}
        return self._query_url("/eth/v1/beacon/headers", params=params)

    def get_headers_from_block_id(self, block_id) -> dict:
        """
        Retrieves block headers matching given query. By default it will fetch current head slot blocks.
        """
        return self._query_url(f"/eth/v1/beacon/headers/{block_id}")

    def get_block_from_block_id(
        self, block_id, response_type: str = "json"
    ) -> Union[dict, str]:
        """
        Retrieves block details for given block id.
        Depending on Accept header it can be returned either as json or as bytes serialized by SSZ
        response_type in [json, ssz]
        """
        assert response_type in ["json", "ssz"], "response_type must be in [json, ssz]"
        if response_type == "json":
            headers = {"Accept": "application/json"}
        if response_type == "ssz":
            headers = {"Accept": "application/octet-stream"}
        return self._query_url(f"/eth/v2/beacon/blocks/{block_id}", headers=headers)

    def get_block_root_from_block_id(self, block_id) -> dict:
        """
        Retrieves hashTreeRoot of BeaconBlock/BeaconBlockHeader
        """
        return self._query_url(f"/eth/v1/beacon/blocks/{block_id}/root")

    def get_attestations_from_block_id(self, block_id) -> dict:
        """
        Retrieves attestation included in requested block.
        """
        return self._query_url(f"/eth/v1/beacon/blocks/{block_id}/attestations")

    def get_pool_attestations(
        self, slot: Union[int, None] = None, committee_index: Union[int, None] = None
    ) -> dict:
        """
        Retrieves attestations known by the node but not necessarily incorporated into any block
        """
        params = {"slot": slot, "committee_index": committee_index}
        return self._query_url("/eth/v1/beacon/pool/attestations", params=params)

    def get_pool_attester_slashings(self) -> dict:
        """
        Retrieves attester slashings known by the node but not necessarily incorporated into any block
        """
        return self._query_url("/eth/v1/beacon/pool/attester_slashings")

    def get_pool_proposer_slashings(self) -> dict:
        """
        Retrieves proposer slashings known by the node but not necessarily incorporated into any block
        """
        return self._query_url("/eth/v1/beacon/pool/proposer_slashings")

    def get_pool_voluntary_exits(self) -> dict:
        """
        Retrieves voluntary exits known by the node but not necessarily incorporated into any block
        """
        return self._query_url("/eth/v1/beacon/pool/voluntary_exits")
