import random

class PoisonGas:
    """
    A class to represent the effects of poison gas on characters.
    """

    @staticmethod
    def hold_breath_time(constitution: int, prepared: bool, in_combat: bool) -> int:
        """
        Calculate the time a character can hold their breath based on constitution and circumstances.

        :param constitution: The constitution score of the character.
        :param prepared: Whether the character had time to fill their lungs before exposure.
        :param in_combat: Whether the character is engaged in combat or other strenuous activity.
        :return: The number of minutes the character can hold their breath.
        """
        hold_time = constitution if prepared else constitution // 2
        if in_combat:
            hold_time //= 2
        return max(1, hold_time)

    @staticmethod
    def con_check(constitution: int, elapsed_minutes: int) -> bool:
        """
        Make a CON check for the character based on how long they've held their breath.

        :param constitution: The constitution score of the character.
        :param elapsed_minutes: The number of minutes the character has been holding their breath.
        :return: True if the character passes the CON check, False if they inhale the poison.
        """
        penalty = 2 * elapsed_minutes
        con_check_roll = random.randint(1, 20) + penalty
        return con_check_roll <= constitution

    @staticmethod
    def encounter_poison_gas(constitution: int, prepared: bool, in_combat: bool) -> bool:
        """
        Simulate an encounter with poison gas.

        :param constitution: The constitution score of the character.
        :param prepared: Whether the character had time to fill their lungs before exposure.
        :param in_combat: Whether the character is engaged in combat or other strenuous activity.
        :return: True if the character survives without inhaling poison, False if they inhale the poison.
        """
        breath_time = PoisonGas.hold_breath_time(constitution, prepared, in_combat)
        for minute in range(1, breath_time + 1):
            if not PoisonGas.con_check(constitution, minute):
                return False  # The character inhales the poison
        return True  # The character survives without inhaling poison

# Example Usage:
# Character with a constitution score of 14, prepared and not in combat
character_constitution = 14
prepared = True
in_combat = False

# Simulating the encounter with poison gas
survives = PoisonGas.encounter_poison_gas(character_constitution, prepared, in_combat)

if survives:
    print("The character survives without inhaling poison.")
else:
    print("The character inhales the poison.")
