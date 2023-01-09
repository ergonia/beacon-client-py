from .types import (
    Gwei,
    ValidatorIndex,
    CommitteeIndex,
    Slot,
    Epoch,
    Validator,
    SignedBeaconBlockHeader,
    BeaconBlockHeader,
    BeaconBlock,
    BeaconBlockBody,
    Eth1Data,
    ValidatorStatus,
    PeerState,
    ConnectionOrientation,
    ChainId,
    Wei,
)
from dacite import from_dict, Config
from bitstring import BitArray
from multiaddr import Multiaddr

SimpleTypeHooks = {
    Gwei: lambda x: Gwei(int(x)),
    Wei: lambda x: Wei(int(x)),
    ValidatorIndex: lambda x: ValidatorIndex(int(x)),
    CommitteeIndex: lambda x: CommitteeIndex(int(x)),
    Slot: lambda x: Slot(int(x)),
    Epoch: lambda x: Epoch(int(x)),
    ChainId: lambda x: ChainId(int(x)),
    int: int,
    BitArray: BitArray,
    Multiaddr: Multiaddr,
    ValidatorStatus: ValidatorStatus,
    PeerState: PeerState,
    ConnectionOrientation: ConnectionOrientation,
}


def _nested_hook(beacon_class, sub_classes: dict = {}, SimpleTypeHooks=SimpleTypeHooks):
    return lambda x: from_dict(
        data_class=beacon_class,
        data=x,
        config=Config(type_hooks={**SimpleTypeHooks, **sub_classes}),
    )


NestedTypeHooks = {
    Validator: _nested_hook(Validator),
    SignedBeaconBlockHeader: _nested_hook(
        SignedBeaconBlockHeader, {BeaconBlockHeader: _nested_hook(BeaconBlockHeader)}
    ),
    BeaconBlock: _nested_hook(
        BeaconBlock,
        {
            BeaconBlockBody: _nested_hook(
                BeaconBlockBody, {Eth1Data: _nested_hook(Eth1Data)}
            )
        },
    ),
}


TypeHooks = {**SimpleTypeHooks, **NestedTypeHooks}


def parse_json(data, data_class, TypeHooks=TypeHooks):
    if isinstance(data, list):
        result = [
            from_dict(
                data_class=data_class,
                data=d,
                config=Config(type_hooks=TypeHooks),
            )
            for d in data
        ]
        return result
    else:
        return from_dict(
            data_class=data_class,
            data=data,
            config=Config(type_hooks=TypeHooks),
        )
