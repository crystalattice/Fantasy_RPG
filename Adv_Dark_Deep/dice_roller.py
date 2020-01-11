from random import randint


def rand_num_gen(choice):
    """Get a random number to simulate a d6, d10, or d100 roll."""
    die = 0
    if choice == 1:  # d6 roll
        die = randint(1, 6)
    elif choice == 2:  # d10 roll
        die = randint(1, 10)
    elif choice == 3:  # d100 roll
        die = randint(1, 100)
    elif choice == 4:  # d4 roll
        die = randint(1, 4)
    elif choice == 5:  # d8 roll
        die = randint(1, 8)
    elif choice == 6:  # d12 roll
        die = randint(1, 12)
    elif choice == 7:  # d20 roll
        die = randint(1, 20)
    else:  # simple error message
        print("Shouldn't be here.  Invalid choice")
    return die


def multi_die(dice_number, die_type):
    """Add die rolls together, e.g. 2d6, 4d10, etc."""
    final_roll = 0
    val = 0

    while val < dice_number:
        final_roll += rand_num_gen(die_type)
        val += 1
    return final_roll


def test():
    """Test criteria to show script works."""
    _1d6 = multi_die(1, 1)  # 1d6
    print("1d6 = ", _1d6, )
    _2d6 = multi_die(2, 1)  # 2d6
    print("\n2d6 = ", _2d6, )
    _3d6 = multi_die(3, 1)  # 3d6
    print("\n3d6 = ", _3d6, )
    _4d6 = multi_die(4, 1)  # 4d6
    print("\n4d6 = ", _4d6, )
    _1d10 = multi_die(1, 2)  # 1d10
    print("\n1d10 = ", _1d10, )
    _2d10 = multi_die(2, 2)  # 2d10
    print("\n2d10 = ", _2d10, )
    _3d10 = multi_die(2, 2)  # 3d10
    print("\n3d10 = ", _3d10, )
    _d100 = multi_die(1, 3)  # d100
    print("\n1d100 = ", _d100, )


if __name__ == "__main__":  # run test() if calling as a separate program
    test()
