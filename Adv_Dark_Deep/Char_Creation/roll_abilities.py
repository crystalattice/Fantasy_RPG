from typing import List

from Adv_Dark_Deep.dice_roller import multi_die


def three_d6() -> list:
    """Roll 3d6 six times. Each result is the value of the ability, from top to bottom

    This can lead to characters that are weaker than average and limit race and class eligibility.
    However, it can also lead to more role playing opportunities.
    """
    rolls: List[int] = []
    for i in range(1, 7):
        roll: int = multi_die(3, 1)
        rolls.append(roll)
    return rolls


def four_d6_drop_lowest() -> list:
    """Roll 4d6 six times, discarding the lowest roll, keeping the order.

    This ensures above average scores and greater likelihood of getting the desired class.
    """
    rolls: List[int] = []
    for x in range(1, 7):
        new_val: int = 0
        i: int = 0
        while i < 7:
            roll: int = multi_die(3, 1)
            if roll >= new_val:
                new_val = roll
            i += 1
        rolls.append(new_val)
    return rolls


def two_d6_plus_6() -> list:
    """Roll 2d6+6 six times, keeping the order.

    This ensures no score is too low and most abilities are above average.
    """
    rolls: List[int] = []
    for i in range(1, 7):
        roll: int = multi_die(2, 1) + 6
        rolls.append(roll)
    return rolls


if __name__ == "__main__":
    print(three_d6())
    print(four_d6_drop_lowest())
    print(two_d6_plus_6())
