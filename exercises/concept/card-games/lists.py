"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
from math import ceil


def get_rounds(num):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return [num, num + 1, num + 2]


def concatenate_rounds(r1, r2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return r1 + r2


def list_contains_round(rounds, num):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return num in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    aprox1 = (hand[0] + hand[len(hand) - 1]) / 2
    aprox2 = hand[ceil(len(hand) / 2)]
    return aprox1 == average or aprox2 == average


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    sum_even = 0
    len_even = 0
    sum_odd = 0
    len_odd = 0

    for i in range(0, len(hand), 2):
        sum_even += hand[i]
        len_even += 1
    for i in range(1, len(hand), 2):
        sum_odd += hand[i]
        len_odd += 1

    avg_even = sum_even / len_even
    avg_odd = sum_odd / len_odd
    return avg_even == avg_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[len(hand) - 1] == 11:
        hand[len(hand) - 1] *= 2
    return hand
