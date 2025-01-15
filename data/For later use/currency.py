class MonetarySystem:
    """Handles the conversion and operations of different types of coins in the standard monetary system."""

    # Conversion rates based on the standard system
    CONVERSION_RATES = {
        'copper': 1/200,        # 200 copper pieces = 1 gold piece
        'silver': 1/20,         # 20 silver pieces = 1 gold piece
        'electrum': 1/2,        # 2 electrum pieces = 1 gold piece
        'gold': 1,              # 1 gold piece = 1 gold piece
        'platinum': 5           # 1 platinum piece = 5 gold pieces
    }

    def __init__(self, copper: int = 0, silver: int = 0, electrum: int = 0, gold: int = 0, platinum: int = 0):
        self.copper = copper
        self.silver = silver
        self.electrum = electrum
        self.gold = gold
        self.platinum = platinum

    def convert_to_gold(self) -> float:
        """Converts all the currency types to their equivalent in gold pieces."""
        total_gold = (self.copper * self.CONVERSION_RATES['copper'] +
                      self.silver * self.CONVERSION_RATES['silver'] +
                      self.electrum * self.CONVERSION_RATES['electrum'] +
                      self.gold * self.CONVERSION_RATES['gold'] +
                      self.platinum * self.CONVERSION_RATES['platinum'])
        return total_gold

    def convert_from_gold(self, gold_amount: float) -> Dict[str, int]:
        """Converts a gold piece amount to the equivalent in all other currency types."""
        remaining_gold = gold_amount

        # Calculate the number of platinum pieces
        platinum = int(remaining_gold // self.CONVERSION_RATES['platinum'])
        remaining_gold -= platinum * self.CONVERSION_RATES['platinum']

        # Calculate the number of gold pieces
        gold = int(remaining_gold)
        remaining_gold -= gold

        # Calculate the number of electrum pieces
        electrum = int(remaining_gold // self.CONVERSION_RATES['electrum'])
        remaining_gold -= electrum * self.CONVERSION_RATES['electrum']

        # Calculate the number of silver pieces
        silver = int(remaining_gold // self.CONVERSION_RATES['silver'])
        remaining_gold -= silver * self.CONVERSION_RATES['silver']

        # Calculate the number of copper pieces
        copper = int(remaining_gold // self.CONVERSION_RATES['copper'])

        return {
            'platinum': platinum,
            'gold': gold,
            'electrum': electrum,
            'silver': silver,
            'copper': copper
        }

    def add_currency(self, copper: int = 0, silver: int = 0, electrum: int = 0, gold: int = 0, platinum: int = 0):
        """Adds the specified amount of currency to the current total."""
        self.copper += copper
        self.silver += silver
        self.electrum += electrum
        self.gold += gold
        self.platinum += platinum

    def subtract_currency(self, copper: int = 0, silver: int = 0, electrum: int = 0, gold: int = 0, platinum: int = 0):
        """Subtracts the specified amount of currency from the current total."""
        # Convert all amounts to gold pieces for easier subtraction
        current_total_gold = self.convert_to_gold()
        amount_to_subtract = (copper * self.CONVERSION_RATES['copper'] +
                              silver * self.CONVERSION_RATES['silver'] +
                              electrum * self.CONVERSION_RATES['electrum'] +
                              gold * self.CONVERSION_RATES['gold'] +
                              platinum * self.CONVERSION_RATES['platinum'])

        if amount_to_subtract > current_total_gold:
            raise ValueError("Insufficient funds to subtract the specified amount.")

        # Convert the remaining gold pieces back to individual currency types
        new_total_gold = current_total_gold - amount_to_subtract
        new_currency = self.convert_from_gold(new_total_gold)

        self.copper = new_currency['copper']
        self.silver = new_currency['silver']
        self.electrum = new_currency['electrum']
        self.gold = new_currency['gold']
        self.platinum = new_currency['platinum']

    def __repr__(self) -> str:
        """Returns a string representation of the current currency amounts."""
        return (f"Currency: {self.platinum} platinum, {self.gold} gold, "
                f"{self.electrum} electrum, {self.silver} silver, {self.copper} copper")


# Example Usage
currency = MonetarySystem(copper=1000, silver=50, electrum=10, gold=5, platinum=1)
print(f"Total in gold: {currency.convert_to_gold()} g.p.")

currency.add_currency(gold=10)
print(f"After adding currency: {currency}")

currency.subtract_currency(silver=30, gold=3)
print(f"After subtracting currency: {currency}")

conversion_result = currency.convert_from_gold(50)
print(f"Converting 50 gold to other currencies: {conversion_result}")
