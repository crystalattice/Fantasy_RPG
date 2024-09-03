import random
from enum import Enum

class InsanityType(Enum):
    """Enumeration of possible types of insanity."""
    AMNESIAC = 1
    CATATONIC = 2
    DELUSIONAL = 3
    EATING_DISORDER = 4
    ECHOLALIA = 5
    ECHOPRAXIA = 6
    ESSENTIAL_TREMOR = 7
    HALLUCINATORY = 8
    HOMICIDAL = 9
    HYSTERIA = 10
    MANIA = 11
    MELANCHOLY = 12
    MULTIPLE_PERSONALITY = 13
    OBSESSION = 14
    PARANOID = 15
    PATHOLOGICAL_LIAR = 16
    PHOBIC = 17
    PSYCHOSOMATIC_ILLNESS = 18
    SCHIZOPHASIC = 19
    SUICIDAL = 20

class Insanity:
    """Class representing the insanity inflicted on a character."""

    def __init__(self, insanity_type: InsanityType):
        """
        Initialize the Insanity class with the type of insanity.

        :param insanity_type: The type of insanity inflicted on the character.
        """
        self.insanity_type = insanity_type

    def describe(self) -> str:
        """
        Provide a description of the insanity's effects.

        :return: A string description of the insanity.
        """
        descriptions = {
            InsanityType.AMNESIAC: (
                "The victim loses all memory of his identity, the identity of friends, etc. "
                "Also, 25% of all skills, memorized spells, class abilities, etc. will be lost."
            ),
            InsanityType.CATATONIC: (
                "Victim sits unmoving, completely unresponsive to outside stimuli. "
                "They can be led around, fed, etc., but will not exhibit any real responses."
            ),
            InsanityType.DELUSIONAL: (
                "The victim will believe himself to be a famous and important personage (king, deity, archmage, etc.). "
                "Hostility will result if the delusion is challenged."
            ),
            InsanityType.EATING_DISORDER: (
                "The character will either be afflicted by bulimia, anorexia, etc. "
                "or will feel a compulsion to eat unusual things (dirt, insects, scat, etc.)."
            ),
            InsanityType.ECHOLALIA: (
                "The victim will uncontrollably echo whatever those around him say."
            ),
            InsanityType.ECHOPRAXIA: (
                "The victim will uncontrollably repeat the actions of those around him; "
                "if someone else swings a sword, he will do the same. If someone casts a spell, he will as well, etc."
            ),
            InsanityType.ESSENTIAL_TREMOR: (
                "The victim is beset by uncontrollable shaking of a hand, the head, the voice, etc. "
                "If making a STR, DEX, or CHA check, there is a -4 penalty, plus a -4 penalty 'to hit' "
                "and a 25% chance that any spell with a verbal or somatic component will be spoiled. "
                "There is also a 25% penalty to any skill or power that requires a steady hand, "
                "such as picking pockets, finding and removing traps, etc."
            ),
            InsanityType.HALLUCINATORY: (
                "The victim sees and/or hears things that aren’t there. The game master can decide what/where."
            ),
            InsanityType.HOMICIDAL: (
                "The victim will be compelled to kill some human or demi-human every 1d20 days. "
                "This is manifested not as a wild, uncontrollable fury, but rather as a sly cunning."
            ),
            InsanityType.HYSTERIA: (
                "The victim is gripped by uncontrollable laughing, crying, shrieking, etc. "
                "If a long-term illness, will affect the character for 1d20 minutes every 1d12 hours, "
                "or 20% of the time when in a dangerous situation such as combat."
            ),
            InsanityType.MANIA: (
                "The victim is beset by an uncontrollable rage, violently lashing out at any and all around him."
            ),
            InsanityType.MELANCHOLY: (
                "The victim is subject to black moods, and will exhibit a complete lack of interest in anything. "
                "There is a 20-50% chance (1d4+1x10) that any given event or situation will be ignored. "
                "The chance for ignoring something will change every month."
            ),
            InsanityType.MULTIPLE_PERSONALITY: (
                "The victim actually splits into 1d4 separate and distinct personalities, any one of which will be dominant for 1d8 days. "
                "Each personality can have its own class (and believe itself to be of a different race or gender), "
                "and should have its own intelligence, wisdom, and charisma scores. "
                "The personalities are semi-aware of each other’s existence, and usually resent or fear the others."
            ),
            InsanityType.OBSESSION: (
                "The victim will become obsessed with some project, collection, object, person, substance, etc. "
                "Pyromania and kleptomania fall within this category as well."
            ),
            InsanityType.PARANOID: (
                "The victim feels himself to be the target of shadowy enemies, sees conspiracies where none exist, "
                "and can even believe that friends or acquaintances are out to get him."
            ),
            InsanityType.PATHOLOGICAL_LIAR: (
                "The victim cannot help but spin elaborate webs of deceit, creating tall tales about himself, his companions, history, or just about anything. "
                "When confronted with either a flat-out fact or a self-contradiction, the pathological liar will deny any contradiction even exists "
                "and will merrily go on with his pathology."
            ),
            InsanityType.PHOBIC: (
                "The victim is struck by an intense fear of some object, type of creature, or situation. "
                "When faced with it, he will become completely overwhelmed by fear, depending on the severity of the exposure, to the point of temporary catatonia."
            ),
            InsanityType.PSYCHOSOMATIC_ILLNESS: (
                "The victim will believe himself to be stricken by some disease: blindness, deafness, etc. "
                "In the case of an illness, roll as if the character were actually ill; the accompanying statistic loss will still affect the character, "
                "but the illness will never be terminal. It will last as long as the insanity does, not as long as the illness would ordinarily last."
            ),
            InsanityType.SCHIZOPHASIC: (
                "The victim will babble uncontrollably, stringing together words and nonsense syllables into a 'word salad' "
                "that can be both amusing and disturbing, as occasional glimpses of lucidity seem to be buried in the verbal landslide."
            ),
            InsanityType.SUICIDAL: (
                "The victim will be fixated on his own death, and when provided with a suitable opportunity will bring it about."
            ),
        }
        return descriptions.get(self.insanity_type, "Unknown insanity")

    @staticmethod
    def random_insanity() -> 'Insanity':
        """
        Generate a random insanity type.

        :return: An Insanity object with a randomly determined insanity type.
        """
        roll = random.randint(1, 20)
        insanity_type = InsanityType(roll)
        return Insanity(insanity_type)


# Example Usage:
# Randomly generate an insanity type and describe its effects
random_insanity = Insanity.random_insanity()
print(f"Type of Insanity: {random_insanity.insanity_type.name}")
print(f"Description: {random_insanity.describe()}")
