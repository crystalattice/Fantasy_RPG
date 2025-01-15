class VisionMode:
    def __init__(self, mode, range_in_feet):
        self.mode = mode
        self.range_in_feet = range_in_feet

    def use_vision(self, environment, light_source_present, underwater_depth=0, terrain_coverage=0):
        if self.mode == "Infravision":
            return self.infravision(environment, light_source_present, underwater_depth)
        elif self.mode == "Ultravision":
            return self.ultravision(environment, light_source_present, underwater_depth, terrain_coverage)
        else:
            return "Unknown vision mode."

    def infravision(self, environment, light_source_present, underwater_depth):
        if light_source_present:
            return "Infravision is spoiled by the presence of regular light sources."

        if underwater_depth > 0:
            if underwater_depth <= 100:
                return f"Infravision underwater: Can see up to {self.range_in_feet} feet, but may be confusing due to temperature currents."
            else:
                return f"Infravision underwater: Reduced effectiveness due to depth."

        visible_objects = [obj for obj in environment if obj['temperature'] > environment['ambient_temperature']]
        if visible_objects:
            details = ", ".join([obj['name'] for obj in visible_objects])
            return f"Infravision: You can see the following heat-emitting objects: {details}."
        else:
            return "Infravision: No heat sources detected."

    def ultravision(self, environment, light_source_present, underwater_depth, terrain_coverage):
        if light_source_present:
            return "Ultravision is spoiled by the presence of regular light sources."

        if underwater_depth > 200:
            return "Ultravision cannot be used at depths exceeding 200 feet."

        if underwater_depth > 0:
            range_in_feet = self.range_in_feet // 2 if underwater_depth <= 100 else 0
            if range_in_feet > 0:
                return f"Ultravision underwater: Can see up to {range_in_feet} feet."
            else:
                return "Ultravision cannot penetrate this depth."

        if terrain_coverage > 0:
            if terrain_coverage >= 6:
                return "Ultravision: Very dim sight with a range of only 3 feet."
            elif terrain_coverage >= 3:
                return "Ultravision: Extremely limited vision."

        visible_objects = [obj for obj in environment if obj.get('uv_reflective', False)]
        if visible_objects:
            details = ", ".join([obj['name'] for obj in visible_objects])
            return f"Ultravision: You can see the following UV-reflective objects: {details}."
        else:
            return "Ultravision: No UV-reflective objects detected."


# Example usage:

# Environment example for infravision:
dungeon_environment = {
    'ambient_temperature': 60,
    'objects': [
        {'name': 'Doorway', 'temperature': 60},
        {'name': 'Orc', 'temperature': 98},
        {'name': 'Treasure Chest', 'temperature': 60}
    ]
}

# Environment example for ultravision:
outdoor_environment = {
    'objects': [
        {'name': 'Rock', 'uv_reflective': False},
        {'name': 'Magical Glyph', 'uv_reflective': True}
    ]
}

# Create instances of vision modes
infravision = VisionMode(mode="Infravision", range_in_feet=60)
ultravision = VisionMode(mode="Ultravision", range_in_feet=300)

# Using Infravision in a dungeon environment without light sources
print(infravision.use_vision(dungeon_environment, light_source_present=False))

# Using Ultravision on a clear night without light sources or terrain coverage
print(ultravision.use_vision(outdoor_environment, light_source_present=False, terrain_coverage=0))
