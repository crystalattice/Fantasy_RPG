import random

class Flight:
    def __init__(self, speed, agility):
        self.speed = speed
        self.agility = agility
        self.turn_radius = self.get_turn_radius()
        self.acceleration_time = self.get_acceleration_time()

    def get_turn_radius(self):
        # Determine the turn radius based on agility
        agility_to_turn = {
            "perfect": 180,
            "good": 120,
            "average": 90,
            "poor": 60,
            "clumsy": 30
        }
        return agility_to_turn.get(self.agility.lower(), 0)

    def get_acceleration_time(self):
        # Determine time to accelerate to full speed based on agility
        agility_to_acceleration = {
            "perfect": 6,
            "good": 36,
            "average": 60,
            "poor": 120,
            "clumsy": 240
        }
        return agility_to_acceleration.get(self.agility.lower(), 0)

    def can_hover(self):
        # Only creatures with perfect or good agility can hover
        return self.agility.lower() in ["perfect", "good"]

    def can_perform_aerial_stunts(self):
        # Only creatures with perfect agility can perform complex aerial maneuvers
        return self.agility.lower() == "perfect"

    def flight_status(self, current_hp, max_hp):
        # Determine if a flying creature can continue flying based on damage taken
        if current_hp <= max_hp * 0.25:
            return "Fall"
        elif current_hp <= max_hp * 0.5:
            return "Forced Landing"
        else:
            return "Continue Flying"

    def missile_penalty(self, trained=False):
        # Apply penalties for using missile weapons while flying
        if trained:
            return {"short_range": -2, "medium_range": -5, "long_range": -5}
        else:
            return "Cannot use missile weapons without training"

    def time_to_strap_in(self):
        # Determine time to strap into a flying saddle
        return random.randint(1, 3) * 60  # in seconds

# Example Usage:

# Create a flying creature with speed and agility
flying_creature = Flight(speed=60, agility="good")

# Check the flight characteristics
print(f"Turn Radius: {flying_creature.turn_radius}° per minute")
print(f"Time to Accelerate to Full Speed: {flying_creature.acceleration_time} seconds")
print(f"Can Hover: {flying_creature.can_hover()}")
print(f"Can Perform Aerial Stunts: {flying_creature.can_perform_aerial_stunts()}")

# Check flight status based on damage taken
current_hp = 10
max_hp = 40
print(f"Flight Status: {flying_creature.flight_status(current_hp, max_hp)}")

# Missile weapon penalties while flying
print(f"Missile Penalties (trained): {flying_creature.missile_penalty(trained=True)}")
print(f"Missile Penalties (untrained): {flying_creature.missile_penalty(trained=False)}")

# Time to strap into the saddle
print(f"Time to Strap Into Saddle: {flying_creature.time_to_strap_in()} seconds")
