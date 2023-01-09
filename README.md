# beacon-client-py
A Python client for interacting with the Ethereum Beacon Chain API

[Beacon Chain API Reference](https://ethereum.github.io/beacon-APIs)

[Ethereum Consensus Specification](https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md)

[Ethereum Consensus Specification Annotated](https://eth2book.info/altair/part3)

This implementation also leans on types implemented [here](https://github.com/ralexstokes/beacon-api-client)

## Installation
```bash
pip install beacon-client-py
```

## Simple Example

```python
from beacon_client.api import BeaconChainAPI

client = BeaconChainAPI("http://localhost:5052")
client.get_headers_from_block_id(block_id="head")
```

## Streaming Example
```python
for event in client.stream_events(head=True, block=True, attestation=True):
    match event.event:
        case "head":
            print(client.parse_head(event.data))
        case "block":
            print(client.parse_block(event.data))
        case "attestation":
            print(client.parse_attestation(event.data))
        case other:
            pass
```

## Development

Run the docs locally 

```bash
poetry run mkdocs serve
```

Formatter
```bash
poetry run black .
```

Tests
```bash
poetry run pytest -vv
```

linter
```bash
poetry run flake8
```

_note_: requires poetry version 1.2.x or higher
