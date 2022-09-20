from beacon_client.api import BeaconChainAPI


class TestNodeEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_get_node_identity(self):
        # node specific
        pass

    def test_get_node_peers(self):
        # node specific
        pass

    def test_get_peer_by_id(self):
        # node specific
        pass

    def test_get_peer_count(self):
        # node specific
        pass

    def test_get_node_version(self):
        # node specific
        pass

    def test_get_syncing_status(self):
        # node specific
        pass

    def test_get_node_health(self):
        # node specific
        pass
