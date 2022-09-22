from typing import List
from .utils.types import Fork, DepositContract
from .utils.parsing import parse_json


class ConfigEndpoints:
    def get_fork_schedule(self) -> List[Fork]:
        """
        Retrieve all forks, past present and future, of which this node is aware.
        """
        value = self._query_url("/eth/v1/config/fork_schedule")
        data = parse_json(value["data"], Fork)
        return data

    def get_node_specification(self) -> dict:
        """
        Retrieve specification configuration used on this node.
        """
        value = self._query_url("/eth/v1/config/spec")
        return value["data"]

    def get_deposit_contract(self) -> DepositContract:
        """
        Retrieve Eth1 deposit contract address and chain ID.
        """
        value = self._query_url("/eth/v1/config/deposit_contract")
        data = parse_json(value["data"], DepositContract)
        return data
