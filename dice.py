#!/usr/bin/python3

# ----------------------------------------------------------------------------
# |
# | File:         dice.py
# | Author:       Tan Duc MAI
# | Email:        tan.duc.work@gmail.com
# | Date:         02-Feb-2022
# | Description:  Displays the face value of dice to the screen.
# |   I hereby declare that I completed this work without any improper help
# |   from a third party and without using any aids other than those cited.
# |
# ----------------------------------------------------------------------------


def display_dice(dice):
    """Display the face value of dice to the screen.

    Parameters
    ----------
    list
        A list containing 5 die face values (die1, die2, die3, die4, die5).

    Returns
    -------
    None
    """
    # Display die number to the screen.
    print("\n")
    print(format("", '<5s'), end='')
    for i in range(len(dice)):
        print(format("Die " + str(i+1), '<10s'), end='')
    print()

    # Display face value of die to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        print(format("[" + str(dice[i]) + "]", '<10s'), end='')
    print("\n")

    # Display the top row of face value to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        if dice[i] == 1:
            print(format(" ", '<10s'), end='')
        elif dice[i] == 2 or dice[i] == 3:
            print(format("*", '<10s'), end='')
        elif dice[i] == 4 or dice[i] == 5 or dice[i] == 6:
            print(format("* *", '<10s'), end='')
    print()

    # Display the middle row of face value to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        if dice[i] == 1 or dice[i] == 3 or dice[i] == 5:
            print(format(" *", '<10s'), end='')
        elif dice[i] == 6:
            print(format("* *", '<10s'), end='')
        else:
            print(format(" ", '<10s'), end='')
    print()

    # Display the bottom row of face value to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        if dice[i] == 1:
            print(format(" ", '<10s'), end='')
        elif dice[i] == 2 or dice[i] == 3:
            print(format("  *", '<10s'), end='')
        elif dice[i] == 4 or dice[i] == 5 or dice[i] == 6:
            print(format("* *", '<10s'), end='')
    print("\n\n")
