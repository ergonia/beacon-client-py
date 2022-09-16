class ConfigEndpoints:
    def get_fork_schedule(self) -> dict:
        """
        Retrieve all forks, past present and future, of which this node is aware.
        """
        return self._query_url("/eth/v1/config/fork_schedule")

    def get_node_specification(self) -> dict:
        """
        Retrieve specification configuration used on this node.
        """
        return self._query_url("/eth/v1/config/spec")

    def get_deposit_contract(self) -> dict:
        """
        Retrieve Eth1 deposit contract address and chain ID.
        """
        return self._query_url("/eth/v1/config/deposit_contract")
