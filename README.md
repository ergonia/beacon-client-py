# beacon-client-py
A Python client for interacting with the Ethereum Beacon Chain API

Reference: https://ethereum.github.io/beacon-APIs/

## Simple Example

```
from beacon_client.api import BeaconChainAPI


api = BeaconChainAPI("http://localhost:5052")
api.get_block_from_block_id(block_id="head", response_type="json")
```

## Streaming Example
```
for event in api.stream_events(head=True, block=True):
    print(event.event)
    print(json.loads(event.data))
```
