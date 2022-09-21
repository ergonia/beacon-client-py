from typing import NewType


Slot = NewType("Slot", int)
Epoch = NewType("Epoch", int)
Root = NewType("Root", str)

CommitteeIndex = NewType("CommitteeIndex", int)
ValidatorIndex = NewType("ValidatorIndex", int)
Gwei = NewType("Gwei", int)
Version = NewType("Version", int)
DomainType = NewType("DomainType", str)
ForkDigest = NewType("ForkDigest", str)
Domain = NewType("Domain", str)
BLSPubkey = NewType("BLSPubkey", str)
BLSSignature = NewType("BLSSignature", str)


@dataclass
class AttestationData:
    slot: Slot
    index: CommitteeIndex
    # LMD GHOST vote
    beacon_block_root: Root
    # FFG vote
    source: Checkpoint
    target: Checkpoint

@dataclass
class IndexedAttestation:
    attesting_indices: List[ValidatorIndex, MAX_VALIDATORS_PER_COMMITTEE]
    data: AttestationData
    signature: BLSSignature

@dataclass
class PendingAttestation:
    aggregation_bits: Bitlist[MAX_VALIDATORS_PER_COMMITTEE]
    data: AttestationData
    inclusion_delay: Slot
    proposer_index: ValidatorIndex

@dataclass
class Eth1Data:
    deposit_root: Root
    deposit_count: uint64
    block_hash: Bytes32

@dataclass
class HistoricalBatch:
    block_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]
    state_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]

@dataclass
class DepositMessage:
    pubkey: BLSPubkey
    withdrawal_credentials: Bytes32
    amount: Gwei

@dataclass
class DepositData:
    pubkey: BLSPubkey
    withdrawal_credentials: Bytes32
    amount: Gwei
    signature: BLSSignature

@dataclass
class BeaconBlockHeader:
    slot: Slot
    proposer_index: ValidatorIndex
    parent_root: Root
    state_root: Root
    body_root: Root

@dataclass
class SigningData:
    object_root: Root
    domain: Domain

@dataclass
class ProposerSlashing:
    signed_header_1: SignedBeaconBlockHeader
    signed_header_2: SignedBeaconBlockHeader

@dataclass
class AttesterSlashing:
    attestation_1: IndexedAttestation
    attestation_2: IndexedAttestation

@dataclass
class Attestation:
    aggregation_bits: Bitlist[MAX_VALIDATORS_PER_COMMITTEE]
    data: AttestationData
    signature: BLSSignature

@dataclass
class Deposit:
    proof: Vector[Bytes32, DEPOSIT_CONTRACT_TREE_DEPTH + 1]  # Merkle path to deposit root
    data: DepositData

@dataclass
class VoluntaryExit:
    epoch: Epoch  # Earliest epoch when voluntary exit can be processed
    validator_index: ValidatorIndex


# i think this changed
@dataclass
class BeaconBlockBody:
    randao_reveal: BLSSignature
    eth1_data: Eth1Data  # Eth1 data vote
    graffiti: Bytes32  # Arbitrary data
    # Operations
    proposer_slashings: List[ProposerSlashing, MAX_PROPOSER_SLASHINGS]
    attester_slashings: List[AttesterSlashing, MAX_ATTESTER_SLASHINGS]
    attestations: List[Attestation, MAX_ATTESTATIONS]
    deposits: List[Deposit, MAX_DEPOSITS]
    voluntary_exits: List[SignedVoluntaryExit, MAX_VOLUNTARY_EXITS]


@dataclass
class BeaconBlock:
    slot: Slot
    proposer_index: ValidatorIndex
    parent_root: Root
    state_root: Root
    body: BeaconBlockBody

@dataclass
class BeaconState:
    # Versioning
    genesis_time: uint64
    genesis_validators_root: Root
    slot: Slot
    fork: Fork
    # History
    latest_block_header: BeaconBlockHeader
    block_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]
    state_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]
    historical_roots: List[Root, HISTORICAL_ROOTS_LIMIT]
    # Eth1
    eth1_data: Eth1Data
    eth1_data_votes: List[Eth1Data, EPOCHS_PER_ETH1_VOTING_PERIOD * SLOTS_PER_EPOCH]
    eth1_deposit_index: uint64
    # Registry
    validators: List[Validator, VALIDATOR_REGISTRY_LIMIT]
    balances: List[Gwei, VALIDATOR_REGISTRY_LIMIT]
    # Randomness
    randao_mixes: Vector[Bytes32, EPOCHS_PER_HISTORICAL_VECTOR]
    # Slashings
    slashings: Vector[Gwei, EPOCHS_PER_SLASHINGS_VECTOR]  # Per-epoch sums of slashed effective balances
    # Attestations
    previous_epoch_attestations: List[PendingAttestation, MAX_ATTESTATIONS * SLOTS_PER_EPOCH]
    current_epoch_attestations: List[PendingAttestation, MAX_ATTESTATIONS * SLOTS_PER_EPOCH]
    # Finality
    justification_bits: Bitvector[JUSTIFICATION_BITS_LENGTH]  # Bit set for every recent justified epoch
    previous_justified_checkpoint: Checkpoint  # Previous epoch snapshot
    current_justified_checkpoint: Checkpoint
    finalized_checkpoint: Checkpoint