from typing import List
from .types import Fork, TypeHooks, Root, DepositContract
from dacite import from_dict, Config


class ConfigEndpoints:
    def get_fork_schedule(self) -> List[Fork]:
        """
        Retrieve all forks, past present and future, of which this node is aware.
        """
        value = self._query_url("/eth/v1/config/fork_schedule")
        data = [
            from_dict(
                data_class=Fork,
                data=fork,
                config=Config(type_hooks=TypeHooks),
            )
            for fork in value["data"]
        ]
        return data

    def get_node_specification(self) -> dict:
        """
        Retrieve specification configuration used on this node.
        """
        value = self._query_url("/eth/v1/config/spec")
        return value["data"]

    def get_deposit_contract(self) -> dict:
        """
        Retrieve Eth1 deposit contract address and chain ID.
        """
        value = self._query_url("/eth/v1/config/deposit_contract")
        data = from_dict(
            data_class=DepositContract,
            data=value["data"],
            config=Config(type_hooks=TypeHooks),
        )
        return data
