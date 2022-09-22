import requests
import urllib.parse
from typing import Union
from .beacon_endpoints import BeaconEndpoints
from .config_endpoints import ConfigEndpoints
from .debug_endpoints import DebugEndpoints
from .event_endpoints import EventEndpoints
from .node_endpoints import NodeEndpoints
from .validator_endpoints import ValidatorEndpoints


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
