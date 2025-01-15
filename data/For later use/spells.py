import random

class Spell:
    def __init__(self, name, level, casting_time, material_components=None):
        self.name = name
        self.level = level
        self.casting_time = casting_time  # in segments (6 seconds each)
        self.material_components = material_components if material_components else []

class SpellBook:
    def __init__(self, book_type="standard"):
        self.book_type = book_type
        self.spells = []
        self.page_capacity = self.set_page_capacity()
        self.pages_used = 0

    def set_page_capacity(self):
        if self.book_type == "standard":
            return 144
        elif self.book_type == "traveling":
            return 36
        elif self.book_type == "reference":
            return 288
        else:
            raise ValueError("Invalid spell book type")

    def add_spell(self, spell):
        spell_pages = self.calculate_spell_pages(spell.level)
        if self.pages_used + spell_pages > self.page_capacity:
            print(f"Not enough space to add {spell.name} to the spell book.")
        else:
            self.spells.append(spell)
            self.pages_used += spell_pages
            print(f"{spell.name} added to the spell book.")

    @staticmethod
    def calculate_spell_pages(spell_level):
        if spell_level == 0:
            return 4
        elif 1 <= spell_level <= 3:
            return 6
        elif 4 <= spell_level <= 6:
            return 9
        elif 7 <= spell_level <= 9:
            return 18
        else:
            raise ValueError("Invalid spell level")

class SpellCaster:
    def __init__(self, name, caster_class):
        self.name = name
        self.caster_class = caster_class
        self.spell_books = {"standard": SpellBook("standard"), "traveling": None}
        self.current_spells = []

    def rest_and_memorize_spells(self, spells_to_memorize):
        total_rest_hours = self.calculate_rest_hours(spells_to_memorize)
        total_study_time = self.calculate_study_time(spells_to_memorize)

        print(f"{self.name} needs to rest for {total_rest_hours} hours and study for {total_study_time} minutes to memorize the spells.")

        self.current_spells = spells_to_memorize

    @staticmethod
    def calculate_rest_hours(spells):
        max_rest_needed = max(spell.level for spell in spells)
        if max_rest_needed <= 2:
            return 4
        elif 3 <= max_rest_needed <= 4:
            return 6
        elif 5 <= max_rest_needed <= 6:
            return 8
        elif 7 <= max_rest_needed <= 8:
            return 10
        elif max_rest_needed == 9:
            return 12
        else:
            raise ValueError("Invalid spell level")

    @staticmethod
    def calculate_study_time(spells):
        time_needed = 0
        for spell in spells:
            if spell.level == 1:
                time_needed += 15
            elif spell.level == 2:
                time_needed += 30
            elif spell.level == 3:
                time_needed += 45
            elif spell.level == 4:
                time_needed += 60
            elif spell.level == 5:
                time_needed += 75
            elif spell.level == 6:
                time_needed += 90
            elif spell.level == 7:
                time_needed += 105
            elif spell.level == 8:
                time_needed += 120
            elif spell.level == 9:
                time_needed += 135
            else:
                raise ValueError("Invalid spell level")
        return time_needed

    def cast_spell(self, spell_name):
        for spell in self.current_spells:
            if spell.name == spell_name:
                if spell.material_components:
                    print(f"Casting {spell.name} with material components: {', '.join(spell.material_components)}")
                else:
                    print(f"Casting {spell.name}")
                self.current_spells.remove(spell)
                return
        print(f"{self.name} has not memorized the spell {spell_name}.")

    def read_spell_from_book(self, spell_name, book_type="standard"):
        if book_type not in self.spell_books or not self.spell_books[book_type]:
            print(f"{self.name} does not have a {book_type} spell book.")
            return

        for spell in self.spell_books[book_type].spells:
            if spell.name == spell_name:
                if random.randint(1, 100) <= spell.level:
                    print(f"{spell_name} and adjacent spells are erased from the book!")
                    self.spell_books[book_type].spells.remove(spell)
                else:
                    print(f"{self.name} casts {spell_name} directly from the spell book.")
                return
        print(f"{spell_name} is not found in the {book_type} spell book.")

# Example usage:

# Define some spells
fireball = Spell(name="Fireball", level=3, casting_time=3, material_components=["bat guano", "sulfur"])
magic_missile = Spell(name="Magic Missile", level=1, casting_time=1)

# Create a spell caster
gandalf = SpellCaster(name="Gandalf", caster_class="Mage")

# Add spells to Gandalf's spell book
gandalf.spell_books["standard"].add_spell(fireball)
gandalf.spell_books["standard"].add_spell(magic_missile)

# Memorize some spells
gandalf.rest_and_memorize_spells([fireball, magic_missile])

# Cast a spell
gandalf.cast_spell("Fireball")

# Attempt to cast a spell directly from the spell book
gandalf.read_spell_from_book("Fireball")

