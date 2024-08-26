from typing import Optional
import random


class Combatant:
    """Represents a combatant in a game, with hit points, damage, and conditions."""

    def __init__(self, name: str, level: int, hit_die: int, constitution: int):
        self.name = name
        self.level = level
        self.hit_die = hit_die
        self.constitution = constitution
        self.hit_points = self.calculate_max_hit_points()
        self.current_hit_points = self.hit_points
        self.conditions = []

    def calculate_max_hit_points(self) -> int:
        """Calculate the maximum hit points based on level, hit dice, and constitution."""
        base_hp = self.level * (self.hit_die + self.get_constitution_modifier())
        return base_hp

    def get_constitution_modifier(self) -> int:
        """Determine the constitution modifier."""
        if self.constitution <= 3:
            return -3
        elif self.constitution <= 6:
            return -2
        elif self.constitution <= 9:
            return -1
        elif self.constitution <= 12:
            return 0
        elif self.constitution <= 15:
            return 1
        elif self.constitution <= 18:
            return 2
        else:
            return 3

    def take_damage(self, damage: int):
        """Apply damage to the combatant."""
        self.current_hit_points -= damage
        if self.current_hit_points <= 0:
            self.current_hit_points = 0
            self.check_for_death()
        print(f"{self.name} takes {damage} damage and is now at {self.current_hit_points}/{self.hit_points} HP.")

    def heal(self, healing: int):
        """Heal the combatant by a certain amount."""
        self.current_hit_points += healing
        if self.current_hit_points > self.hit_points:
            self.current_hit_points = self.hit_points
        print(f"{self.name} heals {healing} HP and is now at {self.current_hit_points}/{self.hit_points} HP.")

    def check_for_death(self):
        """Check if the combatant is dead."""
        if self.current_hit_points <= -10:
            print(f"{self.name} has died.")
        elif self.current_hit_points == 0:
            print(f"{self.name} is unconscious and will lose 1 HP per minute unless stabilized.")

    def stabilize(self):
        """Stabilize the combatant, stopping HP loss."""
        if self.current_hit_points < 0:
            self.current_hit_points = 1
            print(f"{self.name} is stabilized and at 1 HP, but suffers penalties until reaching half HP.")
            self.apply_penalties()

    def apply_penalties(self):
        """Apply penalties due to being severely wounded."""
        self.conditions.append("penalized")
        print(f"{self.name} is penalized: -4 to attack rolls, half speed, -20% to skills.")

    def remove_penalties(self):
        """Remove penalties when the combatant recovers to half HP or more."""
        if self.current_hit_points >= self.hit_points // 2:
            self.conditions.remove("penalized")
            print(f"{self.name} has recovered to half HP and is no longer penalized.")

    def rest(self, days: int):
        """Rest and recover HP over time."""
        if days > 7:
            healing_rate = 5
        else:
            healing_rate = 1
        healed_hp = days * healing_rate
        self.heal(healed_hp)

    def __repr__(self) -> str:
        """String representation of the combatant."""
        return f"Combatant({self.name}, Level: {self.level}, HP: {self.current_hit_points}/{self.hit_points})"


class CombatScenario:
    """Manages the combat scenario, handling actions and combatants."""

    def __init__(self, combatants: list[Combatant]):
        self.combatants = combatants

    def apply_falling_damage(self, combatant: Combatant, fall_distance: int):
        """Apply falling damage to a combatant."""
        damage = 0
        if fall_distance <= 50:
            damage = (fall_distance // 10) * random.randint(1, 6)
        else:
            damage = (5 * 6) + (fall_distance - 50) // 10 * random.randint(1, 6)
            damage = min(damage, 150)  # Cap the damage for falls greater than 100 feet
        combatant.take_damage(damage)

    def apply_gaze_attack(self, combatant: Combatant, gaze_chance: int):
        """Apply gaze attack effects."""
        if random.randint(1, 100) <= gaze_chance:
            save_roll = random.randint(1, 20)
            if save_roll < 15:  # Assuming a save DC of 15 for the example
                print(f"{combatant.name} fails to save against the gaze attack and is affected.")
                combatant.take_damage(10)  # Example damage for failing the save
            else:
                print(f"{combatant.name} saves against the gaze attack.")

    def morale_check(self, combatant: Combatant, conditions: dict):
        """Check morale based on various conditions."""
        morale_roll = random.randint(1, 20)
        modifiers = sum(conditions.values())
        morale_result = morale_roll + modifiers
        if morale_result <= 10:
            self.apply_morale_failure(combatant, morale_result)
        else:
            print(f"{combatant.name} passes the morale check.")

    def apply_morale_failure(self, combatant: Combatant, result: int):
        """Apply the results of a failed morale check."""
        if result <= 3:
            print(f"{combatant.name} makes a well-formed fighting retreat.")
        elif result <= 6:
            print(f"{combatant.name} makes a general retreat.")
        elif result <= 10:
            print(f"{combatant.name} retreats in disarray.")
        else:
            print(f"{combatant.name} surrenders.")

    def apply_critical_hit(self, combatant: Combatant, critical_type: str, base_damage: int):
        """Apply a critical hit based on the selected method."""
        if critical_type == "double_on_20":
            if random.randint(1, 20) == 20:
                combatant.take_damage(base_damage * 2)
                print(f"Critical hit! {combatant.name} takes double damage.")
        elif critical_type == "follow_through_damage":
            max_damage = random.randint(1, base_damage)
            if base_damage == max_damage:
                follow_through = random.randint(1, base_damage)
                combatant.take_damage(follow_through)
                print(f"Follow-through damage! {combatant.name} takes additional {follow_through} damage.")
        elif critical_type == "carry_over_damage":
            # Example logic for carry-over damage; assumes multiple opponents
            pass

    def run_combat_round(self):
        """Run a full combat round for all combatants."""
        print("Starting combat round.")
        for combatant in self.combatants:
            if combatant.current_hit_points > 0:
                action = random.choice(["attack", "defend", "rest"])
                if action == "attack":
                    # Example of attack handling
                    damage = random.randint(1, 10)
                    combatant.take_damage(damage)
                elif action == "defend":
                    print(f"{combatant.name} is defending this round.")
                elif action == "rest":
                    combatant.rest(1)
        print("End of combat round.")

    def __repr__(self) -> str:
        """String representation of the combat scenario."""
        return f"CombatScenario with {len(self.combatants)} combatants."


if __name__ == "__main__":
    # Example combatants
    alice = Combatant(name="Alice", level=5, hit_die=10, constitution=12)
    bob = Combatant(name="Bob", level=4, hit_die=8, constitution=14)
    charlie = Combatant(name="Charlie", level=6, hit_die=12, constitution=10)

    # Combat scenario manager
    combat_scenario = CombatScenario(combatants=[alice, bob, charlie])

    # Example falling damage
    combat_scenario.apply_falling_damage(alice, 30)

    # Example gaze attack
    combat_scenario.apply_gaze_attack(bob, gaze_chance=30)

    # Example morale check
    combat_scenario.morale_check(charlie, {"25% of friendly force eliminated": -1, "Leader incapacitated": -2})

    # Example critical hit
    combat_scenario.apply_critical_hit(alice, critical_type="double_on_20", base_damage=15)

    # Run a combat round
    combat_scenario.run_combat_round()
