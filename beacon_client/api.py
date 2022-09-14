import requests
import urllib.parse


class BeaconChainAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
            
    #### BEACON ENDPOINTS ####
    def _query_url(self, path):
        url = urllib.parse.urljoin(self.base_url, path)
        response = requests.get(url)
        assert response.status_code == 200, f"Status Code: {response.status_code} | {response.text}"
        return response.json()
        
    def get_genesis(self):
        '''
        Retrieve details of the chain's genesis which can be used to identify chain.
        '''
        return self._query_url("/eth/v1/beacon/genesis")
    
    def get_state_root(self, state_id):
        '''
        Calculates HashTreeRoot for state with given 'state_id'. If state_id is root, same value will be returned.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/root")
    
    def get_fork_from_state(self, state_id):
        '''
        Returns Fork object for state with given 'state_id'.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/fork")
    
    def get_finality_checkpoints_from_state(self, state_id):
        '''
        Returns finality checkpoints for state with given 'state_id'. 
        In case finality is not yet achieved, checkpoint should return epoch 0 and ZERO_HASH as root.

        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/finality_checkpoints")
    
    def get_validators_from_state(self, state_id):
        '''
        Returns filterable list of validators with their balance, status and index.
        Information will be returned for all indices or public key that match known validators. 
        If an index or public key does not match any known validator, 
        no information will be returned but this will not cause an error. 
        There are no guarantees for the returned data in terms of ordering; 
        both the index and public key are returned for each validator, 
        and can be used to confirm for which inputs a response has been returned.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/validators")
    

    def get_validators_from_state_by_id(self, state_id, validator_id):
        '''
        Returns validator specified by state and id or public key along with status and balance.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/validators/{validator_id}")
    

    def get_validators_balances_from_state(self, state_id):
        '''
        Returns validator specified by state and id or public key along with status and balance.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/validator_balances")
    
    def get_committees_from_state(self, state_id, epoch=None, index=None, slot=None):
        '''
        Retrieves the committees for the given state.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/committees")
    
    def get_sync_committees_from_state(self, state_id, epoch=None):
        '''
        Retrieves the sync committees for the given state.
        '''
        return self._query_url(f"/eth/v1/beacon/states/{state_id}/sync_committees")
    
    def get_headers(self, slot=None, parent_root=None):
        '''
        Retrieves block headers matching given query. By default it will fetch current head slot blocks.
        '''
        return self._query_url("/eth/v1/beacon/headers")

    def get_headers_from_block_id(self, block_id):
        '''
        Retrieves block headers matching given query. By default it will fetch current head slot blocks.
        '''
        return self._query_url(f"/eth/v1/beacon/headers/{block_id}")
    
    def get_block_from_block_id(self, block_id):
        '''
        Retrieves block details for given block id. 
        Depending on Accept header it can be returned either as json or as bytes serialized by SSZ
        '''
        return self._query_url(f"/eth/v2/beacon/blocks/{block_id}")

    def get_block_root_from_block_id(self, block_id):
        '''
        Retrieves hashTreeRoot of BeaconBlock/BeaconBlockHeader
        '''
        return self._query_url(f"/eth/v1/beacon/blocks/{block_id}/root")
    
    def get_attestations_from_block_id(self, block_id):
        '''
        Retrieves attestation included in requested block.
        '''
        return self._query_url(f"/eth/v1/beacon/blocks/{block_id}/attestations")
    
    def get_pool_attestations(self, slot=None, committee_index=None):
        '''
        Retrieves attestations known by the node but not necessarily incorporated into any block
        '''
        return self._query_url("/eth/v1/beacon/pool/attestations")
    
    def get_pool_attester_slashings(self):
        '''
        Retrieves attester slashings known by the node but not necessarily incorporated into any block
        '''
        return self._query_url("/eth/v1/beacon/pool/attester_slashings")
    

    def get_pool_attester_slashings(self):
        '''
        Retrieves proposer slashings known by the node but not necessarily incorporated into any block
        '''
        return self._query_url("/eth/v1/beacon/pool/proposer_slashings")
    
    def get_pool_voluntary_exits(self):
        '''
        Retrieves voluntary exits known by the node but not necessarily incorporated into any block
        '''
        return self._query_url("/eth/v1/beacon/pool/voluntary_exits")
    
    #### CONFIG ENDPOINTS ####
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
    
    
    #### DEBUG ENDPOINTS ####
    
    # This page is crashing for me on the spec so will skip
    
    #### EVENT ENDPOINTS ####

    # TODO
    
    #### NODE ENDPOINTS ####
    
    # TODO

    #### VALIDATOR ENDPOINTS ####
    
    # not implemented


if __name__ == "__main__":
    api = BeaconChainAPI("http://localhost:5052")
    print(api.get_deposit_contract())
    