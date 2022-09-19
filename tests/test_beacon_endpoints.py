from beacon_client.api import BeaconChainAPI


class TestBeaconEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_genesis(self):
        pass

    def test_get_state_root(self):
        pass

    def test_get_fork_from_state(self):
        pass

    def test_get_finality_checkpoints_from_state(self):
        pass

    def test_get_validators_from_state(self):
        pass

    def test_get_validators_from_state_by_id(self):
        pass

    def test_get_validator_balances_from_state(self):
        pass

    def test_get_committees_from_state(self):
        pass

    def test_get_sync_committees_from_state(self):
        pass

    def test_get_headers(self):
        pass

    def test_get_headers_from_block_id(self):
        pass

    def test_get_block_from_block_id(self):
        actual = self.client.get_block_from_block_id(
            block_id=4733495, response_type="json"
        )
        assert (
            actual["data"]["message"]["state_root"]
            == "0xba3b2821811aa990fcf4148e0528819a813e2908c93545076355a0132fb5e87a"
        )

    def test_get_block_root_from_block_id(self):
        pass

    def test_get_attestations_from_block_id(self):
        pass

    def test_get_pool_attestations(self):
        pass

    def test_get_pool_attester_slashings(self):
        pass

    def test_pool_proposer_slashings(self):
        pass

    def test_get_pool_voluntary_exits(self):
        pass
