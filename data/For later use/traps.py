import random


class Trap:
    def __init__(self, difficulty_find=0, difficulty_disarm=0):
        self.difficulty_find = difficulty_find  # Modifier to find the trap
        self.difficulty_disarm = difficulty_disarm  # Modifier to disarm the trap
        self.is_found = False

    def find_trap(self, thief_skill):
        roll = random.randint(1, 100)
        adjusted_roll = roll + self.difficulty_find
        print(f"Thief attempts to find the trap... (Roll: {roll}, Adjusted Roll: {adjusted_roll})")

        if adjusted_roll <= thief_skill:
            self.is_found = True
            print("Trap found!")
        else:
            print("No trap detected.")

        return self.is_found

    def disarm_trap(self, thief_skill):
        if not self.is_found:
            print("No trap found to disarm.")
            return False

        roll = random.randint(1, 100)
        adjusted_roll = roll + self.difficulty_disarm
        print(f"Thief attempts to disarm the trap... (Roll: {roll}, Adjusted Roll: {adjusted_roll})")

        if roll == 100:
            print("Critical failure! The trap goes off in the thief's face!")
            return False
        elif adjusted_roll <= thief_skill:
            print("Trap successfully disarmed!")
            return True
        else:
            print("Failed to disarm the trap.")
            return False

    def time_to_find(self):
        time = random.randint(1, 10)
        print(f"Time taken to find trap: {time} minutes")
        return time

    def time_to_disarm(self):
        time = random.randint(1, 4)
        print(f"Time taken to disarm trap: {time} minutes")
        return time


# Example Usage
thief_skill_find = 70  # Thief's skill percentage for finding traps
thief_skill_disarm = 65  # Thief's skill percentage for disarming traps

# Create a trap with moderate difficulty to find and disarm
trap = Trap(difficulty_find=10, difficulty_disarm=5)

# Thief attempts to find the trap
trap.time_to_find()
found = trap.find_trap(thief_skill_find)

# If found, thief attempts to disarm the trap
if found:
    trap.time_to_disarm()
    trap.disarm_trap(thief_skill_disarm)
