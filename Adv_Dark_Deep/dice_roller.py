from random import randint
from typing import Any, Union


def rand_num_gen(choice: int) -> int:
    """Get a random number to simulate a d6, d10, or d100 roll."""
    die: Union[int, int] = 1
    if choice == 6:  # d6 roll
        die = randint(1, 6)
    elif choice == 10:  # d10 roll
        die = randint(1, 10)
    elif choice == 100:  # d100 roll
        die = randint(1, 100)
    elif choice == 4:  # d4 roll
        die = randint(1, 4)
    elif choice == 8:  # d8 roll
        die = randint(1, 8)
    elif choice == 12:  # d12 roll
        die = randint(1, 12)
    elif choice == 20:  # d20 roll
        die = randint(1, 20)
    return die


def multi_die(dice_number: int, die_type: int) -> int:
    """Add die rolls together, e.g. 2d6, 4d10, etc."""
    final_roll: int = 0
    val: int = 0

    while val < dice_number:
        final_roll += rand_num_gen(die_type)
        val += 1
    return final_roll


def test():
    """Test criteria to show script works."""
    _1d6: int = multi_die(1, 6)  # 1d6
    print("1d6 = ", _1d6, )
    _2d6: int = multi_die(2, 6)  # 2d6
    print("\n2d6 = ", _2d6, )
    _3d6: int = multi_die(3, 6)  # 3d6
    print("\n3d6 = ", _3d6, )
    _4d6: int = multi_die(4, 6)  # 4d6
    print("\n4d6 = ", _4d6, )
    _1d10: int = multi_die(1, 10)  # 1d10
    print("\n1d10 = ", _1d10, )
    _2d10: int = multi_die(2, 10)  # 2d10
    print("\n2d10 = ", _2d10, )
    _3d10: int = multi_die(2, 10)  # 3d10
    print("\n3d10 = ", _3d10, )
    _d100: int = multi_die(1, 100)  # d100
    print("\n1d100 = ", _d100, )


if __name__ == "__main__":  # run test() if calling as a separate program
    test()
