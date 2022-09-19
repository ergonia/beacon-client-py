from beacon_client.api import BeaconChainAPI


class TestConfigEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_get_fork_schedule(self):
        pass

    def test_get_node_specification(self):
        pass

    def test_get_deposit_contract(self):
        pass
