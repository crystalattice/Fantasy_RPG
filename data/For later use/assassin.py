class Assassin:
    def __init__(self, name, race, strength, dexterity, intelligence, level=1):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.level = level
        self.hit_points = self.calculate_hit_points()
        self.weapon_proficiencies = self.get_weapon_proficiencies()
        self.abilities = self.get_abilities()
        self.alignment = None
        self.experience_points = 0

    def calculate_hit_points(self):
        # Hit Points are calculated as 1d6 per level
        return sum([random.randint(1, 6) for _ in range(self.level)])

    def get_weapon_proficiencies(self):
        initial_proficiencies = 3
        new_proficiency_every = 4
        return initial_proficiencies + (self.level - 1) // new_proficiency_every

    def get_abilities(self):
        abilities = {
            'Assassinate': self.get_assassinate_chance(),
            'Back Stab': self.get_backstab_multiplier(),
            'Disguise': self.get_disguise_chance(),
            'Pick Pockets': self.get_pick_pockets_chance(),
            'Open Locks': self.get_open_locks_chance(),
            'Find and Remove Traps': self.get_find_remove_traps_chance(),
            'Move Silently': self.get_move_silently_chance(),
            'Hide in Shadows': self.get_hide_in_shadows_chance(),
            'Listen at Doors': self.get_listen_at_doors_chance(),
            'Climb Walls': self.get_climb_walls_chance(),
            'Read Languages': self.get_read_languages_chance(),
            'Poison': self.get_poison_ability()
        }
        return abilities

    def get_assassinate_chance(self):
        base_chance = 50
        modifier = 5 * (self.level - 1)
        return min(100, base_chance + modifier)

    def get_backstab_multiplier(self):
        if 1 <= self.level <= 4:
            return 2
        elif 5 <= self.level <= 8:
            return 3
        elif 9 <= self.level <= 12:
            return 4
        else:
            return 5

    def get_disguise_chance(self):
        return self.level * 5  # Just an example formula

    def get_pick_pockets_chance(self):
        pick_pockets_table = {3: 30, 4: 35, 5: 40, 6: 45, 7: 50, 8: 55,
                              9: 60, 10: 65, 11: 70, 12: 80, 13: 90, 14: 100, 15: 105}
        return pick_pockets_table.get(self.level, 0)

    def get_open_locks_chance(self):
        open_locks_table = {3: 25, 4: 29, 5: 33, 6: 37, 7: 42, 8: 47,
                            9: 52, 10: 57, 11: 62, 12: 67, 13: 72, 14: 77, 15: 82}
        return open_locks_table.get(self.level, 0)

    def get_find_remove_traps_chance(self):
        find_remove_traps_table = {3: 20, 4: 25, 5: 30, 6: 35, 7: 40, 8: 45,
                                   9: 50, 10: 55, 11: 60, 12: 65, 13: 70, 14: 75, 15: 80}
        return find_remove_traps_table.get(self.level, 0)

    def get_move_silently_chance(self):
        move_silently_table = {3: 15, 4: 21, 5: 27, 6: 33, 7: 40, 8: 47,
                               9: 55, 10: 62, 11: 70, 12: 78, 13: 86, 14: 94, 15: 99}
        return move_silently_table.get(self.level, 0)

    def get_hide_in_shadows_chance(self):
        hide_in_shadows_table = {3: 10, 4: 15, 5: 20, 6: 25, 7: 31, 8: 37,
                                 9: 43, 10: 49, 11: 56, 12: 63, 13: 70, 14: 77, 15: 85}
        return hide_in_shadows_table.get(self.level, 0)

    def get_listen_at_doors_chance(self):
        listen_at_doors_table = {3: 10, 4: 10, 5: 15, 6: 15, 7: 20, 8: 20,
                                 9: 25, 10: 25, 11: 30, 12: 30, 13: 35, 14: 35, 15: 40}
        return listen_at_doors_table.get(self.level, 0)

    def get_climb_walls_chance(self):
        climb_walls_table = {3: 85, 4: 86, 5: 87, 6: 88, 7: 90, 8: 92,
                             9: 94, 10: 96, 11: 98, 12: 99, 13: 99.1, 14: 99.2, 15: 99.3}
        return climb_walls_table.get(self.level, 0)

    def get_read_languages_chance(self):
        if self.level >= 6:
            read_languages_table = {6: 20, 7: 25, 8: 30, 9: 35, 10: 40, 11: 45, 12: 50, 13: 55, 14: 60, 15: 65}
            return read_languages_table.get(self.level, 0)
        return 0

    def get_poison_ability(self):
        if self.level >= 9:
            return True
        return False

    def level_up(self, exp):
        self.experience_points += exp
        required_exp = [1500, 3000, 6000, 12000, 25000, 50000, 100000, 200000, 300000, 425000, 575000, 750000, 1000000, 1500000]
        if self.level < 15 and self.experience_points >= required_exp[self.level - 1]:
            self.level += 1
            self.hit_points += random.randint(1, 6)
            self.weapon_proficiencies = self.get_weapon_proficiencies()
            self.abilities = self.get_abilities()

    def set_alignment(self, alignment):
        if alignment not in ['Neutral Evil', 'Lawful Evil', 'Chaotic Evil', 'Neutral']:
            raise ValueError("Invalid alignment for Assassin")
        self.alignment = alignment


# Example of creating an assassin character
assassin = Assassin(name="Shadow", race="Human", strength=14, dexterity=16, intelligence=13)
print(f"{assassin.name} is a level {assassin.level} assassin with {assassin.hit_points} hit points.")
print(f"Assassinate chance: {assassin.abilities['Assassinate']}%")
print(f"Backstab multiplier: {assassin.abilities['Back Stab']}x")
