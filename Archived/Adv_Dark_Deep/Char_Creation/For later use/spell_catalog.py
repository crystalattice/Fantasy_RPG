spells = {
    "Acid Arrow": {
        "level": 2,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "dart", "powdered rhubarb leaf", "adder stomach"],
        "range": "see description",
        "duration": "see description",
        "area_of_effect": "single target",
        "saving_throw": "none",
        "description": """
            This spell calls forth an enchanted arrow made of pure green acid, which flies forth at the designated target as if it were an arrow +1 fired from a longbow by a fighter of the same level as the caster. 
            When it hits, the arrow itself does 2-5 h.p. of damage. The target is also splashed with the acid of the arrow (and thus creatures that would not normally be damaged by such an arrow may still be harmed by the acid, and vice versa). 
            The acid itself causes 2d4 h.p. of damage per minute in a 1’ diameter area, and those items vulnerable to acid damage must make saving throws. 
            The number of minutes the acid persists depends on the level of the caster: 1 minute for every three levels. Thus a 4th level caster would evoke an arrow whose acid would remain for 2 minutes, doing 2d4 h.p. per minute, 
            a 7th level caster’s arrow would last 3 minutes, etc. The spell requires a normal dart, powdered rhubarb, and the stomach of an adder. All are lost in the casting.
        """,
    },
    "Abjure (Implore)": {
        "level": 4,
        "class": ["cleric"],
        "school": "abjuration",
        "casting_time": "1 minute",
        "components": ["incantation", "gestures", "holy symbol", "holy water", "other (see description)"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "special",
        "description": """
            This spell allows the caster to attempt to send a creature from some other plane of existence back to its home plane. 
            The spell requires that the caster know the name of the creature to be sent back (if any) or the specific type of creature 
            (for instance, most lesser demons and devils don’t have proper names). The creature to be abjured must be touched by the caster, 
            and is entitled to a special saving throw; the base chance of success is 50%, adjusted by 1% for every difference in levels/hit dice 
            between the caster and the target. The spell requires the caster’s holy symbol (which is not consumed by the casting of the spell), 
            as well as holy water and some other substance which is inimical to the target creature (iron to a demon, silver to a devil, etc.).
            The reverse of the spell, implore, allows the caster to summon some being from another plane with a similar alignment, with the 
            same percent chance of success as described above for abjuring an extra-planar creature. Deities of any sort are immune to the spell’s effects, 
            although their servants are not, however in any case there is no telling whether the being that answers the caster’s imploring will indeed be friendly. 
            This spell has the same components as abjure, except that some substance desired by the targeted being must be provided.
        """,
    },
    # Additional spells will follow in a similar format.
}
spells.update({
    "Aid": {
        "level": 2,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "1 turn + 1 round/level",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Aid grants the target creature a bonus of 1d8 hit points, and also provides a +1 bonus to attack rolls and saving throws for the spell’s duration. 
            The temporary hit points are the first to be lost if the creature takes damage. The spell ends either when the duration runs out or when the hit points 
            granted by the spell are lost. If the spell is cast on a creature already at full hit points, the temporary hit points will stack on top of the creature’s 
            existing hit points.
        """,
    },
    "Animal Growth": {
        "level": 4,
        "class": ["cleric", "druid"],
        "school": "alteration",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "120 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "1 or more animals within a 20’ cube",
        "saving_throw": "none",
        "description": """
            This spell causes up to 8 animals within the area of effect to double in size, along with a proportional increase in weight and strength. 
            The spell can only affect animals, not magical creatures or monsters. A successful casting means the animal’s hit points are doubled, and all attacks 
            it makes do double damage. The reverse of the spell, diminish animal, reduces the target animal to half its normal size, along with a corresponding 
            reduction in hit points and damage output.
        """,
    },
    "Animate Dead": {
        "level": 3,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "9 segments (54 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "permanent",
        "area_of_effect": "1 corpse or set of bones",
        "saving_throw": "none",
        "description": """
            Animate Dead allows the caster to turn the bones or body of a dead creature into a skeleton or zombie that will follow the caster’s orders. 
            The animated dead is under the complete control of the caster, but it has no mind or will of its own. The number of undead creatures that can be 
            animated depends on the level of the caster: 1 skeleton or zombie per level. The undead remain animated until they are destroyed. 
            This spell is often considered an evil act, and good-aligned clerics may avoid using it. 
        """,
    },
    "Armor": {
        "level": 1,
        "class": ["mage", "illusionist"],
        "school": "conjuration/summoning",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "cloth woven with spider silk"],
        "range": "touch",
        "duration": "1 hour/level",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Armor creates a magical field of force that serves as armor for the target creature. It gives the target the same armor class as chain mail, 
            or improves the creature’s current armor class by 1, whichever is better. The spell will absorb the first 8 points of damage before it dissipates. 
            If cast on a creature already wearing armor, it has no effect. The cloth woven with spider silk is consumed in the casting.
        """,
    },
    "Augury": {
        "level": 2,
        "class": ["cleric"],
        "school": "divination",
        "casting_time": "2 rounds",
        "components": ["incantation", "gestures", "holy symbol", "gem worth 100 g.p."],
        "range": "caster",
        "duration": "instantaneous",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Augury allows the caster to receive a brief glimpse into the future, revealing whether a particular action will bring good or bad results. 
            The spell does not provide detailed information, only a general sense of success (weal), failure (woe), or a mix of both (weal and woe). 
            The caster can attempt to foresee events up to 30 minutes into the future. The gem is consumed in the casting.
        """,
    },
    "Banishment": {
        "level": 7,
        "class": ["cleric"],
        "school": "abjuration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol", "holy water", "items inimical to the target"],
        "range": "10 yards",
        "duration": "permanent",
        "area_of_effect": "1 or more creatures in a 10’ cube/level",
        "saving_throw": "special",
        "description": """
            Banishment allows the caster to send one or more extraplanar creatures back to their home plane. The base chance of success is 50%, 
            adjusted by 1% for each level or hit die difference between the caster and the target(s). The spell requires the caster’s holy symbol, 
            holy water, and substances that are inimical to the target creature(s). If successful, the target creature(s) are immediately banished 
            and cannot return for at least one year.
        """,
    },
    # Additional spells will follow in a similar format.
})

spells.update({
    "Beacon": {
        "level": 4,
        "class": ["cleric"],
        "school": "alteration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol", "rare incense"],
        "range": "120 yards",
        "duration": "1 hour/level",
        "area_of_effect": "10’ radius/level",
        "saving_throw": "none",
        "description": """
            Beacon creates an area of bright light that can be seen for miles, allowing allies to find the caster’s location easily. 
            The light is visible even through thick fog or other obscuring conditions, although it does not penetrate solid objects. 
            The light has a 10’ radius per level of the caster, and it lasts for 1 hour per level. The rare incense is consumed in the casting.
        """,
    },
    "Bless": {
        "level": 1,
        "class": ["cleric"],
        "school": "conjuration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "60 yards",
        "duration": "6 rounds",
        "area_of_effect": "50’ radius",
        "saving_throw": "none",
        "description": """
            Bless grants all allies within a 50’ radius a +1 bonus to attack rolls and saving throws against fear effects. 
            This spell must be cast before combat begins, and it has no effect on creatures that are already engaged in melee. 
            The effects of bless cannot be combined with the spell chant.
        """,
    },
    "Blindness": {
        "level": 2,
        "class": ["cleric", "mage", "illusionist"],
        "school": "alteration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol (if cleric)"],
        "range": "30 yards",
        "duration": "permanent",
        "area_of_effect": "1 creature",
        "saving_throw": "negates",
        "description": """
            Blindness causes the target creature to lose its sight permanently. The target is allowed a saving throw to negate the effect. 
            The blindness can only be removed by a spell such as remove curse, dispel magic, or similar means. 
            If cast by a cleric, the caster’s holy symbol is required.
        """,
    },
    "Blur": {
        "level": 2,
        "class": ["illusionist"],
        "school": "illusion/phantasm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "3 rounds + 1 round/level",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Blur causes the caster’s form to become blurred, shifting and wavering. This distortion makes it harder for enemies to target the caster, 
            imposing a -4 penalty on attack rolls against the caster. The effect lasts for 3 rounds plus 1 round per caster level.
        """,
    },
    "Call Lightning": {
        "level": 3,
        "class": ["druid"],
        "school": "evocation",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "360 yards",
        "duration": "1 turn/level",
        "area_of_effect": "5’ radius around target point",
        "saving_throw": "none",
        "description": """
            Call Lightning allows the druid to summon a bolt of lightning from the sky to strike a target within range. The lightning bolt deals 2d8 points 
            of damage per caster level, up to a maximum of 10d8. The spell can only be cast outdoors and is dependent on stormy weather for maximum effect.
        """,
    },
    "Calm Animals": {
        "level": 1,
        "class": ["druid"],
        "school": "enchantment/charm",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "40 yards",
        "duration": "1 round/level",
        "area_of_effect": "30’ radius",
        "saving_throw": "negates",
        "description": """
            Calm Animals soothes and pacifies up to 2d4 hit dice of animals within a 30’ radius. The animals must make a saving throw or stop any hostile actions 
            and remain calm for the duration of the spell. The spell does not affect magical or intelligent creatures.
        """,
    },
    "Cause Fear": {
        "level": 1,
        "class": ["cleric", "illusionist"],
        "school": "necromancy",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "holy symbol (if cleric)"],
        "range": "30 yards",
        "duration": "1 round/level",
        "area_of_effect": "1 creature",
        "saving_throw": "negates",
        "description": """
            Cause Fear makes a single creature of less than 6 hit dice flee in panic for the duration of the spell. The creature is allowed a saving throw 
            to resist the effect. The spell has no effect on undead or constructs.
        """,
    },
    "Chain Lightning": {
        "level": 6,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures"],
        "range": "40 yards + 10 yards/level",
        "duration": "instantaneous",
        "area_of_effect": "one creature, then jumps to others within range",
        "saving_throw": "half",
        "description": """
            Chain Lightning creates a bolt of lightning that leaps from the primary target to other targets within range. The first target takes full damage, 
            while each subsequent target takes damage reduced by 1d6 per jump. Each target is allowed a saving throw for half damage. 
            The bolt can strike up to 1 target per caster level.
        """,
    },
    "Charm Animal": {
        "level": 2,
        "class": ["druid"],
        "school": "enchantment/charm",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "20 yards",
        "duration": "special",
        "area_of_effect": "1 animal",
        "saving_throw": "negates",
        "description": """
            Charm Animal allows the caster to enchant one animal, making it regard the caster as a trusted friend and ally. The animal gets a saving throw 
            to resist the charm. The spell lasts until dispelled or until the caster or his allies do something harmful to the charmed animal.
        """,
    },
    "Charm Person": {
        "level": 1,
        "class": ["mage", "illusionist"],
        "school": "enchantment/charm",
        "casting_time": "1 round",
        "components": ["incantation", "gestures"],
        "range": "10 yards",
        "duration": "special",
        "area_of_effect": "1 person",
        "saving_throw": "negates",
        "description": """
            Charm Person enchants one humanoid of 4 hit dice or fewer, causing it to regard the caster as a trusted friend and ally. 
            The target is allowed a saving throw to resist the charm. The spell lasts until dispelled or until the caster or his allies 
            do something harmful to the charmed person.
        """,
    },
    # Additional spells will follow in a similar format.
})

spells.update({
    "Clairaudience": {
        "level": 3,
        "class": ["mage", "illusionist"],
        "school": "divination",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "a small horn"],
        "range": "60 yards/level",
        "duration": "1 round/level",
        "area_of_effect": "one location",
        "saving_throw": "none",
        "description": """
            Clairaudience allows the caster to hear as if they were at a different location within the spell's range. The location must be familiar or known 
            to the caster. The spell does not allow the caster to see, only hear, and it can penetrate solid barriers, provided they are not too thick or 
            magically shielded.
        """,
    },
    "Clairvoyance": {
        "level": 3,
        "class": ["mage", "illusionist"],
        "school": "divination",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "a small mirror"],
        "range": "60 yards/level",
        "duration": "1 round/level",
        "area_of_effect": "one location",
        "saving_throw": "none",
        "description": """
            Clairvoyance allows the caster to see as if they were at a different location within the spell's range. The location must be familiar or known 
            to the caster. The spell does not allow the caster to hear, only see, and it can penetrate solid barriers, provided they are not too thick 
            or magically shielded.
        """,
    },
    "Cloudkill": {
        "level": 5,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards",
        "duration": "1 round/level",
        "area_of_effect": "20’ cube",
        "saving_throw": "none",
        "description": """
            Cloudkill creates a moving, poisonous cloud of gas that kills creatures with 3 or fewer hit dice, without a saving throw. 
            Creatures with 4 or more hit dice take 1d4 points of damage per round they remain within the cloud. The cloud moves away 
            from the caster at a rate of 10 feet per round and is heavier than air, sinking to the lowest level of the terrain.
        """,
    },
    "Color Spray": {
        "level": 1,
        "class": ["illusionist"],
        "school": "illusion/phantasm",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a pinch of powder or sand colored red, yellow, and blue"],
        "range": "0",
        "duration": "instantaneous",
        "area_of_effect": "5’ wide, 20’ long, and 10’ high arc",
        "saving_throw": "none",
        "description": """
            Color Spray causes a vivid array of clashing colors to spring forth from the caster's hand, affecting creatures within the area of effect. 
            Up to 6 hit dice of creatures can be affected. Creatures with 2 or fewer hit dice are knocked unconscious for 2d4 rounds, 
            those with 3 or 4 hit dice are blinded for 1d4 rounds, and creatures with more than 4 hit dice are stunned for 1 round. 
            The spell affects creatures from the lowest hit dice first.
        """,
    },
    "Command": {
        "level": 1,
        "class": ["cleric"],
        "school": "enchantment/charm",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "holy symbol"],
        "range": "30 yards",
        "duration": "1 round",
        "area_of_effect": "1 creature",
        "saving_throw": "negates",
        "description": """
            Command allows the caster to give a one-word command to a creature within range. If the creature fails its saving throw, 
            it must obey the command to the best of its ability. The command must be simple and straightforward, such as "flee," "halt," 
            or "sleep." The spell only affects creatures with intelligence of 13 or lower.
        """,
    },
    "Commune": {
        "level": 5,
        "class": ["cleric"],
        "school": "divination",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "holy symbol", "rare incense"],
        "range": "caster",
        "duration": "special",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Commune allows the cleric to contact their deity or a powerful entity associated with their deity to ask up to three yes-or-no questions. 
            The answers are usually brief, and the caster must wait one week before casting this spell again. The incense is consumed in the casting.
        """,
    },
    "Comprehend Languages": {
        "level": 1,
        "class": ["cleric", "mage"],
        "school": "divination",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "a pinch of soot and salt"],
        "range": "0",
        "duration": "5 rounds/level",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Comprehend Languages allows the caster to understand the meaning of any spoken language they hear. 
            The spell does not enable the caster to speak the language, only to comprehend its meaning. 
            The spell lasts for 5 rounds per caster level.
        """,
    },
    "Confusion": {
        "level": 4,
        "class": ["mage", "illusionist", "druid"],
        "school": "enchantment/charm",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a set of three nut shells"],
        "range": "120 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "40’ cube",
        "saving_throw": "negates",
        "description": """
            Confusion causes all creatures within the area of effect to become confused, making them unable to determine friend from foe. 
            Affected creatures will either wander aimlessly, attack the nearest creature, or stand still. The spell lasts for 2 rounds plus 
            1 round per caster level. A saving throw negates the effect.
        """,
    },
    "Conjure Animals": {
        "level": 6,
        "class": ["druid"],
        "school": "conjuration/summoning",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "30’ radius",
        "saving_throw": "none",
        "description": """
            Conjure Animals summons 1d4 animals that appear within the area of effect. The animals obey the caster's commands and 
            remain for 2 rounds per caster level or until slain. The types of animals summoned are determined by the GM and can include 
            any normal or giant animals appropriate to the caster’s environment.
        """,
    },
    "Conjure Elemental": {
        "level": 5,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "a piece of the element to be conjured"],
        "range": "60 yards",
        "duration": "1 turn/level",
        "area_of_effect": "1 elemental",
        "saving_throw": "none",
        "description": """
            Conjure Elemental summons a powerful elemental of air, earth, fire, or water, depending on the material component used. 
            The elemental will obey the caster's commands but may turn against the caster if concentration is broken. 
            The elemental remains for 1 turn per caster level or until destroyed.
        """,
    },
    "Contact Other Plane": {
        "level": 5,
        "class": ["mage"],
        "school": "divination",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "rare incense"],
        "range": "caster",
        "duration": "special",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Contact Other Plane allows the caster to send their mind to another plane of existence to ask questions. 
            The number of questions that can be asked depends on the caster's level, and the answers are often cryptic. 
            The process is mentally taxing, and the caster may suffer temporary insanity if the contacted entity is hostile or too powerful.
        """,
    },
    "Continual Light": {
        "level": 3,
        "class": ["cleric", "mage"],
        "school": "alteration",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "permanent",
        "area_of_effect": "60’ radius",
        "saving_throw": "negates",
        "description": """
            Continual Light creates a permanent, bright light that illuminates a 60’ radius. The light can be cast on an object, 
            causing it to emit light, or in an area. If cast on an unwilling creature or an item it carries, a saving throw is allowed to negate the effect. 
            Continual Light can be dispelled by a darkness spell of equal or higher level.
        """,
    },
    "Control Weather": {
        "level": 7,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "4 miles",
        "duration": "4d12 hours",
        "area_of_effect": "4d12 square miles",
        "saving_throw": "none",
        "description": """
            Control Weather allows the caster to change the weather within a 4-mile radius, with a duration of 4d12 hours. 
            The caster can summon storms, clear skies, or even cause snow in the summer, but the changes are gradual and take 
            about 10-30 minutes to manifest fully. The spell cannot create supernatural effects such as hurricanes or tornadoes.
        """,
    },
    "Control Winds": {
        "level": 5,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "40 yards/level",
        "duration": "1 turn/level",
        "area_of_effect": "40-yard radius/level",
        "saving_throw": "none",
        "description": """
            Control Winds allows the caster to alter the speed and direction of the wind within the spell's area of effect. 
            The caster can calm winds, create a breeze, or even generate powerful gusts that can knock down trees and capsize ships. 
            The effects last for 1 turn per caster level.
        """,
    },
    "Create Water": {
        "level": 1,
        "class": ["cleric"],
        "school": "alteration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "permanent",
        "area_of_effect": "up to 27 cubic feet",
        "saving_throw": "none",
        "description": """
            Create Water allows the caster to generate up to 27 cubic feet of water (approximately 200 gallons) at a location within range. 
            The water is clean and drinkable. The spell is often used in desert environments or to create water for a group of travelers.
        """,
    },
    # Continue with the rest of the spells...
})

spells.update({
    "Creeping Doom": {
        "level": 7,
        "class": ["druid"],
        "school": "conjuration/summoning",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "0",
        "duration": "4 rounds + 1 round/level",
        "area_of_effect": "60’ radius",
        "saving_throw": "none",
        "description": """
            Creeping Doom summons a swarm of small, venomous creatures (insects, spiders, etc.) that attack all creatures within the area of effect. 
            The swarm covers an area of 60 feet in radius and can move 10 feet per round at the caster's command. 
            The swarm inflicts 1d6 points of damage per round to all within its area and remains for 4 rounds plus 1 round per caster level.
        """,
    },
    "Cure Blindness": {
        "level": 3,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "permanent",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Cure Blindness removes blindness, whether caused by disease, injury, or magic, from a single creature. 
            The effect is instantaneous and permanent, restoring full vision to the affected creature.
        """,
    },
    "Cure Disease": {
        "level": 3,
        "class": ["cleric", "druid"],
        "school": "necromancy",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Cure Disease cures any form of natural disease affecting the touched creature. The spell can also cure parasitic infestations 
            and similar conditions but cannot restore lost hit points or cure magical diseases unless specified otherwise.
        """,
    },
    "Cure Light Wounds": {
        "level": 1,
        "class": ["cleric", "druid"],
        "school": "necromancy",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Cure Light Wounds heals 1d8 hit points of damage to the touched creature. The spell cannot restore hit points beyond 
            the creature's normal maximum. The healing is immediate and can be used to stabilize a dying character.
        """,
    },
    "Cure Serious Wounds": {
        "level": 4,
        "class": ["cleric", "druid"],
        "school": "necromancy",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Cure Serious Wounds heals 2d8+1 hit points of damage to the touched creature. 
            Like Cure Light Wounds, this spell cannot restore hit points beyond the creature's normal maximum.
        """,
    },
    "Cure Critical Wounds": {
        "level": 5,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Cure Critical Wounds heals 3d8+3 hit points of damage to the touched creature. 
            The spell is more powerful than Cure Serious Wounds but still cannot restore hit points beyond the creature's normal maximum.
        """,
    },
    "Death Spell": {
        "level": 6,
        "class": ["mage"],
        "school": "necromancy",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "a crushed black pearl worth at least 1,000 g.p."],
        "range": "60 yards",
        "duration": "instantaneous",
        "area_of_effect": "40’ cube",
        "saving_throw": "none",
        "description": """
            Death Spell instantly kills 4d20 hit dice worth of creatures within the area of effect. 
            The spell does not affect creatures with more than 8 hit dice, and it automatically kills those with fewer hit dice without a saving throw.
        """,
    },
    "Delayed Blast Fireball": {
        "level": 7,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "a tiny ball of bat guano and sulfur"],
        "range": "100 yards + 10 yards/level",
        "duration": "special",
        "area_of_effect": "20’ radius",
        "saving_throw": "half",
        "description": """
            Delayed Blast Fireball creates a fireball that detonates after a delay set by the caster (up to 5 rounds). 
            The fireball inflicts 1d6 points of damage per caster level (up to a maximum of 10d6). 
            Creatures caught in the area of effect can make a saving throw for half damage.
        """,
    },
    "Detect Evil": {
        "level": 1,
        "class": ["cleric", "druid"],
        "school": "divination",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "120 yards",
        "duration": "1 turn + 5 rounds/level",
        "area_of_effect": "60’ path, 10’ wide",
        "saving_throw": "none",
        "description": """
            Detect Evil allows the caster to sense the presence of evil creatures, objects, or magic within the area of effect. 
            The spell detects evil as an aura, and the caster can concentrate to focus on a particular area. 
            The spell lasts for 1 turn plus 5 rounds per caster level.
        """,
    },
    "Detect Invisibility": {
        "level": 2,
        "class": ["mage"],
        "school": "divination",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards/level",
        "duration": "5 rounds/level",
        "area_of_effect": "10’ path, 10’ wide",
        "saving_throw": "none",
        "description": """
            Detect Invisibility allows the caster to see invisible creatures and objects within the area of effect. 
            The spell lasts for 5 rounds per caster level and does not reveal illusions unless they are invisible.
        """,
    },
    "Detect Magic": {
        "level": 1,
        "class": ["cleric", "mage", "illusionist"],
        "school": "divination",
        "casting_time": "1 round",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "10’ path, 10’ wide",
        "saving_throw": "none",
        "description": """
            Detect Magic allows the caster to sense magical auras within the area of effect. 
            The spell detects magic on creatures, objects, and areas, revealing the presence and intensity of magic. 
            The spell lasts for 2 rounds per caster level.
        """,
    },
    "Detect Snares & Pits": {
        "level": 1,
        "class": ["druid"],
        "school": "divination",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a small piece of iron"],
        "range": "60 yards",
        "duration": "3 turns",
        "area_of_effect": "10’ path, 10’ wide",
        "saving_throw": "none",
        "description": """
            Detect Snares & Pits allows the caster to detect natural or man-made traps such as snares, pits, and deadfalls within the area of effect. 
            The spell does not reveal magical traps. The spell lasts for 3 turns.
        """,
    },
    "Dimension Door": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a small silver key"],
        "range": "360 yards",
        "duration": "instantaneous",
        "area_of_effect": "caster only",
        "saving_throw": "none",
        "description": """
            Dimension Door instantly transports the caster up to 360 yards to any location they can visualize or describe. 
            The caster can bring up to 500 pounds of equipment or objects with them, but cannot transport other creatures. 
            The spell is instantaneous and does not allow a saving throw.
        """,
    },
    "Dispel Evil": {
        "level": 5,
        "class": ["cleric"],
        "school": "abjuration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "1 round/level",
        "area_of_effect": "1 creature or object",
        "saving_throw": "special",
        "description": """
            Dispel Evil allows the caster to drive away or destroy evil creatures or spirits within the area of effect. 
            The spell has a special effect against summoned or magically created evil creatures, forcing them back to their home plane. 
            A successful saving throw allows the creature to resist the effects.
        """,
    },
    # Continue with the rest of the spells...
})

spells.update({
    "Dispel Magic": {
        "level": 3,
        "class": ["cleric", "mage", "illusionist"],
        "school": "abjuration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "120 yards",
        "duration": "instantaneous",
        "area_of_effect": "30’ cube",
        "saving_throw": "none",
        "description": """
            Dispel Magic removes ongoing magical effects within the area of effect. 
            The spell has a base 50% chance of success, modified by the difference in levels between the caster and the creator of the magical effect. 
            The spell can affect multiple spells within the area but does not dispel curses or instantaneous effects.
        """,
    },
    "Divination": {
        "level": 4,
        "class": ["cleric"],
        "school": "divination",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol", "sacrificial offering worth 25 g.p."],
        "range": "0",
        "duration": "instantaneous",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Divination allows the caster to receive a useful piece of information concerning a specific goal, event, or activity 
            that will occur within one week. The spell is accurate 70% + 1% per caster level. The information received is 
            cryptic and not always direct, depending on the wisdom of the deity contacted.
        """,
    },
    "Drawmij’s Instant Summons": {
        "level": 7,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a gem worth 1,000 g.p."],
        "range": "infinite (same plane)",
        "duration": "instantaneous",
        "area_of_effect": "1 object",
        "saving_throw": "none",
        "description": """
            Drawmij’s Instant Summons allows the caster to instantly summon a specific item that has been previously 
            enchanted with the spell. The item appears in the caster’s hand, regardless of its location, as long as it is on the same plane of existence.
        """,
    },
    "Dream": {
        "level": 5,
        "class": ["mage", "illusionist"],
        "school": "illusion/phantasm",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures"],
        "range": "special",
        "duration": "special",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Dream allows the caster to send a message to another creature in the form of a dream. 
            The message can be up to 10 minutes long and must be understandable by the recipient. 
            The recipient must be asleep, and the caster can dictate the nature of the dream, which can affect the recipient's thoughts and actions upon waking.
        """,
    },
    "Emotion": {
        "level": 4,
        "class": ["illusionist"],
        "school": "enchantment/charm",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "1 round/level",
        "area_of_effect": "20’ cube",
        "saving_throw": "none",
        "description": """
            Emotion allows the caster to induce a strong emotion in all creatures within the area of effect. 
            The caster can choose from fear, hatred, hopelessness, or rage. Each emotion has a specific effect on those affected, such as 
            fear causing them to flee, or rage granting a bonus to attack rolls but forcing them to fight recklessly.
        """,
    },
    "Enchanted Weapon": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "1 round/level",
        "area_of_effect": "1 weapon",
        "saving_throw": "none",
        "description": """
            Enchanted Weapon temporarily enchants a normal weapon, allowing it to hit creatures that require magical weapons to be harmed. 
            The weapon gains a +1 bonus to attack and damage rolls and lasts for the duration of the spell.
        """,
    },
    "Endure Cold/Endure Heat": {
        "level": 1,
        "class": ["cleric", "druid"],
        "school": "abjuration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "1 turn/level",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Endure Cold/Endure Heat protects the touched creature from extreme temperatures. 
            The spell halves all damage from cold or heat-based attacks, and the creature can withstand temperatures 
            from -50°F to 140°F without ill effects. The spell lasts for 1 turn per caster level.
        """,
    },
    "Erase": {
        "level": 1,
        "class": ["mage", "illusionist"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "instantaneous",
        "area_of_effect": "1 scroll or 2 pages",
        "saving_throw": "special",
        "description": """
            Erase removes writing from scrolls, books, or similar surfaces. The spell can erase magical writings as well, 
            but the caster must succeed on a caster level check (1d20 + caster level) against a DC equal to 11 + the spell level 
            of the magical writing. The spell erases up to 2 pages or 1 scroll.
        """,
    },
    "ESP": {
        "level": 2,
        "class": ["mage", "illusionist"],
        "school": "divination",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a copper piece"],
        "range": "60 yards",
        "duration": "5 rounds/level",
        "area_of_effect": "10’ path, 2’ wide",
        "saving_throw": "none",
        "description": """
            ESP allows the caster to read the surface thoughts of creatures within the area of effect. 
            The caster can focus on a specific creature each round, learning its thoughts at that moment. 
            The spell does not reveal memories, intentions, or deep secrets, only what the creature is currently thinking.
        """,
    },
    "Explosive Runes": {
        "level": 3,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "permanent until triggered",
        "area_of_effect": "written object",
        "saving_throw": "1/2 damage",
        "description": """
            Explosive Runes creates magical runes that explode when read, inflicting 6d4+6 points of damage to the reader 
            and anyone within 10 feet. A successful saving throw halves the damage. The runes remain dormant until triggered or dispelled.
        """,
    },
    "Feign Death": {
        "level": 3,
        "class": ["cleric", "illusionist"],
        "school": "necromancy",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "1 turn + 1 round/level",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Feign Death allows the caster or a willing creature to appear dead to all forms of detection. 
            The affected creature falls into a cataleptic state, with no discernible heartbeat, breath, or movement. 
            The creature is immune to poison and paralysis during this state, but is also helpless and cannot take any actions until the spell ends.
        """,
    },
    "Find Familiar": {
        "level": 1,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 day",
        "components": ["incantation", "gestures", "100 g.p. worth of incense and materials"],
        "range": "1 mile/level",
        "duration": "permanent until dispelled or familiar's death",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Find Familiar summons a magical creature to serve as the caster's familiar. 
            The creature will be a small animal with special abilities, depending on the environment and the caster's alignment. 
            The familiar shares a telepathic bond with the caster and grants various benefits, but if it dies, the caster suffers a significant penalty.
        """,
    },
    # Continue with additional spells...
})
spells.update({
    "Fireball": {
        "level": 3,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures", "bat guano and sulfur"],
        "range": "240 yards",
        "duration": "instantaneous",
        "area_of_effect": "20’ radius",
        "saving_throw": "1/2 damage",
        "description": """
            Fireball creates a burst of fire that detonates with a low roar, dealing 1d6 points of fire damage per caster level 
            (maximum 10d6) to all creatures within the area of effect. A successful saving throw halves the damage. 
            The fireball fills the area to its maximum extent, conforming to the shape of the area.
        """,
    },
    "Fire Trap": {
        "level": 4,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "brimstone and iron filings"],
        "range": "touch",
        "duration": "permanent until discharged",
        "area_of_effect": "object touched",
        "saving_throw": "1/2 damage",
        "description": """
            Fire Trap allows the caster to place a magical trap on an object. 
            When the object is opened, it bursts into flame, dealing 1d4 points of fire damage per caster level (maximum 20d4) 
            to the creature that triggered it. A successful saving throw halves the damage. The trap is undetectable except by magical means.
        """,
    },
    "Flame Arrow": {
        "level": 3,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a pinch of sulfur"],
        "range": "touch",
        "duration": "1 round/level",
        "area_of_effect": "1 arrow/level",
        "saving_throw": "none",
        "description": """
            Flame Arrow causes up to one arrow per caster level to become magical, bursting into flame when fired. 
            Each arrow deals an additional 1d6 points of fire damage to any target it hits. 
            The arrows must be fired before the spell's duration expires, or the magic is lost.
        """,
    },
    "Flame Strike": {
        "level": 5,
        "class": ["cleric"],
        "school": "evocation",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "60 yards",
        "duration": "instantaneous",
        "area_of_effect": "10’ radius, 30’ high cylinder",
        "saving_throw": "1/2 damage",
        "description": """
            Flame Strike calls down a column of divine fire that deals 6d8 points of damage to all creatures within the area of effect. 
            Half the damage is fire damage, and the other half is divine energy that is not subject to fire resistance or immunity. 
            A successful saving throw halves the damage.
        """,
    },
    "Fly": {
        "level": 3,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures", "a feather or wing"],
        "range": "touch",
        "duration": "1 turn/level + 1d6 turns",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Fly grants the touched creature the ability to fly at a speed of 60 feet per round (40 feet if heavily encumbered). 
            The spell lasts for 1 turn per caster level, plus an additional 1d6 turns. 
            The caster has control over the speed and altitude but cannot exceed the spell's time limit.
        """,
    },
    "Fog Cloud": {
        "level": 2,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a bit of wool or a dab of smoke"],
        "range": "10 yards/level",
        "duration": "4 rounds + 1 round/level",
        "area_of_effect": "20’ cube/level",
        "saving_throw": "none",
        "description": """
            Fog Cloud creates a bank of fog that obscures vision, making it impossible to see through or into the area. 
            The fog lasts for 4 rounds plus 1 round per caster level, or until dispersed by wind or magical means. 
            The spell is often used to provide cover or create confusion during combat.
        """,
    },
    "Forget": {
        "level": 2,
        "class": ["illusionist"],
        "school": "enchantment/charm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "permanent",
        "area_of_effect": "1-4 creatures",
        "saving_throw": "negates",
        "description": """
            Forget causes the affected creatures to forget up to 10 minutes of events. 
            The spell affects 1 creature at 2nd level, 2 at 4th level, 3 at 6th level, and 4 at 8th level. 
            A successful saving throw negates the effect. The memory loss is permanent, although powerful magic might restore the lost memories.
        """,
    },
    "Free Action": {
        "level": 4,
        "class": ["cleric"],
        "school": "abjuration",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "1 turn/level",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Free Action allows the touched creature to move and act normally, even under the influence of paralysis, 
            slow effects, or any other effect that would impede movement. 
            The spell lasts for 1 turn per caster level and can be used to counteract effects like hold person or web.
        """,
    },
    "Gate": {
        "level": 9,
        "class": ["cleric"],
        "school": "conjuration/summoning",
        "casting_time": "9 segments (54 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "instantaneous",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Gate opens a portal to another plane of existence, allowing the caster to call forth a powerful being, usually a deity or demon. 
            The summoned entity may be willing to assist the caster or might have its own agenda. 
            The spell is risky, as the summoned creature is not under the caster's control and could act unpredictably.
        """,
    },
    "Geas": {
        "level": 6,
        "class": ["cleric", "mage"],
        "school": ["enchantment/charm"],
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards",
        "duration": "until discharged",
        "area_of_effect": "1 creature",
        "saving_throw": "negates",
        "description": """
            Geas compels the affected creature to carry out a specific task or suffer penalties. 
            The task must be reasonable and can last until completed or a set duration. 
            A successful saving throw negates the effect. The spell can cause significant harm if the task is not completed.
        """,
    },
    "Globe of Invulnerability": {
        "level": 6,
        "class": ["mage"],
        "school": "abjuration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures"],
        "range": "10 yards",
        "duration": "1 round/level",
        "area_of_effect": "10’ radius sphere",
        "saving_throw": "none",
        "description": """
            Globe of Invulnerability creates an immobile, faintly shimmering sphere that surrounds the caster and excludes all 1st-3rd level spells 
            from entering. The globe moves with the caster and provides a safe zone from lower-level spells, but higher-level spells can still penetrate the globe.
        """,
    },
    "Guards and Wards": {
        "level": 6,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "a small amount of each material component required by the included spells"],
        "range": "caster's location",
        "duration": "2 hours/level",
        "area_of_effect": "400 square feet/level",
        "saving_throw": "none",
        "description": """
            Guards and Wards creates a series of magical effects that protect and obscure a large area, such as a castle or dungeon. 
            The spell includes the following effects: web, stinking cloud, a minor confusion effect, dancing lights, and a gust of wind. 
            The exact placement and configuration of these effects are up to the caster.
        """,
    },
    # Continue with additional spells...
})
spells.update({
    "Haste": {
        "level": 3,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures", "a shaving of licorice root"],
        "range": "60 yards",
        "duration": "3 rounds + 1 round/level",
        "area_of_effect": "1 creature/level",
        "saving_throw": "none",
        "description": """
            Haste grants extra speed to the affected creatures, doubling their movement and giving them an extra attack each round. 
            The spell lasts for 3 rounds plus 1 round per caster level. However, after the spell ends, the affected creatures are fatigued, suffering a -2 penalty to AC and attack rolls.
        """,
    },
    "Heal": {
        "level": 6,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Heal cures all damage, diseases, and most negative conditions, such as blindness, deafness, and paralysis, restoring the creature to full health. 
            It does not restore lost limbs or bring a creature back to life.
        """,
    },
    "Hold Monster": {
        "level": 5,
        "class": ["mage"],
        "school": "enchantment/charm",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "1-4 creatures",
        "saving_throw": "negates",
        "description": """
            Hold Monster paralyzes up to 4 creatures, preventing them from taking any actions. 
            The affected creatures can attempt a saving throw to negate the effect. The spell lasts for 2 rounds per caster level. 
            The creatures are aware of their surroundings but cannot move or speak.
        """,
    },
    "Hold Person": {
        "level": 2,
        "class": ["cleric", "mage"],
        "school": "enchantment/charm",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "60 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "1-4 persons",
        "saving_throw": "negates",
        "description": """
            Hold Person paralyzes up to 4 humanoid creatures, preventing them from taking any actions. 
            The affected creatures can attempt a saving throw to negate the effect. 
            The spell lasts for 2 rounds per caster level. The creatures are aware of their surroundings but cannot move or speak.
        """,
    },
    "Identify": {
        "level": 1,
        "class": ["mage"],
        "school": "divination",
        "casting_time": "1 hour",
        "components": ["incantation", "gestures", "a pearl worth at least 100 gp"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 item",
        "saving_throw": "none",
        "description": """
            Identify allows the caster to determine the magical properties of a single item. 
            The spell requires a pearl worth at least 100 gp, which is consumed in the process. 
            The caster has a 100% chance minus 5% per level of the item’s creator to successfully identify the item.
        """,
    },
    "Invisibility": {
        "level": 2,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "an eyelash encased in gum arabic"],
        "range": "touch",
        "duration": "special",
        "area_of_effect": "1 creature or object",
        "saving_throw": "none",
        "description": """
            Invisibility renders the affected creature or object unseen, even to infravision and ultravision. 
            The invisibility lasts until the subject attacks or until it is dispelled. The subject can perform other actions without breaking the invisibility.
        """,
    },
    "Invisibility 10' Radius": {
        "level": 3,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures", "an eyelash encased in gum arabic"],
        "range": "touch",
        "duration": "special",
        "area_of_effect": "10’ radius",
        "saving_throw": "none",
        "description": """
            Invisibility 10' Radius works like the Invisibility spell but affects all creatures within a 10-foot radius of the recipient. 
            The invisibility lasts until one of the subjects attacks or until it is dispelled. 
            The subjects can perform other actions without breaking the invisibility.
        """,
    },
    "Invisible Stalker": {
        "level": 6,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 hour",
        "components": ["incantation", "gestures"],
        "range": "10 yards",
        "duration": "until task is complete",
        "area_of_effect": "1 invisible stalker",
        "saving_throw": "none",
        "description": """
            Invisible Stalker summons an invisible stalker, an extraplanar creature, to serve the caster. 
            The stalker follows the caster’s commands to the best of its abilities, completing the task and then returning to its home plane.
        """,
    },
    "Knock": {
        "level": 2,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "instantaneous",
        "area_of_effect": "1 door, chest, or similar object",
        "saving_throw": "none",
        "description": """
            Knock opens stuck, barred, locked, or magically held doors, gates, or chests. 
            The spell does not bypass traps or protective spells, but it will open objects secured by mundane or magical means.
        """,
    },
    "Legend Lore": {
        "level": 6,
        "class": ["mage"],
        "school": "divination",
        "casting_time": "1 turn/level",
        "components": ["incantation", "gestures", "incense worth at least 250 gp"],
        "range": "caster",
        "duration": "special",
        "area_of_effect": "1 object or place",
        "saving_throw": "none",
        "description": """
            Legend Lore reveals the history, legends, and lore associated with a person, place, or object. 
            The spell takes 1 turn per caster level to cast and requires incense worth at least 250 gp. 
            The information gained depends on the time and conditions under which the spell is cast.
        """,
    },
    "Levitate": {
        "level": 2,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a small leather loop or a piece of golden wire bent into a cup shape"],
        "range": "60 yards",
        "duration": "1 turn/level",
        "area_of_effect": "1 creature or object",
        "saving_throw": "none",
        "description": """
            Levitate allows the caster to lift a creature or object into the air, moving it vertically up to 20 feet per round. 
            The spell lasts for 1 turn per caster level. The caster has no horizontal control unless the object can be pushed or pulled.
        """,
    },
    "Light": {
        "level": 1,
        "class": ["cleric", "mage"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a firefly or a piece of phosphorescent moss"],
        "range": "120 yards",
        "duration": "1 hour + 1 turn/level",
        "area_of_effect": "20’ radius",
        "saving_throw": "none",
        "description": """
            Light creates a bright light equivalent to a torch, illuminating an area with a 20-foot radius. 
            The light lasts for 1 hour plus 1 turn per caster level. It can be cast on an object or in an area, and it can be used to blind creatures temporarily if cast on their eyes.
        """,
    },
    "Lightning Bolt": {
        "level": 3,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures", "a bit of fur and a glass or crystal rod"],
        "range": "40 yards + 10 yards/level",
        "duration": "instantaneous",
        "area_of_effect": "5’ wide, 60’ long line",
        "saving_throw": "half",
        "description": """
            Lightning Bolt creates a powerful bolt of lightning that deals 1d6 points of damage per caster level (up to 10d6) to all creatures within its path. 
            The bolt can rebound off walls, potentially hitting the same targets multiple times. 
            Creatures can attempt a saving throw for half damage.
        """,
    },
    "Locate Object": {
        "level": 2,
        "class": ["cleric", "mage"],
        "school": "divination",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "a bit of fur from a bloodhound"],
        "range": "60 yards + 10 yards/level",
        "duration": "1 round/level",
        "area_of_effect": "centered on the caster",
        "saving_throw": "none",
        "description": """
            Locate Object allows the caster to sense the direction of a well-known or clearly visualized object. 
            The spell’s range is 60 yards plus 10 yards per caster level, and it lasts for 1 round per level. 
            The spell is blocked by lead or running water.
        """,
    },
    # Continue with additional spells...
})
spells.update({
    "Lower Water": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a small vial of dust or sand"],
        "range": "80 yards",
        "duration": "1 turn/level",
        "area_of_effect": "10’ x 10’/level area",
        "saving_throw": "none",
        "description": """
            Lower Water causes the water level in a designated area to drop by 50%, making it easier to cross. 
            The spell affects an area of 10’ x 10’ per caster level and lasts for 1 turn per level. 
            The effect is instantaneous and cannot be dispelled.
        """,
    },
    "Magic Jar": {
        "level": 5,
        "class": ["mage"],
        "school": "necromancy",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "a gem or crystal worth at least 100 gp"],
        "range": "10 yards/level",
        "duration": "special",
        "area_of_effect": "1 creature",
        "saving_throw": "special",
        "description": """
            Magic Jar allows the caster’s soul to leave their body and enter a prepared gem or crystal. 
            From there, the caster can attempt to possess another creature within range, forcing them to make a saving throw or be possessed. 
            The spell lasts until the caster’s soul returns to their body or the gem is destroyed.
        """,
    },
    "Magic Missile": {
        "level": 1,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "60 yards + 10 yards/level",
        "duration": "instantaneous",
        "area_of_effect": "1 or more creatures",
        "saving_throw": "none",
        "description": """
            Magic Missile creates a glowing arrow of magical energy that strikes its target unerringly, dealing 1d4+1 points of damage. 
            The caster gains an additional missile every two levels, up to a maximum of five missiles at 9th level.
        """,
    },
    "Mass Invisibility": {
        "level": 7,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "an eyelash encased in gum arabic"],
        "range": "10 yards/level",
        "duration": "special",
        "area_of_effect": "creatures within a 60’ diameter",
        "saving_throw": "none",
        "description": """
            Mass Invisibility functions like the Invisibility spell but affects all creatures within a 60-foot diameter area. 
            The spell lasts until one of the creatures attacks or until it is dispelled. 
            The creatures can perform other actions without breaking the invisibility.
        """,
    },
    "Maze": {
        "level": 8,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "5 yards/level",
        "duration": "special",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Maze banishes a creature to a labyrinthine demiplane from which it must escape. 
            The creature must attempt to find its way out, taking 2d4 rounds minus its intelligence modifier. 
            Once it escapes, it reappears in the spot it left or the nearest available space.
        """,
    },
    "Mirror Image": {
        "level": 2,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "2 rounds/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Mirror Image creates 2d4 illusory duplicates of the caster that move with them and mimic their actions. 
            The images last for 2 rounds per level or until destroyed. 
            Attacks directed at the caster will hit the images first, potentially destroying them.
        """,
    },
    "Monster Summoning I": {
        "level": 3,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning I conjures 1d6 first-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 30 yards.
        """,
    },
    "Monster Summoning II": {
        "level": 4,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "40 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning II conjures 1d6 second-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 40 yards.
        """,
    },
    "Monster Summoning III": {
        "level": 5,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures"],
        "range": "50 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning III conjures 1d6 third-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 50 yards.
        """,
    },
    "Monster Summoning IV": {
        "level": 6,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning IV conjures 1d6 fourth-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 60 yards.
        """,
    },
    "Monster Summoning V": {
        "level": 7,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures"],
        "range": "70 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning V conjures 1d6 fifth-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 70 yards.
        """,
    },
    "Monster Summoning VI": {
        "level": 8,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "8 segments (48 seconds)",
        "components": ["incantation", "gestures"],
        "range": "80 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning VI conjures 1d6 sixth-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 80 yards.
        """,
    },
    "Monster Summoning VII": {
        "level": 9,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "9 segments (54 seconds)",
        "components": ["incantation", "gestures"],
        "range": "90 yards",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Monster Summoning VII conjures 1d6 seventh-level monsters to fight for the caster. 
            The creatures remain for 2 rounds plus 1 round per caster level or until slain. 
            The caster can summon the creatures within 90 yards.
        """,
    },
    "Mordenkainen's Disjunction": {
        "level": 9,
        "class": ["mage"],
        "school": "abjuration",
        "casting_time": "9 segments (54 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "instantaneous",
        "area_of_effect": "30’ radius",
        "saving_throw": "special",
        "description": """
            Mordenkainen's Disjunction disenchants all magical effects and items within a 30-foot radius. 
            Each item must make a saving throw or be permanently disenchanted. 
            The spell can also destroy magical barriers such as prismatic walls, 
            but has a small chance of affecting artifacts and relics, potentially rendering them inert.
        """,
    },
    "Move Earth": {
        "level": 6,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "a small quantity of soil or rock"],
        "range": "10 yards/level",
        "duration": "permanent",
        "area_of_effect": "10 cubic yards/level",
        "saving_throw": "none",
        "description": """
            Move Earth reshapes the terrain, allowing the caster to move up to 10 cubic yards of soil or rock per level. 
            The changes are permanent, but the spell cannot affect structures or other solid objects. 
            The spell requires one turn of casting time and has no effect on creatures.
        """,
    },
    "Neutralize Poison": {
        "level": 4,
        "class": ["cleric", "druid"],
        "school": "necromancy",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "a small quantity of purified water"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "1 creature or object",
        "saving_throw": "none",
        "description": """
            Neutralize Poison detoxifies any sort of venom or poison in a creature or object, rendering it harmless. 
            The spell can neutralize poison in a living creature, which otherwise might result in death or debilitation. 
            It can also purify contaminated food or drink.
        """,
    },
    "Obscurement": {
        "level": 2,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a pinch of mistletoe"],
        "range": "0",
        "duration": "4 rounds/level",
        "area_of_effect": "10’ radius/level",
        "saving_throw": "none",
        "description": """
            Obscurement creates a thick cloud of mist that obscures vision in a 10-foot radius per level of the caster. 
            The mist lasts for 4 rounds per level and provides concealment for creatures within its area of effect.
        """,
    },
    # Continue with additional spells...
})
spells.update({
    "Otto's Irresistible Dance": {
        "level": 8,
        "class": ["mage"],
        "school": "enchantment/charm",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a small fiddle"],
        "range": "touch",
        "duration": "1d4+1 rounds",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Otto's Irresistible Dance forces the target to dance uncontrollably, making them unable to attack, cast spells, or do anything else. 
            The target is also easier to hit, suffering a -4 penalty to Armor Class and a -2 penalty on saving throws. 
            The spell lasts for 1d4+1 rounds, and there is no saving throw to avoid the effect.
        """,
    },
    "Passwall": {
        "level": 5,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures", "a pinch of sesame seeds"],
        "range": "30 yards",
        "duration": "3 turns",
        "area_of_effect": "10’ long, 5’ wide, 8’ high passage",
        "saving_throw": "none",
        "description": """
            Passwall creates a temporary passage through wooden, plaster, or stone walls up to 10 feet thick. 
            The passage is 10 feet long, 5 feet wide, and 8 feet high. 
            The passage remains open for 3 turns before the wall returns to its original state.
        """,
    },
    "Permanency": {
        "level": 8,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "2 rounds",
        "components": ["incantation", "gestures", "a pinch of diamond dust worth 5,000 gp"],
        "range": "touch",
        "duration": "permanent",
        "area_of_effect": "1 spell effect or item",
        "saving_throw": "none",
        "description": """
            Permanency makes certain spells or magical effects permanent. 
            The spell can be used on other spells such as Enlarge, Invisibility, or Wall of Force, but the caster must sacrifice 1 point of constitution permanently to cast this spell. 
            The spell can also be used to make other magical effects permanent.
        """,
    },
    "Phase Door": {
        "level": 7,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "a small cube of quartz"],
        "range": "caster",
        "duration": "1 usage per 2 levels",
        "area_of_effect": "special",
        "saving_throw": "none",
        "description": """
            Phase Door allows the caster to pass through solid material as if it were not there. 
            The caster can use the Phase Door once for every two levels they have, 
            and the door closes behind them after they pass through. 
            Only the caster can use the Phase Door, and it cannot be dispelled.
        """,
    },
    "Plant Growth": {
        "level": 3,
        "class": ["druid", "mage"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "a handful of seeds"],
        "range": "10 yards/level",
        "duration": "permanent",
        "area_of_effect": "100 square feet/level",
        "saving_throw": "none",
        "description": """
            Plant Growth causes normal vegetation within the area of effect to grow rapidly, thickening and becoming overgrown. 
            The vegetation can impede movement, providing cover and concealment. 
            The effect is permanent unless the vegetation is cleared or destroyed.
        """,
    },
    "Polymorph Any Object": {
        "level": 8,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 round",
        "components": ["incantation", "gestures", "a piece of the object to be changed"],
        "range": "5 yards/level",
        "duration": "permanent",
        "area_of_effect": "1 object or creature",
        "saving_throw": "none",
        "description": """
            Polymorph Any Object allows the caster to transform any object or creature into another object or creature. 
            The effect is permanent unless dispelled or reversed by the caster. 
            The spell can change the target’s form, material, and even properties.
        """,
    },
    "Polymorph Other": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a cocoon"],
        "range": "5 yards/level",
        "duration": "permanent",
        "area_of_effect": "1 creature",
        "saving_throw": "negates",
        "description": """
            Polymorph Other transforms the target creature into another type of creature. 
            The transformation is permanent unless dispelled. 
            The target retains its original hit points and saving throws, but gains the physical abilities of its new form.
        """,
    },
    "Polymorph Self": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "2 turns/level",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Polymorph Self allows the caster to change their form into that of any creature. 
            The caster gains the physical abilities of the chosen form but retains their original hit points and saving throws. 
            The spell lasts for 2 turns per caster level.
        """,
    },
    "Power Word Kill": {
        "level": 9,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "5 yards/level",
        "duration": "instantaneous",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Power Word Kill instantly slays any creature with 60 hit points or fewer. 
            The spell has no effect on creatures with more than 60 hit points. 
            The spell requires only a single word to cast and cannot be resisted.
        """,
    },
    "Power Word Stun": {
        "level": 7,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "5 yards/level",
        "duration": "special",
        "area_of_effect": "1 creature",
        "saving_throw": "none",
        "description": """
            Power Word Stun stuns a creature with 90 hit points or fewer, rendering it unable to act for 2d4 rounds. 
            The spell has no effect on creatures with more than 90 hit points. 
            The duration of the stun effect depends on the target’s hit points.
        """,
    },
    "Prismatic Sphere": {
        "level": 9,
        "class": ["mage"],
        "school": "abjuration",
        "casting_time": "9 segments (54 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "1 turn/level",
        "area_of_effect": "10’ radius sphere",
        "saving_throw": "see text",
        "description": """
            Prismatic Sphere creates a multi-layered protective sphere around the caster. 
            Each layer has a different color, offering various protections and effects. 
            Creatures attempting to pass through the sphere must make saving throws or suffer harmful effects, 
            with each color presenting a different challenge.
        """,
    },
    "Prismatic Spray": {
        "level": 7,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "instantaneous",
        "area_of_effect": "70’ long, 5’-20’ wide spray",
        "saving_throw": "see text",
        "description": """
            Prismatic Spray releases a series of multicolored beams, each with different effects, including fire, electricity, and petrification. 
            The spell’s effects are determined randomly, and each creature in the area must make saving throws or suffer the corresponding effect.
        """,
    },
    "Prismatic Wall": {
        "level": 8,
        "class": ["mage"],
        "school": "abjuration",
        "casting_time": "8 segments (48 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards",
        "duration": "1 turn/level",
        "area_of_effect": "20’ high, 40’ wide, 10’ deep wall",
        "saving_throw": "see text",
        "description": """
            Prismatic Wall creates a solid wall of multi-colored light, each color offering different protections and effects. 
            Creatures attempting to pass through the wall must make saving throws or suffer harmful effects, 
            with each color presenting a different challenge.
        """,
    },
    # Continue with additional spells...
})
spells.update({
    "Produce Flame": {
        "level": 2,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "a small piece of phosphorus"],
        "range": "caster",
        "duration": "2 rounds/level",
        "area_of_effect": "flame in caster’s hand",
        "saving_throw": "none",
        "description": """
            Produce Flame allows the caster to create a flame in their hand that sheds light as a torch. 
            The flame can be thrown as a missile weapon, inflicting 1d4+1 points of damage with a successful hit. 
            The flame lasts for 2 rounds per caster level or until it is thrown.
        """,
    },
    "Programmed Illusion": {
        "level": 6,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "1 turn",
        "components": ["incantation", "gestures", "a small piece of fleece"],
        "range": "10 yards/level",
        "duration": "special",
        "area_of_effect": "visual illusion within a 10’ cube + 10’/level",
        "saving_throw": "none",
        "description": """
            Programmed Illusion allows the caster to create a visual illusion that is triggered by a specific event or condition. 
            The illusion can include visual and audible elements and will behave according to the caster’s instructions. 
            The illusion lasts until triggered or dispelled.
        """,
    },
    "Project Image": {
        "level": 6,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "a small mirror"],
        "range": "10 yards/level",
        "duration": "1 round/level",
        "area_of_effect": "one image",
        "saving_throw": "none",
        "description": """
            Project Image creates a visual illusion of the caster that can move and act as if it were the caster. 
            The image can mimic the caster’s movements and cast spells, but the spells are only illusions with no actual effect. 
            The image lasts for 1 round per caster level.
        """,
    },
    "Protection from Evil": {
        "level": 1,
        "class": ["cleric", "mage"],
        "school": "abjuration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "holy water or powdered silver"],
        "range": "touch",
        "duration": "2 rounds/level",
        "area_of_effect": "creature touched",
        "saving_throw": "none",
        "description": """
            Protection from Evil creates a magical barrier around the target, granting a +2 bonus to Armor Class and saving throws against attacks by evil creatures. 
            The spell also prevents summoned or conjured creatures from making physical contact with the target. 
            The spell lasts for 2 rounds per caster level.
        """,
    },
    "Protection from Evil, 10' Radius": {
        "level": 4,
        "class": ["cleric", "mage"],
        "school": "abjuration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "holy water or powdered silver"],
        "range": "10’ radius around caster",
        "duration": "2 rounds/level",
        "area_of_effect": "10’ radius sphere",
        "saving_throw": "none",
        "description": """
            Protection from Evil, 10' Radius creates a protective barrier that extends in a 10-foot radius around the caster. 
            The spell grants a +2 bonus to Armor Class and saving throws against attacks by evil creatures for all within the radius. 
            It also prevents summoned or conjured creatures from making physical contact with those within the radius. 
            The spell lasts for 2 rounds per caster level.
        """,
    },
    "Protection from Normal Missiles": {
        "level": 3,
        "class": ["mage"],
        "school": "abjuration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures", "a piece of turtle shell"],
        "range": "caster",
        "duration": "1 turn/level",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Protection from Normal Missiles grants the caster immunity to small, non-magical missile weapons such as arrows, bolts, darts, etc. 
            The spell does not protect against large or magical missiles such as boulders or magical arrows. 
            The protection lasts for 1 turn per caster level.
        """,
    },
    "Purify Food and Drink": {
        "level": 1,
        "class": ["cleric", "druid"],
        "school": "alteration",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures"],
        "range": "30 feet",
        "duration": "instantaneous",
        "area_of_effect": "1 cubic foot/level",
        "saving_throw": "none",
        "description": """
            Purify Food and Drink removes any impurities, poison, disease, or other contaminants from food and water within the area of effect. 
            The spell renders the food and drink pure and safe to consume. 
            It can affect 1 cubic foot of food or drink per caster level.
        """,
    },
    "Pyrotechnics": {
        "level": 2,
        "class": ["mage", "druid"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a pinch of dust"],
        "range": "120 yards",
        "duration": "1d4+1 rounds",
        "area_of_effect": "fire source",
        "saving_throw": "negates",
        "description": """
            Pyrotechnics allows the caster to transform an existing fire source into either a dazzling display of fireworks or a choking cloud of smoke. 
            The fireworks blind all creatures within a 120-foot radius for 1d4+1 rounds, while the smoke cloud obscures vision in a 20-foot radius, 
            causing all within to suffer a -4 penalty to attack rolls. 
            The fire source is extinguished after the spell is cast.
        """,
    },
    "Raise Dead": {
        "level": 5,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "10 yards",
        "duration": "permanent",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Raise Dead allows the caster to restore life to a dead creature. 
            The spell requires the body to be relatively intact and must have been dead for no more than 1 day per caster level. 
            The creature returns to life with 1 hit point, and any lost limbs remain missing. 
            The creature is weak and helpless for 1 day per day it was dead.
        """,
    },
    "Ray of Enfeeblement": {
        "level": 2,
        "class": ["mage"],
        "school": "enchantment/charm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards/level",
        "duration": "1 round/level",
        "area_of_effect": "1 creature",
        "saving_throw": "negates",
        "description": """
            Ray of Enfeeblement reduces the target's Strength, making them weaker in combat. 
            The target suffers a penalty to attack rolls and damage equal to 25% of their Strength, rounded down. 
            The spell lasts for 1 round per caster level.
        """,
    },
    "Reincarnate": {
        "level": 5,
        "class": ["druid"],
        "school": "necromancy",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol", "rare herbs worth 1,000 gp"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Reincarnate allows the caster to bring a dead creature back to life in a new body. 
            The creature’s new form is determined randomly, and may not be the same race or species as the original. 
            The creature retains its original memories and abilities, but may gain new physical traits based on its new form.
        """,
    },
    "Remove Curse": {
        "level": 3,
        "class": ["cleric", "mage"],
        "school": "abjuration",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "one creature or object",
        "saving_throw": "none",
        "description": """
            Remove Curse lifts a curse from a creature or object. 
            The spell can remove any one curse, including those placed by powerful spells or cursed items. 
            The caster must touch the creature or object to be affected, and the curse is removed instantly.
        """,
    },
    "Resist Fire/Resist Cold": {
        "level": 2,
        "class": ["cleric", "druid"],
        "school": "abjuration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "1 turn/level",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Resist Fire/Resist Cold grants the target resistance to extreme temperatures. 
            The target receives a +3 bonus to saving throws against fire or cold-based attacks and takes only half damage from such attacks. 
            The spell lasts for 1 turn per caster level.
        """,
    },
    "Restoration": {
        "level": 7,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Restoration restores lost levels or drained abilities to the target. 
            The spell can restore one lost level or 1d4 points of an ability score drained by a creature or magical effect. 
            The caster must touch the creature to be affected, and the restoration is permanent.
        """,
    },
    "Resurrection": {
        "level": 7,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "permanent",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Resurrection restores life to a dead creature, even if the body is destroyed or missing. 
            The spell requires a portion of the creature's remains, or the caster must know the creature well. 
            The creature returns to life with full hit points, and any lost limbs or abilities are restored. 
            The creature is weak and helpless for 1 day per day it was dead.
        """,
    },
    "Reverse Gravity": {
        "level": 7,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards/level",
        "duration": "1/10 round (6 seconds)",
        "area_of_effect": "30’ square/level",
        "saving_throw": "none",
        "description": """
            Reverse Gravity temporarily reverses the gravitational pull in the area of effect, causing all creatures and objects to fall upwards. 
            The effect lasts for 1/10 of a round, after which gravity returns to normal and everything falls back down. 
            The spell can cause significant damage to those caught in the area of effect if they fall a great distance.
        """,
    },
    "Rope Trick": {
        "level": 2,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a small piece of rope"],
        "range": "touch",
        "duration": "2 turns/level",
        "area_of_effect": "one rope up to 30’ long",
        "saving_throw": "none",
        "description": """
            Rope Trick causes a rope to rise into the air and hang vertically, creating an invisible entrance to an extradimensional space. 
            The space can hold up to 8 creatures of medium size and provides a safe place to rest or hide. 
            The rope can be climbed, and once inside, creatures can pull the rope up to prevent others from following.
        """,
    },
    "Sanctuary": {
        "level": 1,
        "class": ["cleric"],
        "school": "abjuration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "caster",
        "duration": "2 rounds + 1 round/level",
        "area_of_effect": "caster",
        "saving_throw": "negates",
        "description": """
            Sanctuary surrounds the caster with an aura of protection, causing enemies to be unable to attack the caster directly. 
            Enemies must make a saving throw or be unable to target the caster with attacks or harmful spells. 
            The spell lasts for 2 rounds plus 1 round per caster level.
        """,
    },
    "Scare": {
        "level": 2,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a small piece of white cloth"],
        "range": "30 yards",
        "duration": "1d4 rounds + 1 round/level",
        "area_of_effect": "up to 4 creatures",
        "saving_throw": "negates",
        "description": """
            Scare fills the minds of creatures with fear, causing them to flee in terror. 
            Affected creatures must make a saving throw or flee for the duration of the spell. 
            The spell affects creatures with up to 6 hit dice or levels and lasts for 1d4 rounds plus 1 round per caster level.
        """,
    },
    # Continue with additional spells...
})
spells.update({
    "Secret Page": {
        "level": 3,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "powdered lead and zinc"],
        "range": "touch",
        "duration": "permanent",
        "area_of_effect": "one page",
        "saving_throw": "none",
        "description": """
            Secret Page allows the caster to magically hide the true contents of a page, replacing it with a false text of the caster’s choosing. 
            The hidden text can be revealed only by a dispel magic spell or by the caster speaking a command word. 
            The false text appears completely genuine to any reader until the hidden text is revealed.
        """,
    },
    "Seduction": {
        "level": 3,
        "class": ["bard"],
        "school": "enchantment/charm",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 feet",
        "duration": "1 turn/level",
        "area_of_effect": "one creature",
        "saving_throw": "negates",
        "description": """
            Seduction allows the caster to charm a single creature, causing it to become infatuated with the caster and more likely to comply with their requests. 
            The affected creature must make a saving throw or be charmed, following the caster’s instructions to the best of its ability. 
            The charm lasts for 1 turn per caster level.
        """,
    },
    "Seeming": {
        "level": 5,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures"],
        "range": "10 yards/level",
        "duration": "12 hours",
        "area_of_effect": "1 person/2 levels",
        "saving_throw": "none",
        "description": """
            Seeming allows the caster to change the appearance of multiple creatures, making them look like something else. 
            The illusions can alter the creatures’ clothing, armor, weapons, and even their physical appearance. 
            The spell lasts for 12 hours or until the caster dispels it.
        """,
    },
    "Sepia Snake Sigil": {
        "level": 3,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "6 segments (36 seconds)",
        "components": ["incantation", "gestures", "ink of sepia"],
        "range": "touch",
        "duration": "until triggered",
        "area_of_effect": "one sigil",
        "saving_throw": "special",
        "description": """
            Sepia Snake Sigil creates a magical trap on a page or surface, causing a sepia-colored serpent to spring forth and bind a creature that touches it. 
            The creature must make a saving throw or be trapped in a suspended state, unable to move or take any actions. 
            The serpent and the binding effect disappear after 1d4+1 days, releasing the creature.
        """,
    },
    "Shadow Door": {
        "level": 5,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 feet/level",
        "duration": "1 round/level",
        "area_of_effect": "one shadowy door",
        "saving_throw": "none",
        "description": """
            Shadow Door creates an illusory door that appears to lead into a shadowy, hidden passage. 
            The caster can step through the door, becoming invisible and undetectable to creatures outside the illusion. 
            The illusion lasts for 1 round per caster level, after which the caster becomes visible again.
        """,
    },
    "Shape Change": {
        "level": 9,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "9 segments (54 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "1 turn/level",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Shape Change allows the caster to transform into any creature or object, changing their appearance, abilities, and size. 
            The caster retains their own hit points and personality, but otherwise gains the abilities and physical characteristics of the new form. 
            The caster can change forms as often as they wish during the spell’s duration, which lasts for 1 turn per caster level.
        """,
    },
    "Shatter": {
        "level": 2,
        "class": ["cleric", "mage"],
        "school": "evocation",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "a small rock crystal"],
        "range": "30 yards",
        "duration": "instantaneous",
        "area_of_effect": "3’ radius sphere",
        "saving_throw": "negates",
        "description": """
            Shatter causes a sudden loud ringing noise that breaks brittle, non-magical objects in the area of effect. 
            The spell can also damage crystalline creatures, causing them to take 1d6 points of damage per caster level (maximum 10d6). 
            Creatures and magical objects in the area can make a saving throw to avoid the effect.
        """,
    },
    "Shield": {
        "level": 1,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "2 rounds/level",
        "area_of_effect": "caster",
        "saving_throw": "none",
        "description": """
            Shield creates an invisible barrier that grants the caster protection from physical and magical attacks. 
            The spell improves the caster’s Armor Class by +4 and grants immunity to magic missile spells. 
            The shield lasts for 2 rounds per caster level.
        """,
    },
    "Shield of Faith": {
        "level": 1,
        "class": ["cleric"],
        "school": "abjuration",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "1 turn/level",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Shield of Faith grants a creature a +2 bonus to Armor Class. 
            The spell’s effects last for 1 turn per caster level, providing protection from both physical and magical attacks.
        """,
    },
    "Shillelagh": {
        "level": 1,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a piece of holly"],
        "range": "touch",
        "duration": "1 round/level",
        "area_of_effect": "one non-magical club or quarterstaff",
        "saving_throw": "none",
        "description": """
            Shillelagh transforms a non-magical club or quarterstaff into a magical weapon with a +1 bonus to attack rolls and damage. 
            The weapon deals 1d6 points of damage and lasts for 1 round per caster level.
        """,
    },
    "Shocking Grasp": {
        "level": 1,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "caster’s hand",
        "saving_throw": "none",
        "description": """
            Shocking Grasp allows the caster to channel an electric charge through their hand, delivering a powerful shock to a creature they touch. 
            The spell inflicts 1d8 points of electrical damage plus 1 point per caster level (maximum +8).
        """,
    },
    "Silence, 15' Radius": {
        "level": 2,
        "class": ["cleric"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "120 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "15’ radius sphere",
        "saving_throw": "none",
        "description": """
            Silence, 15' Radius creates an area of magical silence within a 15-foot radius, centered on a point chosen by the caster. 
            No sound can be heard within the area of effect, preventing speech, spellcasting with verbal components, and any other sound-based actions. 
            The silence lasts for 2 rounds per caster level.
        """,
    },
    "Simulacrum": {
        "level": 7,
        "class": ["mage"],
        "school": "illusion/phantasm",
        "casting_time": "12 hours",
        "components": ["incantation", "gestures", "snow or ice", "hair or other part of the creature to be duplicated"],
        "range": "touch",
        "duration": "permanent",
        "area_of_effect": "one duplicate creature",
        "saving_throw": "none",
        "description": """
            Simulacrum creates a duplicate of a creature using snow or ice, with the creature’s physical form and abilities. 
            The duplicate has only half the hit points of the original and cannot gain experience points or levels. 
            The simulacrum is under the caster’s control and can act independently, but it cannot be healed by any means.
        """,
    },
    "Sleep": {
        "level": 1,
        "class": ["mage", "illusionist"],
        "school": "enchantment/charm",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a pinch of sand or rose petals"],
        "range": "30 yards",
        "duration": "5 rounds/level",
        "area_of_effect": "4d4 hit dice of creatures",
        "saving_throw": "none",
        "description": """
            Sleep causes a magical slumber to come upon creatures with a total of 4d4 hit dice or less. 
            Creatures with more than 4 hit dice are not affected. 
            The spell can target multiple creatures within a 30-yard range, and they will remain asleep for 5 rounds per caster level or until awakened.
        """,
    },
    # Continue adding more spells as needed...
})
spells.update({
    "Slow": {
        "level": 3,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "3 rounds + 1 round/level",
        "area_of_effect": "40-foot cube",
        "saving_throw": "negates",
        "description": """
            Slow reduces the movement rate and attack rate of affected creatures by 50%. 
            It affects up to 40 feet of creatures, and they must make a saving throw to avoid the effects. 
            The spell lasts for 3 rounds plus 1 round per caster level.
        """,
    },
    "Snare": {
        "level": 3,
        "class": ["druid"],
        "school": "enchantment/charm",
        "casting_time": "3 turns (30 minutes)",
        "components": ["incantation", "gestures", "a piece of vine or rope"],
        "range": "touch",
        "duration": "until triggered",
        "area_of_effect": "one snare",
        "saving_throw": "none",
        "description": """
            Snare sets a magical trap in the form of a vine or rope that will bind any creature that triggers it. 
            The snare is invisible and nearly impossible to detect. 
            When triggered, the snare binds the creature, holding it fast until released or the spell is dispelled.
        """,
    },
    "Solid Fog": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "2 rounds/level",
        "area_of_effect": "20-foot cube",
        "saving_throw": "none",
        "description": """
            Solid Fog creates a thick, cloying mist that slows movement and hampers visibility. 
            Creatures moving through the fog can only move at 10% of their normal speed, and ranged attacks are impossible. 
            The fog lasts for 2 rounds per caster level.
        """,
    },
    "Speak with Animals": {
        "level": 1,
        "class": ["cleric", "druid"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "2 rounds/level",
        "area_of_effect": "15-foot radius",
        "saving_throw": "none",
        "description": """
            Speak with Animals allows the caster to communicate with normal animals. 
            The caster can ask questions and receive answers, but the intelligence of the animals limits the responses. 
            The spell lasts for 2 rounds per caster level.
        """,
    },
    "Speak with Dead": {
        "level": 3,
        "class": ["cleric"],
        "school": "necromancy",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "10 yards",
        "duration": "1 round/level",
        "area_of_effect": "one corpse",
        "saving_throw": "none",
        "description": """
            Speak with Dead allows the caster to ask questions of a dead body. 
            The number of questions and the clarity of the answers depend on the caster's level and the time since death. 
            The spell lasts for 1 round per caster level.
        """,
    },
    "Speak with Plants": {
        "level": 4,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "1 turn/level",
        "area_of_effect": "15-foot radius",
        "saving_throw": "none",
        "description": """
            Speak with Plants allows the caster to communicate with normal plants and plant creatures. 
            The plants can reveal information about their surroundings or provide other useful information. 
            The spell lasts for 1 turn per caster level.
        """,
    },
    "Spider Climb": {
        "level": 1,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "a drop of bitumen and a live spider"],
        "range": "touch",
        "duration": "3 rounds + 1 round/level",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Spider Climb allows the affected creature to move on walls and ceilings as if they were a spider. 
            The creature gains a +7 bonus to climb walls and can move at its normal speed on vertical or horizontal surfaces. 
            The spell lasts for 3 rounds plus 1 round per caster level.
        """,
    },
    "Spike Growth": {
        "level": 3,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "1 hour/level",
        "area_of_effect": "20-foot square/level",
        "saving_throw": "none",
        "description": """
            Spike Growth causes the ground in the area of effect to become covered in sharp spikes. 
            Any creature moving through the area takes 1d4 points of damage per 10 feet of movement. 
            The spell lasts for 1 hour per caster level.
        """,
    },
    "Spike Stones": {
        "level": 5,
        "class": ["druid"],
        "school": "alteration",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "3 turns + 1 turn/level",
        "area_of_effect": "10-foot square/level",
        "saving_throw": "none",
        "description": """
            Spike Stones transforms the ground into sharp, jagged stones that injure creatures moving through the area. 
            Each 10 feet of movement causes 1d8 points of damage. 
            The spell lasts for 3 turns plus 1 turn per caster level.
        """,
    },
    "Spiritual Hammer": {
        "level": 2,
        "class": ["cleric"],
        "school": "evocation",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "30 yards",
        "duration": "3 rounds + 1 round/level",
        "area_of_effect": "one magical hammer",
        "saving_throw": "none",
        "description": """
            Spiritual Hammer creates a magical hammer that strikes as a weapon of the caster's deity. 
            The hammer can attack once per round and deals 1d4+1 points of damage per hit. 
            The spell lasts for 3 rounds plus 1 round per caster level.
        """,
    },
    "Stinking Cloud": {
        "level": 2,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "1 round/level",
        "area_of_effect": "20-foot cube",
        "saving_throw": "special",
        "description": """
            Stinking Cloud creates a cloud of noxious fumes that causes creatures in the area to become nauseated. 
            Creatures in the cloud must make a saving throw or be unable to take any action for the duration of the spell. 
            The cloud lasts for 1 round per caster level.
        """,
    },
    "Stone Shape": {
        "level": 3,
        "class": ["cleric", "druid", "mage"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "soft clay"],
        "range": "touch",
        "duration": "permanent",
        "area_of_effect": "up to 10 cubic feet + 1 cubic foot/level",
        "saving_throw": "none",
        "description": """
            Stone Shape allows the caster to reshape stone as if it were clay. 
            The spell can create doors, windows, or other shapes in stone walls, or it can be used to create sculptures. 
            The shape is permanent, and the spell affects up to 10 cubic feet of stone plus 1 cubic foot per caster level.
        """,
    },
    "Stone Tell": {
        "level": 6,
        "class": ["druid"],
        "school": "divination",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "1 turn",
        "area_of_effect": "one stone or stone object",
        "saving_throw": "none",
        "description": """
            Stone Tell allows the caster to speak with stone, gaining information about what the stone has experienced. 
            The stone can reveal details about events that occurred nearby, creatures that passed by, and other relevant information. 
            The spell lasts for 1 turn.
        """,
    },
    "Stoneskin": {
        "level": 4,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "granite and diamond dust"],
        "range": "touch",
        "duration": "until discharged",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Stoneskin grants the affected creature protection from physical attacks by turning its skin to stone. 
            The spell absorbs a number of attacks equal to 1d4 + 1 per two caster levels before it is discharged. 
            The spell lasts until it absorbs all the attacks or is dispelled.
        """,
    },
    # Continue adding more spells as needed...
})
spells.update({
    "Strength": {
        "level": 2,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "6 turns/level",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Strength increases the Strength score of the targeted creature by 1d6 points, up to a maximum of 18. 
            The spell lasts for 6 turns per caster level. 
            The increased Strength affects the creature's ability to hit and damage in melee combat.
        """,
    },
    "Suggestion": {
        "level": 3,
        "class": ["mage"],
        "school": "enchantment/charm",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation"],
        "range": "30 yards",
        "duration": "6 turns + 6 turns/level",
        "area_of_effect": "one creature",
        "saving_throw": "negates",
        "description": """
            Suggestion allows the caster to influence the actions of a creature by suggesting a course of action. 
            The suggestion must be reasonable, and the target gets a saving throw to resist the effect. 
            The spell lasts for 6 turns plus 6 turns per caster level or until the suggestion is carried out.
        """,
    },
    "Sunray": {
        "level": 7,
        "class": ["cleric"],
        "school": "evocation",
        "casting_time": "1 round (1 minute)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "caster",
        "duration": "instantaneous",
        "area_of_effect": "30-foot radius",
        "saving_throw": "none",
        "description": """
            Sunray calls forth a beam of sunlight that erupts from the caster, dealing 6d6 points of damage to undead 
            and creatures vulnerable to sunlight. 
            Undead in the area of effect are destroyed if they fail a saving throw, while others take 1d6 points of damage per caster level.
        """,
    },
    "Teleport": {
        "level": 5,
        "class": ["mage"],
        "school": "alteration",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "caster",
        "duration": "instantaneous",
        "area_of_effect": "caster and willing creatures touched",
        "saving_throw": "none",
        "description": """
            Teleport instantly transports the caster and a limited number of willing creatures or objects to a destination 
            within the caster's knowledge. 
            The destination must be on the same plane, and the accuracy of the teleport depends on the caster's familiarity with the location.
        """,
    },
    "True Seeing": {
        "level": 5,
        "class": ["cleric", "druid"],
        "school": "divination",
        "casting_time": "1 turn (10 minutes)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "1 round/level",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            True Seeing allows the target to see things as they truly are, revealing illusions, polymorphs, and hidden or invisible creatures. 
            The spell lasts for 1 round per caster level.
        """,
    },
    "Vampiric Touch": {
        "level": 3,
        "class": ["mage"],
        "school": "necromancy",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "instantaneous",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Vampiric Touch allows the caster to drain life energy from a target, dealing 1d6 points of damage per two caster levels 
            (up to 6d6). 
            The caster gains temporary hit points equal to the damage dealt, which last for 1 hour.
        """,
    },
    "Wall of Fire": {
        "level": 4,
        "class": ["mage", "druid"],
        "school": "evocation",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "concentration + 2 rounds/level",
        "area_of_effect": "up to 20 feet per level",
        "saving_throw": "none",
        "description": """
            Wall of Fire creates a barrier of flames up to 20 feet per caster level. 
            The wall deals 2d6 points of fire damage to any creature passing through it and 1d6 points of damage to creatures within 10 feet of it. 
            The wall blocks vision, and the flames burn for the duration of the spell.
        """,
    },
    "Wall of Ice": {
        "level": 4,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "4 segments (24 seconds)",
        "components": ["incantation", "gestures"],
        "range": "60 yards",
        "duration": "1 turn/level",
        "area_of_effect": "up to 10 square feet per level",
        "saving_throw": "none",
        "description": """
            Wall of Ice creates a barrier of ice up to 10 square feet per caster level. 
            The wall can be shaped as a plane or a hemisphere. 
            The wall is solid and blocks movement and vision. 
            Creatures breaking through the wall take 2d4 points of cold damage.
        """,
    },
    "Wall of Stone": {
        "level": 5,
        "class": ["cleric", "druid", "mage"],
        "school": "alteration",
        "casting_time": "5 segments (30 seconds)",
        "components": ["incantation", "gestures"],
        "range": "30 yards",
        "duration": "permanent",
        "area_of_effect": "up to 10 cubic feet per level",
        "saving_throw": "none",
        "description": """
            Wall of Stone creates a barrier of stone up to 10 cubic feet per caster level. 
            The wall can be shaped as desired and is permanent until destroyed or dispelled. 
            The wall blocks movement and vision.
        """,
    },
    "Water Breathing": {
        "level": 3,
        "class": ["mage", "druid"],
        "school": "alteration",
        "casting_time": "3 segments (18 seconds)",
        "components": ["incantation", "gestures"],
        "range": "touch",
        "duration": "1 hour/level",
        "area_of_effect": "one creature",
        "saving_throw": "none",
        "description": """
            Water Breathing allows the affected creature to breathe underwater for 1 hour per caster level. 
            The spell does not grant the ability to swim or protect from pressure or cold.
        """,
    },
    "Web": {
        "level": 2,
        "class": ["mage"],
        "school": "evocation",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures"],
        "range": "10 yards/level",
        "duration": "2 turns/level",
        "area_of_effect": "up to 8,000 cubic feet",
        "saving_throw": "negates",
        "description": """
            Web creates a mass of sticky webs that can entangle creatures in the area of effect. 
            The webs are strong and can only be broken by creatures with 13 Strength or higher. 
            The webs block movement and sight and last for 2 turns per caster level.
        """,
    },
    "Wind Walk": {
        "level": 7,
        "class": ["cleric"],
        "school": "alteration",
        "casting_time": "7 segments (42 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "touch",
        "duration": "6 turns + 1 turn/level",
        "area_of_effect": "one creature/level",
        "saving_throw": "none",
        "description": """
            Wind Walk allows the affected creatures to transform into a misty form, enabling them to travel at great speeds. 
            The creatures are nearly invisible in this form, immune to non-magical attacks, and can fly at 60 mph. 
            The spell lasts for 6 turns plus 1 turn per caster level.
        """,
    },
    "Wish": {
        "level": 9,
        "class": ["mage"],
        "school": "conjuration/summoning",
        "casting_time": "special",
        "components": ["incantation", "gestures", "rare and valuable materials"],
        "range": "unlimited",
        "duration": "instantaneous or as specified",
        "area_of_effect": "as specified",
        "saving_throw": "none",
        "description": """
            Wish is the most powerful spell a mage can cast, allowing the caster to alter reality itself. 
            The effects of the spell are limited only by the caster's imagination, but the greater the wish, the more likely there will be unforeseen consequences. 
            The spell requires rare and valuable materials and is taxing on the caster, often resulting in temporary weakness or other side effects.
        """,
    },
    "Word of Recall": {
        "level": 6,
        "class": ["cleric", "druid"],
        "school": "alteration",
        "casting_time": "1 segment (6 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "unlimited",
        "duration": "instantaneous",
        "area_of_effect": "caster and touched creatures",
        "saving_throw": "none",
        "description": """
            Word of Recall teleports the caster and any creatures they are touching to a designated location. 
            The destination must be a location that the caster has previously designated as a sanctuary. 
            The spell is instantaneous and has unlimited range, but the caster must have a strong connection to the destination.
        """,
    },
    "Zone of Truth": {
        "level": 2,
        "class": ["cleric"],
        "school": "enchantment/charm",
        "casting_time": "2 segments (12 seconds)",
        "components": ["incantation", "gestures", "holy symbol"],
        "range": "20 feet",
        "duration": "1 turn/level",
        "area_of_effect": "15-foot radius",
        "saving_throw": "negates",
        "description": """
            Zone of Truth creates an area in which creatures cannot lie. 
            Creatures within the area of effect must make a saving throw or be compelled to speak the truth. 
            The spell lasts for 1 turn per caster level and can be used to uncover hidden truths or deceive others into revealing information.
        """,
    }
})
