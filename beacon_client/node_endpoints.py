class NodeEndpoints:
    def get_node_identity(self):
        '''
        Retrieves data about the node's network presence
        '''
        return self._query_url("/eth/v1/node/identity")

    def get_node_peers(self, state=None, direction=None):
        '''
        Retrieves data about the node's network peers. 
        By default this returns all peers. 
        Multiple query params are combined using AND conditions
        '''
        return self._query_url("/eth/v1/node/peers")

    def get_peer_by_id(self, peer_id: str):
        '''
        Retrieves data about the given peer
        '''
        return self._query_url(f"/eth/v1/node/peers/{peer_id}")

    def get_peer_count(self):
        '''
        Retrieves number of known peers.
        '''
        return self._query_url("/eth/v1/node/peer_count")

    def get_node_version(self):
        '''
        Requests that the beacon node identify information about its implementation in a format similar to a HTTP User-Agent field.
        '''
        return self._query_url("/eth/v1/node/version")

    def get_syncing_status(self):
        '''
        Requests the beacon node to describe if it's currently syncing or not, and if it is, what block it is up to.
        '''
        return self._query_url("/eth/v1/node/syncing")

    def get_node_health(self):
        '''
        Returns node health status in http status codes. Useful for load balancers.
        '''
        return self._query_url("/eth/v1/node/health")
