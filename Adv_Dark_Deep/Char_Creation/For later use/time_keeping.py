from typing import List, Dict


class Combatant:
    """Represents a combatant in a combat scenario."""

    def __init__(self, name: str, initiative: int):
        self.name = name
        self.initiative = initiative
        self.current_segment = 0
        self.actions_taken = False

    def reset_for_new_round(self):
        """Resets the combatant's actions and segment for the new round."""
        self.current_segment = 0
        self.actions_taken = False

    def take_action(self, segment: int) -> bool:
        """
        Allows the combatant to take an action if they haven't already.
        Args:
            segment (int): The current segment of the round.

        Returns:
            bool: True if action is taken, False if already acted.
        """
        if not self.actions_taken:
            self.current_segment = segment
            self.actions_taken = True
            print(f"{self.name} takes action in segment {segment}.")
            return True
        return False


class CombatRound:
    """Manages the timing of actions in a combat round."""

    def __init__(self, combatants: List[Combatant]):
        self.combatants = sorted(combatants, key=lambda x: x.initiative, reverse=True)
        self.current_segment = 1
        self.round = 1

    def next_segment(self):
        """Advances the combat to the next segment."""
        if self.current_segment < 10:
            self.current_segment += 1
        else:
            self.end_of_round()

    def end_of_round(self):
        """Handles the end of the round, resetting for the next round."""
        print(f"End of round {self.round}.")
        self.current_segment = 1
        self.round += 1
        for combatant in self.combatants:
            combatant.reset_for_new_round()

    def resolve_actions(self):
        """Resolves actions for the current segment."""
        for combatant in self.combatants:
            if combatant.initiative >= self.current_segment:
                combatant.take_action(self.current_segment)

    def run_round(self):
        """Runs a full round of combat."""
        print(f"Starting round {self.round}.")
        while self.current_segment <= 10:
            print(f"Segment {self.current_segment}")
            self.resolve_actions()
            self.next_segment()


if __name__ == "__main__":
    # Example combatants
    alice = Combatant(name="Alice", initiative=8)
    bob = Combatant(name="Bob", initiative=5)
    charlie = Combatant(name="Charlie", initiative=7)

    # Combat round manager
    combat_round = CombatRound(combatants=[alice, bob, charlie])

    # Run a few rounds of combat
    combat_round.run_round()
    combat_round.run_round()
