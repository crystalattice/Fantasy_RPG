import random
from typing import List, Dict, Tuple


class Combatant:
    """Represents a combatant in a combat scenario."""

    def __init__(self, name: str, initiative: int, surprise_die: int = 6):
        self.name = name
        self.initiative = initiative
        self.surprise_die = surprise_die
        self.current_segment = 0
        self.actions_taken = False
        self.surprised = False
        self.surprise_bonus = 0

    def reset_for_new_round(self):
        """Resets the combatant's actions and segment for the new round."""
        self.current_segment = 0
        self.actions_taken = False
        self.surprised = False
        self.surprise_bonus = 0

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

    def roll_for_surprise(self) -> int:
        """
        Rolls to determine if the combatant is surprised.

        Returns:
            int: The result of the surprise roll.
        """
        return random.randint(1, self.surprise_die)

    def apply_surprise(self, bonus: int):
        """Applies the surprise bonus or penalty to the combatant."""
        self.surprised = True
        self.surprise_bonus = bonus
        print(f"{self.name} is surprised and suffers a +{bonus} penalty to initiative.")


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

    def determine_surprise(self) -> Tuple[int, int]:
        """
        Determines surprise for the combat.

        Returns:
            Tuple[int, int]: The penalties to apply to each side.
        """
        player_roll = min([combatant.roll_for_surprise() for combatant in self.combatants])
        foe_roll = random.randint(1, 6)  # Assuming foes use d6 for surprise

        player_bonus = max(0, foe_roll - player_roll)
        foe_bonus = max(0, player_roll - foe_roll)

        for combatant in self.combatants:
            if player_bonus > 0:
                combatant.apply_surprise(player_bonus)

        return player_bonus, foe_bonus


if __name__ == "__main__":
    # Example combatants
    alice = Combatant(name="Alice", initiative=8, surprise_die=8)  # Ranger with d8 surprise roll
    bob = Combatant(name="Bob", initiative=5)
    charlie = Combatant(name="Charlie", initiative=7)

    # Combat round manager
    combat_round = CombatRound(combatants=[alice, bob, charlie])

    # Determine surprise
    player_bonus, foe_bonus = combat_round.determine_surprise()
    print(f"Player side surprise bonus: {player_bonus}, Foe side surprise bonus: {foe_bonus}")

    # Run a round of combat with potential surprise penalties
    combat_round.run_round()
