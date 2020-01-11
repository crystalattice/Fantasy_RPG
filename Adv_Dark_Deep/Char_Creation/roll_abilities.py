from Adv_Dark_Deep.dice_roller import multi_die


def _3d6():
    """Roll 3d6 six times. Each result is the value of the ability, from top to bottom

    This can lead to characters that are weaker than average and limit race and class eligibility.
    However, it can also lead to more role playing opportunities.
    """
    rolls = []
    for i in range(1, 7):
        roll = multi_die(3, 1)
        rolls.append(roll)
    return rolls


def _4d6_drop_lowest():
    """Roll 4d6 six times, discarding the lowest roll, keeping the order.

    This ensures above average scores and greater likelihood of getting the desired class.
    """
    rolls = []
    for x in range(1, 7):
        new_val = 0
        i = 0
        while i < 7:
            roll = multi_die(3, 1)
            if roll >= new_val:
                new_val = roll
            i += 1
        rolls.append(new_val)
    return rolls


def _2d6_plus_6():
    """Roll 2d6+6 six times, keeping the order.

    This ensures no score is too low and most abilities are above average.
    """
    rolls = []
    for i in range(1, 7):
        roll = multi_die(2, 1) + 6
        rolls.append(roll)
    return rolls


if __name__ == "__main__":
    print(_3d6())
    print(_4d6_drop_lowest())
    print(_2d6_plus_6())
