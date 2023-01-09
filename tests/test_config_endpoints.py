from beacon_client.api import BeaconChainAPI
from beacon_client.utils.types import Fork, DepositContract, ChainId, Version, Epoch, ExecutionAddress


class TestConfigEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_get_fork_schedule(self):
        expected = [
            Fork(
                current_version=Version("0x00000000"),
                epoch=Epoch(0),
                previous_version=Version("0x00000000"),
            ),
            Fork(
                current_version=Version("0x01000000"),
                epoch=Epoch(74240),
                previous_version=Version("0x00000000"),
            ),
            Fork(
                current_version=Version("0x02000000"),
                epoch=Epoch(144896),
                previous_version=Version("0x01000000"),
            ),
        ]
        actual = self.client.get_fork_schedule()
        assert actual[0:3] == expected

    def test_get_node_specification(self):
        pass

    def test_get_deposit_contract(self):
        expected = DepositContract(
            address=ExecutionAddress("0x00000000219ab540356cbb839cbe05303d7705fa"),
            chain_id=ChainId(1),
        )
        actual = self.client.get_deposit_contract()
        assert actual == expected
