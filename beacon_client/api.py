import requests
import urllib.parse
from typing import Union
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
    ValidatorEndpoints,
):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _query_url(
        self,
        path: str,
        stream: bool = False,
        headers: dict = {"Accept": "application/json"},
        params: Union[dict, None] = None,
    ):
        url = urllib.parse.urljoin(self.base_url, path)
        response = requests.get(url, stream=stream, headers=headers, params=params)
        assert (
            response.status_code == 200
        ), f"Status Code: {response.status_code} | {response.text}"
        if headers["Accept"] == "application/json":
            return response.json()
        elif headers["Accept"] == "application/octet-stream":
            return response.text
        else:
            return response


if __name__ == "__main__":
    from devtools import debug
    import json

    api = BeaconChainAPI("http://localhost:5052")
    debug(
        api.get_block_from_block_id(block_id="head", response_type="json")["data"][
            "message"
        ]["slot"]
    )
    # for event in api.stream_events(attestation=True):
    #     debug(
    #         event.event,
    #         json.loads(event.data),
    #     )
