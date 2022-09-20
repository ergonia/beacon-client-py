from beacon_client.api import BeaconChainAPI
import json


class TestEventEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_stream_events_event_type(self):
        for event in self.client.stream_events(attestation=True):
            break
        assert event.event == "attestation"

    def test_stream_events_event_data(self):
        for event in self.client.stream_events(attestation=True):
            break
        assert "aggregation_bits" in json.loads(event.data)
