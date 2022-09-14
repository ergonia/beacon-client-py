import requests
import urllib.parse
from beacon_client.beacon_endpoints import BeaconEndpoints
from beacon_client.config_endpoints import ConfigEndpoints
from beacon_client.debug_endpoints import DebugEndpoints
from beacon_client.event_endpoints import EventEndpoints
from beacon_client.node_endpoints import NodeEndpoints
from beacon_client.validator_endpoints import ValidatorEndpoints


class BeaconChainAPI(
    BeaconEndpoints,
    ConfigEndpoints,
    DebugEndpoints,
    EventEndpoints,
    NodeEndpoints,
    ValidatorEndpoints
):
    def __init__(self, base_url: str):
        self.base_url = base_url
            
    #### BEACON ENDPOINTS ####
    def _query_url(self, path):
        url = urllib.parse.urljoin(self.base_url, path)
        response = requests.get(url)
        assert response.status_code == 200, f"Status Code: {response.status_code} | {response.text}"
        return response.json()


if __name__ == "__main__":
    api = BeaconChainAPI("http://localhost:5052")
    print(api.get_deposit_contract())
    