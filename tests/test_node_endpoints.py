from beacon_client.api import BeaconChainAPI


class TestNodeEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_get_node_identity(self):
        pass

    def test_get_node_peers(self):
        pass

    def test_get_peer_by_id(self):
        pass

    def test_get_peer_count(self):
        pass

    def test_get_node_version(self):
        pass

    def test_get_syncing_status(self):
        pass

    def test_get_node_health(self):
        pass
