class ConfigEndpoints:
    def get_fork_schedule(self):
        '''
        Retrieve all forks, past present and future, of which this node is aware.
        '''
        return self._query_url("/eth/v1/config/fork_schedule")
    
    def get_node_specification(self):
        '''
        Retrieve specification configuration used on this node.
        '''
        return self._query_url("/eth/v1/config/spec")
    
    def get_deposit_contract(self):
        '''
        Retrieve Eth1 deposit contract address and chain ID.
        '''
        return self._query_url("/eth/v1/config/deposit_contract")
