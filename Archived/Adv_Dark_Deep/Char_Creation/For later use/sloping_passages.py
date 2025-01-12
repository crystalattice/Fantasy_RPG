class SlopingPassage:
    def __init__(self, total_length, vertical_drop):
        self.total_length = total_length  # Length of the passage in feet
        self.vertical_drop = vertical_drop  # Vertical drop in feet

    def is_detectable(self):
        # A slope is undetectable if it has a ratio of 100' horizontal to 10' vertical or less.
        if self.total_length >= self.vertical_drop * 10:
            return False
        else:
            return True

    def calculate_final_level(self, current_level):
        # Calculate the change in level based on the vertical drop
        level_change = self.vertical_drop / 10
        final_level = current_level - level_change
        return final_level

    def passage_info(self, current_level):
        detectable = self.is_detectable()
        final_level = self.calculate_final_level(current_level)

        print(f"Passage Length: {self.total_length} feet")
        print(f"Vertical Drop: {self.vertical_drop} feet")
        print(f"Current Level: {current_level}")
        print(f"Final Level after Passage: {final_level}")
        print(f"Is the slope detectable? {'Yes' if detectable else 'No'}\n")

# Example Usage
passage1 = SlopingPassage(total_length=300, vertical_drop=15)  # Example passage
passage2 = SlopingPassage(total_length=150, vertical_drop=20)  # Steeper passage

# Assume the party starts on level 1 of the dungeon
current_level = 1

# Get information about the sloping passages
passage1.passage_info(current_level)
passage2.passage_info(current_level)
