from typing import Union, List
from .utils.parsing import parse_json
from .utils.types import (
    StateId,
    ValidatorId,
    ValidatorIndex,
    CommitteeIndex,
    BlockId,
    Epoch,
    Slot,
    Root,
    GenesisDetails,
    FinalityCheckpoints,
    ValidatorSummary,
    BalanceSummary,
    CommitteeSummary,
    SyncCommitteeSummary,
    BeaconHeaderSummary,
    SignedBeaconBlock,
    Attestation,
    Fork,
)


class BeaconEndpoints:
    def get_genesis(self) -> GenesisDetails:
        """
        Retrieve details of the chain's genesis which can be used to identify chain.
        """
        value = self._query_url("/eth/v1/beacon/genesis")
        data = parse_json(value["data"], GenesisDetails)
        return data

    def get_state_root(self, state_id: StateId) -> Root:
        """
        Calculates HashTreeRoot for state with given 'state_id'. If state_id is root, same value will be returned.

        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
        """
        value = self._query_url(f"/eth/v1/beacon/states/{state_id}/root")
        data = Root(value["data"]["root"])
        return data

    def get_fork_from_state(self, state_id: StateId) -> Fork:
        """
        Returns Fork object for state with given 'state_id'.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
        """
        value = self._query_url(f"/eth/v1/beacon/states/{state_id}/fork")
        data = parse_json(value["data"], Fork)
        return data

    def get_finality_checkpoints_from_state(
        self, state_id: StateId
    ) -> FinalityCheckpoints:
        """
        Returns finality checkpoints for state with given 'state_id'.
        In case finality is not yet achieved, checkpoint should return epoch 0 and ZERO_HASH as root.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
        """
        value = self._query_url(
            f"/eth/v1/beacon/states/{state_id}/finality_checkpoints"
        )
        data = parse_json(value["data"], FinalityCheckpoints)
        return data

    def get_validators_from_state(
        self,
        state_id: StateId,
        validator_list: Union[List[ValidatorId], None] = None,
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
    ) -> List[ValidatorSummary]:
        """
        Returns filterable list of validators with their balance, status and index.
        Information will be returned for all indices or public key that match known validators.
        If an index or public key does not match any known validator,
        no information will be returned but this will not cause an error.
        There are no guarantees for the returned data in terms of ordering;
        both the index and public key are returned for each validator,
        and can be used to confirm for which inputs a response has been returned.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
            validator_list: List of validators identified by public key or validator index
            pending_initialized: If true return validators with this status
            pending_queued: If true return validators with this status
            active_ongoing: If true return validators with this status
            active_exiting: If true return validators with this status
            active_slashed: If true return validators with this status
            exited_unslashed: If true return validators with this status
            exited_slashed: If true return validators with this status
            withdrawal_possible: If true return validators with this status
            withdrawal_done: If true return validators with this status
            active: If true return validators with this status
            pending: If true return validators with this status
            exited: If true return validators with this status
            withdrawal: If true return validators with this status
        """
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
        value = self._query_url(
            f"/eth/v1/beacon/states/{state_id}/validators", params=params
        )
        data = parse_json(value["data"], ValidatorSummary)
        return data

    def get_validators_from_state_by_id(
        self, state_id: StateId, validator_id: ValidatorId
    ) -> ValidatorSummary:
        """
        Returns validator specified by state and id or public key along with status and balance.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
            validator_id: Validator identified by public key or validator index
        """
        value = self._query_url(
            f"/eth/v1/beacon/states/{state_id}/validators/{validator_id}"
        )
        data = parse_json(value["data"], ValidatorSummary)
        return data

    def get_validators_balances_from_state(
        self, state_id: StateId, validator_list: Union[List[ValidatorId], None] = None
    ) -> List[BalanceSummary]:
        """
        Returns filterable list of validators balances.
        Balances will be returned for all indices or public key that match known validators.
        If an index or public key does not match any known validator,
        no balance will be returned but this will not cause an error.
        There are no guarantees for the returned data in terms of ordering;
        the index and is returned for each balance,
        and can be used to confirm for which inputs a response has been returned.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
            validator_list: List of validators identified by public key or validator index
        """
        params = {"id": validator_list}
        value = self._query_url(
            f"/eth/v1/beacon/states/{state_id}/validator_balances", params=params
        )
        data = parse_json(value["data"], BalanceSummary)
        return data

    def get_committees_from_state(
        self,
        state_id: StateId,
        epoch: Union[Epoch, None] = None,
        index: Union[ValidatorIndex, None] = None,
        slot: Union[Slot, None] = None,
    ) -> List[CommitteeSummary]:
        """
        Retrieves the committees for the given state.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
            epoch: Fetch committees for the given epoch. If not present then the committees for the epoch of the state will be obtained
            index: Restrict returned values to those matching the supplied committee index
            slot: Restrict returned values to those matching the supplied slot
        """
        params = {"epoch": epoch, "index": index, "slot": slot}
        value = self._query_url(
            f"/eth/v1/beacon/states/{state_id}/committees", params=params
        )
        data = parse_json(value["data"], CommitteeSummary)
        return data

    def get_sync_committees_from_state(
        self, state_id: StateId, epoch: Union[Epoch, None] = None
    ) -> SyncCommitteeSummary:
        """
        Retrieves the sync committees for the given state.
        Args:
            state_id: Element of [head, genesis, finalized, justified] or block number (int) or string starting with 0x
            epoch: Fetch committees for the given epoch. If not present then the committees for the epoch of the state will be obtained
        """
        params = {
            "epoch": epoch,
        }
        value = self._query_url(
            f"/eth/v1/beacon/states/{state_id}/sync_committees", params=params
        )
        data = parse_json(value["data"], SyncCommitteeSummary)
        return data

    def get_headers(
        self, slot: Union[Slot, None] = None, parent_root: Union[Root, None] = None
    ) -> BeaconHeaderSummary:
        """
        Retrieves block headers matching given query. By default it will fetch current head slot blocks.
        Args:
            slot: Restrict returned values to those matching the supplied slot
            parent_root: Restrict returned values to those matching the supplied parent_root
        """
        params = {"slot": slot, "parent_root": parent_root}
        value = self._query_url("/eth/v1/beacon/headers", params=params)
        data = parse_json(value["data"], BeaconHeaderSummary)
        return data

    def get_headers_from_block_id(self, block_id: BlockId) -> BeaconHeaderSummary:
        """
        Retrieves block headers matching given query. By default it will fetch current head slot blocks.
        Args:
            block_id: Return block header matching given block id
        """
        value = self._query_url(f"/eth/v1/beacon/headers/{block_id}")
        data = parse_json(value["data"], BeaconHeaderSummary)
        return data

    def get_block_from_block_id(
        self, block_id: BlockId, response_type: str = "json"
    ) -> Union[SignedBeaconBlock, str]:
        """
        Retrieves block details for given block id.
        Depending on Accept header it can be returned either as json or as bytes serialized by SSZ
        response_type in [json, ssz]
        Args:
            block_id: Return block matching given block id
            response_type: Element of [json, szz] that determines the return type
        """
        match response_type:
            case "json":
                headers = {"Accept": "application/json"}
                value = self._query_url(
                    f"/eth/v2/beacon/blocks/{block_id}", headers=headers
                )
                data = parse_json(value["data"], SignedBeaconBlock)
                return data
            case "ssz":
                headers = {"Accept": "application/octet-stream"}
                return self._query_url(
                    f"/eth/v2/beacon/blocks/{block_id}", headers=headers
                )
            case _:
                assert Exception("response_type must be in [json, ssz]")

    def get_block_root_from_block_id(self, block_id: BlockId) -> Root:
        """
        Retrieves hashTreeRoot of BeaconBlock/BeaconBlockHeader
        Args:
            block_id: Return block root matching given block id
        """
        value = self._query_url(f"/eth/v1/beacon/blocks/{block_id}/root")
        return Root(value["data"]["root"])

    def get_attestations_from_block_id(self, block_id: BlockId) -> List[Attestation]:
        """
        Retrieves attestation included in requested block.
        Args:
            block_id: Return attestations matching given block id
        """
        value = self._query_url(f"/eth/v1/beacon/blocks/{block_id}/attestations")
        data = parse_json(value["data"], Attestation)
        return data

    def get_pool_attestations(
        self,
        slot: Union[Slot, None] = None,
        committee_index: Union[CommitteeIndex, None] = None,
    ) -> List[Attestation]:
        """
        Retrieves attestations known by the node but not necessarily incorporated into any block
        Args:
            slot: Restrict returned values to those matching the supplied slot
            committee_index: Restrict returned values to those matching the supplied committee index
        """
        params = {"slot": slot, "committee_index": committee_index}
        value = self._query_url("/eth/v1/beacon/pool/attestations", params=params)
        data = parse_json(value["data"], Attestation)
        return data

    def get_pool_attester_slashings(self) -> list:
        """
        Retrieves attester slashings known by the node but not necessarily incorporated into any block
        """
        value = self._query_url("/eth/v1/beacon/pool/attester_slashings")
        # unparsed because it is very hard to test since slashing is rare
        return value["data"]

    def get_pool_proposer_slashings(self) -> list:
        """
        Retrieves proposer slashings known by the node but not necessarily incorporated into any block
        """
        value = self._query_url("/eth/v1/beacon/pool/proposer_slashings")
        # unparsed because it is very hard to test since slashing is rare
        return value["data"]

    def get_pool_voluntary_exits(self) -> dict:
        """
        Retrieves voluntary exits known by the node but not necessarily incorporated into any block
        """
        value = self._query_url("/eth/v1/beacon/pool/voluntary_exits")
        # unparsed because it is very hard to test since slashing is rare
        return value["data"]
