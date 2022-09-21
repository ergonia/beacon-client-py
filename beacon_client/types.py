from typing import NewType, Union, List
from dataclasses import dataclass
from bitstring import BitArray


# CONSTANTS

# Misc Parameters
MAX_COMMITTEES_PER_SLOT = 64
TARGET_COMMITTEE_SIZE = 128
MAX_VALIDATORS_PER_COMMITTEE = 2048
SHUFFLE_ROUND_COUNT = 90
HYSTERESIS_QUOTIENT = 4
HYSTERESIS_DOWNWARD_MULTIPLIER = 1
HYSTERESIS_UPWARD_MULTIPLIER = 5

# Gwei Parameters
MIN_DEPOSIT_AMOUNT = 10**9
MAX_EFFECTIVE_BALANCE = 32 * 10**9
EFFECTIVE_BALANCE_INCREMENT = 10**9

# Time Parameters
MIN_ATTESTATION_INCLUSION_DELAY = 1
SLOTS_PER_EPOCH = 32
MIN_SEED_LOOKAHEAD = 1
MAX_SEED_LOOKAHEAD = 4
MIN_EPOCHS_TO_INACTIVITY_PENALTY = 4
EPOCHS_PER_ETH1_VOTING_PERIOD = 64
SLOTS_PER_HISTORICAL_ROOT = 8192

# State List Lengths
EPOCHS_PER_HISTORICAL_VECTOR = 2**16
EPOCHS_PER_SLASHINGS_VECTOR = 2**13
HISTORICAL_ROOTS_LIMIT = 2**24
VALIDATOR_REGISTRY_LIMIT = 2**40

# Rewards and penalties
BASE_REWARD_FACTOR = 2**6
WHISTLEBLOWER_REWARD_QUOTIENT = 2**9
PROPOSER_REWARD_QUOTIENT = 2**3
INACTIVITY_PENALTY_QUOTIENT = 2**26
MIN_SLASHING_PENALTY_QUOTIENT = 2**7
PROPORTIONAL_SLASHING_MULTIPLIER = 1

# Max operations per block
MAX_PROPOSER_SLASHINGS = 16
MAX_ATTESTER_SLASHINGS = 2
MAX_ATTESTATIONS = 128
MAX_DEPOSITS = 16
MAX_VOLUNTARY_EXITS = 16

# SIMPLE TYPES
Slot = NewType("Slot", int)
Epoch = NewType("Epoch", int)
Root = NewType("Root", str)
Head = "head"
Genesis = "genesis"
Justified = "justified"
Finalized = "finalized"
StateId = Union[Slot, Root, Head, Genesis, Justified, Finalized]
BlockId = Union[Slot, Root, Head, Genesis, Finalized]
PeerId = NewType("PeerId", str)

PendingInitialized = "pending_initialized"
PendingQueued = "pending_queued"
ActiveOngoing = "active_ongoing"
ActiveExiting = "active_exiting"
ActiveSlashed = "active_slashed"
ExitedUnslashed = "exited_unslashed"
ExitedSlashed = "exited_slashed"
WithdrawalPossible = "withdrawal_possible"
WithdrawalDone = "withdrawal_done"
Active = "active"
Pending = "pending"
Exited = "exited"
Withdrawal = "withdrawal"
ValidatorStatus = Union[
    PendingInitialized,
    PendingQueued,
    ActiveOngoing,
    ActiveExiting,
    ActiveSlashed,
    ExitedUnslashed,
    ExitedSlashed,
    WithdrawalPossible,
    WithdrawalDone,
    Active,
    Pending,
    Exited,
    Withdrawal,
]

Disconnected = "disconnected"
Connecting = "connecting"
Connected = "connected"
Disconnecting = "disconnecting"
PeerState = Union[Disconnected, Connecting, Connected, Disconnecting]

Head = "head"
Block = "block"
Attestation = "attestation"
VoluntaryExit = "voluntary_exit"
FinalizedCheckpoint = "finalized_checkpoint"
ChainReorg = "chain_reorg"
ContributionAndProof = "contribution_and_proof"
EventTopic = Union[
    Head,
    Block,
    Attestation,
    VoluntaryExit,
    FinalizedCheckpoint,
    ChainReorg,
    ContributionAndProof,
]

Inbound = "inbound"
Outbound = "outbound"
ConnectionOrientation = Union[Inbound, Outbound]

Ready = "ready"
Syncing = "syncing"
NotInitialized = "not_initizlized"
Unknown = "unknown"
HealthStatus = Union[Ready, Syncing, NotInitialized, Unknown]

CommitteeIndex = NewType("CommitteeIndex", int)
ValidatorIndex = NewType("ValidatorIndex", int)
Gwei = NewType("Gwei", int)
Version = NewType("Version", str)
DomainType = NewType("DomainType", str)
ForkDigest = NewType("ForkDigest", str)
Domain = NewType("Domain", str)
BLSPubkey = NewType("BLSPubkey", str)
BLSSignature = NewType("BLSSignature", str)
ValidatorId = Union[ValidatorIndex, BLSPubkey]
Bytes32 = NewType("Bytes32", str)


# COMPLEX TYPES
@dataclass
class Fork:
    previous_version: Version
    current_version: Version
    epoch: Epoch  # Epoch of latest fork


@dataclass
class ForkData:
    current_version: Version
    genesis_validators_root: Root


@dataclass
class Checkpoint:
    epoch: Epoch
    root: Root


@dataclass
class Validator:
    pubkey: BLSPubkey
    withdrawal_credentials: Bytes32  # Commitment to pubkey for withdrawals
    effective_balance: Gwei  # Balance at stake
    slashed: bool
    # Status epochs
    activation_eligibility_epoch: Epoch  # When criteria for activation were met
    activation_epoch: Epoch
    exit_epoch: Epoch
    withdrawable_epoch: Epoch


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
    attesting_indices: List[ValidatorIndex]
    data: AttestationData
    signature: BLSSignature


@dataclass
class PendingAttestation:
    aggregation_bits: BitArray
    data: AttestationData
    inclusion_delay: Slot
    proposer_index: ValidatorIndex


@dataclass
class Eth1Data:
    deposit_root: Root
    deposit_count: int
    block_hash: Bytes32


@dataclass
class HistoricalBatch:
    block_roots: List[Root]
    state_roots: List[Root]


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
class AttesterSlashing:
    attestation_1: IndexedAttestation
    attestation_2: IndexedAttestation


@dataclass
class Attestation:
    aggregation_bits: BitArray
    data: AttestationData
    signature: BLSSignature


@dataclass
class Deposit:
    proof: List[Bytes32]  # Merkle path to deposit root
    data: DepositData


@dataclass
class VoluntaryExit:
    epoch: Epoch  # Earliest epoch when voluntary exit can be processed
    validator_index: ValidatorIndex


@dataclass
class SignedBeaconBlockHeader:
    message: BeaconBlockHeader
    signature: BLSSignature


@dataclass
class ProposerSlashing:
    signed_header_1: SignedBeaconBlockHeader
    signed_header_2: SignedBeaconBlockHeader


@dataclass
class SignedVoluntaryExit:
    message: VoluntaryExit
    signature: BLSSignature


# i think this changed
@dataclass
class BeaconBlockBody:
    randao_reveal: BLSSignature
    eth1_data: Eth1Data  # Eth1 data vote
    graffiti: Bytes32  # Arbitrary data
    # Operations
    proposer_slashings: List[ProposerSlashing]
    attester_slashings: List[AttesterSlashing]
    attestations: List[Attestation]
    deposits: List[Deposit]
    voluntary_exits: List[SignedVoluntaryExit]


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
    genesis_time: int
    genesis_validators_root: Root
    slot: Slot
    fork: Fork
    # History
    latest_block_header: BeaconBlockHeader
    block_roots: List[Root]
    state_roots: List[Root]
    historical_roots: List[Root]
    # Eth1
    eth1_data: Eth1Data
    eth1_data_votes: List[Eth1Data]
    eth1_deposit_index: int
    # Registry
    validators: List[Validator]
    balances: List[Gwei]
    # Randomness
    randao_mixes: List[Bytes32]
    # Slashings
    slashings: List[Gwei]  # Per-epoch sums of slashed effective balances
    # Attestations
    previous_epoch_attestations: List[PendingAttestation]
    current_epoch_attestations: List[PendingAttestation]
    # Finality
    justification_bits: BitArray  # Bit set for every recent justified epoch
    previous_justified_checkpoint: Checkpoint  # Previous epoch snapshot
    current_justified_checkpoint: Checkpoint
    finalized_checkpoint: Checkpoint


@dataclass
class SignedBeaconBlock:
    message: BeaconBlock
    signature: BLSSignature


@dataclass
class GenesisDetails:
    genesis_fork_version: Version
    genesis_time: int
    genesis_validators_root: Root


@dataclass
class FinalityCheckpoints:
    previous_justified: Checkpoint
    current_justified: Checkpoint
    finalized: Checkpoint


@dataclass
class ValidatorSummary:
    index: ValidatorIndex
    balance: Gwei
    status: ValidatorStatus
    validator: Validator


@dataclass
class BalanceSummary:
    index: ValidatorIndex
    balance: Gwei


@dataclass
class CommitteeSummary:
    index: CommitteeIndex
    slot: Slot
    validators: List[ValidatorIndex]


@dataclass
class SyncCommitteeSummary:
    validators: List[ValidatorIndex]
    validator_aggregates: List[List[ValidatorIndex]]


@dataclass
class BeaconHeaderSummary:
    root: Root
    canonical: bool
    signed_header: SignedBeaconBlockHeader


@dataclass
class PeerDescriptor:
    state: PeerState
    direction: ConnectionOrientation
