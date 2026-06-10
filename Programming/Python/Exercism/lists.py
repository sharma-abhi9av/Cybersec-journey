"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    n = number 
    list = [number, n +1, n +2 ]
    return list
    pass


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    list = rounds_1 + rounds_2
    return list
    pass


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else: 
        return False
    pass


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    average = sum(hand) / len(hand)
    return average
    pass


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card)== calculated average. 

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    l = len(hand)
    middle_card = hand[l//2]
    average_orfirstandsecond = (hand[0] + hand[-1]) / 2
    calculated_avg = sum(hand) / len(hand)
    if middle_card == calculated_avg or average_orfirstandsecond == calculated_avg:
        return True 
    else: 
        return False 
    pass


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_list = []
    odd_list = []
    for i in range(len(hand)):
       if i % 2 == 0: 
          even_list.append(hand[i])
       else: 
           odd_list.append(hand[i])
    avg_of_even = sum(even_list) / len(even_list)
    avg_of_odd = sum(odd_list) / len(odd_list)
    if avg_of_even == avg_of_odd:
        return True
    else: 
        return False 
    pass


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11: 
        hand[-1] = hand[-1] * 2
        return hand
    else : 
        hand[-1] = hand[-1]
        return hand
    pass
