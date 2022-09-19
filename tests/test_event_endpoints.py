from beacon_client.api import BeaconChainAPI


class TestEventEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_stream_events(self):
        pass
