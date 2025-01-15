import random


class SocialEncounter:
    """
    A class to handle social encounters between PCs and NPCs, including encounter reactions
    and social checks using both charisma and wisdom.
    """

    def __init__(self, pc_charisma: int, npc_wisdom: int):
        self.pc_charisma = pc_charisma
        self.npc_wisdom = npc_wisdom
        self.base_reaction_modifiers = {
            "Hostile": -50,
            "Negative": -25,
            "Neutral": 0,
            "Positive": 20,
            "Friendly": 25,
            "Acceptance": 30
        }

    def encounter_reaction(self, situational_modifiers: int = 0) -> str:
        """
        Determine the initial reaction of an NPC or creature when encountered by the PCs.

        :param situational_modifiers: Additional modifiers based on circumstances.
        :return: The reaction of the NPC or creature.
        """
        roll = random.randint(1, 100) + (self.pc_charisma - 10) * 5 + situational_modifiers

        if roll <= 5:
            return "Hostile, immediate attack"
        elif roll <= 25:
            return "Hostile"
        elif roll <= 36:
            return "Negative"
        elif roll <= 64:
            return "Uncertain / Neutral"
        elif roll <= 75:
            return "Positive"
        elif roll <= 95:
            return "Friendly"
        else:
            return "Acceptance"

    def charisma_check(self) -> bool:
        """
        Make a charisma check for the PC attempting to influence the NPC.

        :return: True if the check is successful, False otherwise.
        """
        roll = random.randint(1, 20)
        return roll <= self.pc_charisma

    def wisdom_check(self) -> bool:
        """
        Make a wisdom check for the NPC who is being influenced.

        :return: True if the check is successful, False otherwise.
        """
        roll = random.randint(1, 20)
        return roll <= self.npc_wisdom

    def social_interaction(self) -> str:
        """
        Handle the social interaction between a PC and an NPC.

        :return: The result of the interaction.
        """
        pc_succeeds = self.charisma_check()
        npc_succeeds = self.wisdom_check()

        if pc_succeeds and not npc_succeeds:
            return "PC succeeds in influencing the NPC."
        elif not pc_succeeds and npc_succeeds:
            return "PC fails to influence the NPC."
        elif pc_succeeds and npc_succeeds:
            return "Tie; PC can try again with a -2 penalty."
        else:
            return "Tie; PC fails, and must retry if they wish."

    def apply_encounter_modifiers(self, base_reaction: str, modifiers: int) -> str:
        """
        Apply additional modifiers to the encounter reaction based on circumstances.

        :param base_reaction: The base reaction result.
        :param modifiers: Additional modifiers to apply.
        :return: The modified reaction result.
        """
        base_score = self.base_reaction_modifiers.get(base_reaction, 0)
        final_score = base_score + modifiers

        if final_score <= -50:
            return "Hostile, immediate attack"
        elif final_score <= -25:
            return "Hostile"
        elif final_score <= 0:
            return "Negative"
        elif final_score <= 20:
            return "Uncertain / Neutral"
        elif final_score <= 25:
            return "Positive"
        elif final_score <= 30:
            return "Friendly"
        else:
            return "Acceptance"


# Example usage:
pc_charisma = 15
npc_wisdom = 12
social_encounter = SocialEncounter(pc_charisma, npc_wisdom)

# Determine the NPC's initial reaction
reaction = social_encounter.encounter_reaction(situational_modifiers=10)
print(f"Initial Reaction: {reaction}")

# Handle the social interaction
interaction_result = social_encounter.social_interaction()
print(f"Interaction Result: {interaction_result}")

# Apply additional modifiers to the encounter
final_reaction = social_encounter.apply_encounter_modifiers(reaction, modifiers=5)
print(f"Final Reaction with Modifiers: {final_reaction}")
