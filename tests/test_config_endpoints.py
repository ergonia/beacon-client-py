from beacon_client.api import BeaconChainAPI
from beacon_client.types import Fork, DepositContract, ChainId


class TestConfigEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_get_fork_schedule(self):
        expected = [
            Fork(
                current_version="0x00000000",
                epoch=0,
                previous_version="0x00000000",
            ),
            Fork(
                current_version="0x01000000",
                epoch=74240,
                previous_version="0x00000000",
            ),
            Fork(
                current_version="0x02000000",
                epoch=144896,
                previous_version="0x01000000",
            ),
        ]
        actual = self.client.get_fork_schedule()
        assert actual[0:3] == expected

    def test_get_node_specification(self):
        pass

    def test_get_deposit_contract(self):
        expected = DepositContract(
            address="0x00000000219ab540356cbb839cbe05303d7705fa",
            chain_id=1,
        )
        actual = self.client.get_deposit_contract()
        assert actual == expected
