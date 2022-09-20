class ValidatorEndpoints:
    def get_block_proposers_duties(self, epoch: int) -> dict:
        """
        Request beacon node to provide all validators that are scheduled to propose a block in the given epoch.
        Duties should only need to be checked once per epoch, however a chain reorganization could occur that results in a change of duties.
        For full safety, you should monitor head events and confirm the dependent root in this response matches:

        event.current_duty_dependent_root when compute_epoch_at_slot(event.slot) == epoch
        event.block otherwise
        The dependent_root value is get_block_root_at_slot(state, compute_start_slot_at_epoch(epoch) - 1) or the genesis block root in the case of underflow.
        Args:
            epoch: provide all proposers for the given epoch value
        """
        return self._query_url(f"/eth/v1/validator/duties/proposer/{epoch}")
