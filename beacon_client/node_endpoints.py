from .utils.types import (
    PeerId,
    NetworkIdentity,
    PeerDescription,
    PeerSummary,
    SyncStatus,
)
from typing import List
from .utils.parsing import parse_json


class NodeEndpoints:
    def get_node_identity(self) -> NetworkIdentity:
        """
        Retrieves data about the node's network presence
        """
        value = self._query_url("/eth/v1/node/identity")
        data = parse_json(value["data"], NetworkIdentity)
        return data

    def get_node_peers(
        self,
        disconnected: bool = False,
        disconnecting: bool = False,
        connected: bool = False,
        connecting: bool = False,
        inbound: bool = False,
        outbound: bool = False,
    ) -> List[PeerDescription]:
        """
        Retrieves data about the node's network peers.
        By default this returns all peers.
        Multiple query params are combined using AND conditions
        Args:
            disconnected: If true return nodes with status disconnected
            disconnecting: If true return nodes with status disconnecting
            connected: If true return nodes with status connected
            connecting: If true return nodes with status connecting
            inbound: If true return nodes with direction inbound
            outbound: If true return nodes with direction outbound
        """
        state = []
        direction = []
        if disconnected:
            state.append("disconnected")
        if disconnecting:
            state.append("disconnecting")
        if connected:
            state.append("connected")
        if connecting:
            state.append("connecting")
        if inbound:
            direction.append("inbound")
        if outbound:
            direction.append("outbound")
        assert (
            len(state) > 0
        ), "Must request at least one state in [disconnected, disconnecting, connected, connecting]"
        assert (
            len(direction) > 0
        ), "Must request at least one direction in [inbound, outbound]"
        params = {"state": state, "direction": direction}
        value = self._query_url("/eth/v1/node/peers", params=params)
        data = parse_json(value["data"], PeerDescription)
        return data

    def get_peer_by_id(self, peer_id: PeerId) -> PeerDescription:
        """
        Retrieves data about the given peer
        Args:
            peer_id: Return peer for given peer id
        """
        value = self._query_url(f"/eth/v1/node/peers/{peer_id}")
        data = parse_json(value["data"], PeerDescription)
        return data

    def get_peer_count(self) -> PeerSummary:
        """
        Retrieves number of known peers.
        """
        value = self._query_url("/eth/v1/node/peer_count")
        data = parse_json(value["data"], PeerSummary)
        return data

    def get_node_version(self) -> str:
        """
        Requests that the beacon node identify information about its implementation in a format similar to a HTTP User-Agent field.
        """
        return self._query_url("/eth/v1/node/version")["data"]["version"]

    def get_syncing_status(self) -> SyncStatus:
        """
        Requests the beacon node to describe if it's currently syncing or not, and if it is, what block it is up to.
        """
        value = self._query_url("/eth/v1/node/syncing")
        data = parse_json(value["data"], SyncStatus)
        return data
