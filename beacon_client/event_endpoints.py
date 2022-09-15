from sseclient import SSEClient


class EventEndpoints:
    def stream_events(
        self, 
        head=False,
        block=False,
        attestation=False,
        voluntary_exit=False,
        finalized_checkpoint=False,
        chain_reorg=False,
        contribution_and_proof=False
    ):
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
        response = self._query_url("/eth/v1/events", stream=True, headers={"Accept": "text/event-stream"})
        client = SSEClient(response)
        return client.events()