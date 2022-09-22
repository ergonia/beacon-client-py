from sseclient import SSEClient
from .utils.parsing import parse_json
from .utils.types import StreamedHead, StreamedBlock, Attestation, StreamedCheckpoint
import json


class EventEndpoints:
    def stream_events(
        self,
        head: bool = False,
        block: bool = False,
        attestation: bool = False,
        voluntary_exit: bool = False,
        finalized_checkpoint: bool = False,
        chain_reorg: bool = False,
        contribution_and_proof: bool = False,
    ):
        """
        Provides endpoint to subscribe to beacon node Server-Sent-Events stream
        Returns an Event object with the event name (event.name: str) and the contents (event.data: str)
        Args:
            head: If true return events of type head
            block: If true return events of type block
            attestation: If true return events of type attestation
            voluntary_exit: If true return events of type voluntary_exit
            finalized_checkpoint: If true return events of type finalized_checkpoint
            chain_reorg: If true return events of type chain_reorg
            contribution_and_proof: If true return events of type contribution_and_proof
        """
        events = []
        if head:
            events.append("head")
        if block:
            events.append("block")
        if attestation:
            events.append("attestation")
        if voluntary_exit:
            events.append("voluntary_exit")
        if finalized_checkpoint:
            events.append("finalized_checkpoint")
        if chain_reorg:
            events.append("chain_reorg")
        if contribution_and_proof:
            events.append("contribution_and_proof")

        assert len(events) > 0, "Must select at least one event"
        response = self._query_url(
            path="/eth/v1/events",
            stream=True,
            headers={"Accept": "text/event-stream"},
            params={"topics": events},
        )
        client = SSEClient(response)
        return client.events()

    @staticmethod
    def parse_head(data):
        data = parse_json(json.loads(data), StreamedHead)
        return data

    @staticmethod
    def parse_block(data):
        data = parse_json(json.loads(data), StreamedBlock)
        return data

    @staticmethod
    def parse_attestation(data):
        data = parse_json(json.loads(data), Attestation)
        return data

    @staticmethod
    def parse_checkpoint(data):
        data = parse_json(json.loads(data), StreamedCheckpoint)
        return data
