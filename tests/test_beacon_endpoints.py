from beacon_client.api import BeaconChainAPI
from beacon_client.types import GenesisDetails, FinalityCheckpoints, Checkpoint, Root
import pytest


slow_test = pytest.mark.skipif(
    "not config.getoption('--run-slow')",
    reason="Only run when --run-slow is given",
)


class TestBeaconEndpoints:
    client = BeaconChainAPI("http://localhost:5052")

    def test_genesis(self):
        expected = GenesisDetails(
            genesis_fork_version="0x00000000",
            genesis_time=1606824023,
            genesis_validators_root="0x4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95",
        )
        actual = self.client.get_genesis()
        assert actual == expected

    def test_get_state_root(self):
        expected = Root(
            "0xc719e01b197a5a2f8f1796e11122009b845d95a19538baaa49362c04f4c74480"
        )
        actual = self.client.get_state_root(state_id=4733490)
        assert actual == expected

    def test_get_fork_from_state(self):
        # this function takes too long to load
        pass

    @slow_test
    def test_get_finality_checkpoints_from_state(self):
        expected = FinalityCheckpoints(
            current_justified=Checkpoint(
                epoch=147920,
                root="0xd7aef74c750474d7a9af76c210fb5c0adb361d59571266a08e91b09182339a98",
            ),
            finalized=Checkpoint(
                epoch=147919,
                root="0xdac10002454d05664bb832b822131da6d7b0bbc17fa21fff8a376547a043a6ad",
            ),
            previous_justified=Checkpoint(
                epoch=147919,
                root="0xdac10002454d05664bb832b822131da6d7b0bbc17fa21fff8a376547a043a6ad",
            ),
        )
        actual = self.client.get_finality_checkpoints_from_state(state_id=4733490)
        assert actual == expected

    @slow_test
    def test_get_validators_from_state(self):
        expected = {
            "balance": "33330442051",
            "index": "0",
            "status": "active_ongoing",
            "validator": {
                "activation_eligibility_epoch": "0",
                "activation_epoch": "0",
                "effective_balance": "32000000000",
                "exit_epoch": "18446744073709551615",
                "pubkey": "0x933ad9491b62059dd065b560d256d8957a8c402cc6e8d8ee7290ae11e8f7329267a8811c397529dac52ae1342ba58c95",
                "slashed": False,
                "withdrawable_epoch": "18446744073709551615",
                "withdrawal_credentials": "0x00f50428677c60f997aadeab24aabf7fceaef491c96a52b463ae91f95611cf71",
            },
        }
        actual = self.client.get_validators_from_state(state_id=1000490, active=True)
        assert actual["data"][0] == expected

    @slow_test
    def test_get_validators_from_state_by_id(self):
        expected = {
            "data": {
                "balance": "35918785526",
                "index": "0",
                "status": "active_ongoing",
                "validator": {
                    "activation_eligibility_epoch": "0",
                    "activation_epoch": "0",
                    "effective_balance": "32000000000",
                    "exit_epoch": "18446744073709551615",
                    "pubkey": "0x933ad9491b62059dd065b560d256d8957a8c402cc6e8d8ee7290ae11e8f7329267a8811c397529dac52ae1342ba58c95",
                    "slashed": False,
                    "withdrawable_epoch": "18446744073709551615",
                    "withdrawal_credentials": "0x00f50428677c60f997aadeab24aabf7fceaef491c96a52b463ae91f95611cf71",
                },
            },
            "execution_optimistic": False,
        }
        actual = self.client.get_validators_from_state_by_id(
            state_id="0xc719e01b197a5a2f8f1796e11122009b845d95a19538baaa49362c04f4c74480",
            validator_id="0x933ad9491b62059dd065b560d256d8957a8c402cc6e8d8ee7290ae11e8f7329267a8811c397529dac52ae1342ba58c95",
        )
        assert actual == expected

    @slow_test
    def test_get_validator_balances_from_state(self):
        expected = {
            "data": [{"balance": "35918785526", "index": "0"}],
            "execution_optimistic": False,
        }
        actual = self.client.get_validators_balances_from_state(
            4733490,
            validator_list=[
                "0x933ad9491b62059dd065b560d256d8957a8c402cc6e8d8ee7290ae11e8f7329267a8811c397529dac52ae1342ba58c95"
            ],
        )
        assert actual == expected

    @slow_test
    def test_get_committees_from_state(self):
        expected = {
            "data": [
                {
                    "index": "4",
                    "slot": "4733472",
                    "validators": [
                        "126043",
                        "191550",
                        "154277",
                        "106864",
                        "139802",
                        "181242",
                        "77541",
                        "12589",
                        "20592",
                        "26300",
                        "23184",
                        "10230",
                        "351673",
                        "359545",
                        "12411",
                        "285308",
                        "122207",
                        "198682",
                        "362129",
                        "343523",
                        "70941",
                        "301741",
                        "105472",
                        "76581",
                        "260160",
                        "244667",
                        "307287",
                        "334261",
                        "84679",
                        "222274",
                        "407706",
                        "68747",
                        "40511",
                        "378698",
                        "333733",
                        "420488",
                        "252066",
                        "64795",
                        "378584",
                        "275514",
                        "50059",
                        "431097",
                        "69177",
                        "48467",
                        "100132",
                        "138981",
                        "100007",
                        "238675",
                        "217401",
                        "64578",
                        "223004",
                        "324121",
                        "204853",
                        "407361",
                        "339766",
                        "282769",
                        "277799",
                        "345095",
                        "208278",
                        "428858",
                        "49588",
                        "191064",
                        "362059",
                        "428197",
                        "22043",
                        "247940",
                        "238269",
                        "216692",
                        "151698",
                        "155813",
                        "159849",
                        "188040",
                        "170646",
                        "308898",
                        "337713",
                        "276796",
                        "51308",
                        "131802",
                        "204766",
                        "198101",
                        "153697",
                        "193496",
                        "81161",
                        "338814",
                        "185502",
                        "284591",
                        "231894",
                        "212046",
                        "72692",
                        "319258",
                        "358485",
                        "20265",
                        "232727",
                        "323991",
                        "348781",
                        "245499",
                        "321176",
                        "135555",
                        "230013",
                        "223643",
                        "359231",
                        "38591",
                        "389632",
                        "396898",
                        "125244",
                        "64553",
                        "33387",
                        "194384",
                        "339512",
                        "310729",
                        "11840",
                        "269233",
                        "373798",
                        "138216",
                        "238287",
                        "104663",
                        "197857",
                        "178522",
                        "49229",
                        "117322",
                        "4287",
                        "37011",
                        "371339",
                        "56020",
                        "379099",
                        "303096",
                        "325536",
                        "137305",
                        "235433",
                        "292264",
                        "271164",
                        "29003",
                        "87390",
                        "167200",
                        "426181",
                        "66185",
                        "872",
                        "58468",
                        "259398",
                        "192272",
                        "40084",
                        "208894",
                        "38739",
                        "183695",
                        "130138",
                        "295933",
                        "343037",
                        "142495",
                        "376132",
                        "258123",
                        "15066",
                        "306620",
                        "365674",
                        "138184",
                        "152481",
                        "174812",
                        "284001",
                        "41300",
                        "343237",
                        "98563",
                        "254840",
                        "249883",
                        "221258",
                        "252570",
                        "83506",
                        "191014",
                        "26318",
                        "210110",
                        "374469",
                        "430635",
                        "204477",
                        "106196",
                        "67564",
                        "337011",
                        "166386",
                        "214432",
                        "224243",
                        "412620",
                        "87170",
                        "188829",
                        "258751",
                        "27357",
                        "79818",
                        "57834",
                        "387404",
                        "143502",
                        "359825",
                        "159969",
                        "406360",
                        "318101",
                        "290189",
                        "210138",
                        "422702",
                        "361788",
                        "302072",
                        "114468",
                        "223197",
                        "65267",
                        "104108",
                        "233160",
                        "425935",
                        "2178",
                        "11448",
                        "129618",
                        "273697",
                        "214625",
                        "180746",
                        "301633",
                        "153997",
                        "403683",
                    ],
                }
            ],
            "execution_optimistic": False,
        }
        actual = self.client.get_committees_from_state(
            state_id=4733490, index=4, slot=4733472
        )
        assert actual == expected

    @slow_test
    def test_get_sync_committees_from_state(self):
        expected = [
            "277496",
            "50668",
            "24975",
            "401625",
            "314279",
            "150950",
            "355117",
            "17656",
            "17101",
            "221531",
            "368962",
            "273991",
            "101600",
            "133288",
            "56844",
            "379769",
            "299095",
            "206685",
            "148704",
            "7559",
            "422792",
            "194172",
            "54428",
            "347965",
            "242550",
            "43919",
            "261044",
            "363732",
            "296862",
            "309518",
            "105942",
            "418682",
            "148329",
            "255854",
            "369345",
            "187924",
            "180546",
            "77913",
            "52368",
            "212019",
            "278354",
            "132331",
            "272153",
            "73684",
            "184884",
            "378499",
            "384762",
            "288509",
            "270748",
            "363074",
            "40565",
            "38710",
            "362676",
            "141357",
            "354759",
            "39823",
            "212895",
            "201662",
            "398384",
            "225656",
            "95292",
            "55155",
            "373703",
            "245780",
            "275595",
            "296527",
            "355924",
            "206410",
            "37152",
            "86000",
            "302114",
            "295114",
            "166807",
            "355659",
            "399540",
            "418159",
            "190764",
            "228000",
            "408872",
            "104143",
            "236309",
            "291627",
            "176436",
            "197837",
            "168597",
            "58207",
            "407673",
            "88445",
            "429393",
            "344613",
            "353447",
            "138000",
            "165004",
            "141972",
            "211020",
            "81322",
            "406918",
            "200730",
            "22508",
            "3396",
            "128487",
            "280394",
            "250404",
            "114475",
            "70844",
            "181687",
            "209717",
            "375122",
            "406288",
            "125649",
            "68061",
            "116989",
            "280922",
            "21174",
            "168342",
            "165810",
            "385449",
            "57114",
            "25351",
            "287834",
            "169884",
            "194121",
            "153574",
            "143741",
            "70225",
            "335791",
            "60852",
            "307443",
        ]
        actual = self.client.get_sync_committees_from_state(
            state_id="0xc719e01b197a5a2f8f1796e11122009b845d95a19538baaa49362c04f4c74480"
        )
        assert actual["data"]["validator_aggregates"][0] == expected

    def test_get_headers(self):
        expected = {
            "data": [
                {
                    "canonical": True,
                    "header": {
                        "message": {
                            "body_root": "0x924a8bf65cc67827c25c76ddb7f376461e3c59033638e292668495bef17414c1",
                            "parent_root": "0x8015f2fb159f85fd46686c09f6a588ec901f9cc11613f1cdeb24864414ca8f97",
                            "proposer_index": "170574",
                            "slot": "4733490",
                            "state_root": "0xc719e01b197a5a2f8f1796e11122009b845d95a19538baaa49362c04f4c74480",
                        },
                        "signature": "0xaa5e271443b1a2027e5b7a1d587c59d43854aad3926fa9424a2723b493536ee46d62bd2ccc74ec5bbbe480af81bcf17d07893feea8c11708d3d838b3e8fae3e426fb525a09192ecc8f364240e127f7c5296bcfb1921dc06831c6fdcee0f2316b",
                    },
                    "root": "0xd4046c8c2de7263edfd239e42e9dd892c07bb99c7222107908aac26767c39c8e",
                }
            ],
            "execution_optimistic": True,
        }
        actual = self.client.get_headers(slot=4733490)
        assert actual == expected

    def test_get_headers_from_block_id(self):
        expected = {
            "data": {
                "canonical": True,
                "header": {
                    "message": {
                        "body_root": "0x924a8bf65cc67827c25c76ddb7f376461e3c59033638e292668495bef17414c1",
                        "parent_root": "0x8015f2fb159f85fd46686c09f6a588ec901f9cc11613f1cdeb24864414ca8f97",
                        "proposer_index": "170574",
                        "slot": "4733490",
                        "state_root": "0xc719e01b197a5a2f8f1796e11122009b845d95a19538baaa49362c04f4c74480",
                    },
                    "signature": "0xaa5e271443b1a2027e5b7a1d587c59d43854aad3926fa9424a2723b493536ee46d62bd2ccc74ec5bbbe480af81bcf17d07893feea8c11708d3d838b3e8fae3e426fb525a09192ecc8f364240e127f7c5296bcfb1921dc06831c6fdcee0f2316b",
                },
                "root": "0xd4046c8c2de7263edfd239e42e9dd892c07bb99c7222107908aac26767c39c8e",
            },
            "execution_optimistic": True,
        }
        actual = self.client.get_headers_from_block_id(block_id=4733490)
        assert actual == expected

    def test_get_block_from_block_id(self):
        # this test goes stale too quickly
        pass

    def test_get_block_root_from_block_id(self):
        expected = {
            "data": {
                "root": "0xd4046c8c2de7263edfd239e42e9dd892c07bb99c7222107908aac26767c39c8e"
            },
            "execution_optimistic": True,
        }
        actual = self.client.get_block_root_from_block_id(block_id=4733490)
        assert actual == expected

    def test_get_attestations_from_block_id(self):
        expected = {
            "aggregation_bits": "0xffffffffffffffffffffffffffffffffffffffffffffffffffff0f",
            "data": {
                "beacon_block_root": "0x8015f2fb159f85fd46686c09f6a588ec901f9cc11613f1cdeb24864414ca8f97",
                "index": "47",
                "slot": "4733489",
                "source": {
                    "epoch": "147920",
                    "root": "0xd7aef74c750474d7a9af76c210fb5c0adb361d59571266a08e91b09182339a98",
                },
                "target": {
                    "epoch": "147921",
                    "root": "0x0e69a750d555cf8bb5ac46b1524d808bcbdec49173f6d8dd963f161a59fa4eac",
                },
            },
            "signature": "0x8e292242b012e0820ea28579efa776a336f1371345dbdfaad9df0b7158d0ae3492b8cec1a22779ad909f10d1cb2a4c570182ffad65c9fcf9ddc73105fc6b75af7984eb74660f10e5de01b4dbdeecd44b37d19a41fe10eec5a799d31f0daa2cb1",
        }
        actual = self.client.get_attestations_from_block_id(block_id=4733490)
        assert actual["data"][0] == expected

    def test_get_pool_attestations(self):
        # specific to validator
        pass

    def test_get_pool_attester_slashings(self):
        # specific to validator
        pass

    def test_pool_proposer_slashings(self):
        # specific to validator
        pass

    def test_get_pool_voluntary_exits(self):
        # specific to validator
        pass
