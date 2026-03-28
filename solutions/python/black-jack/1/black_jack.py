A = 1
face_card = {'J','Q','K'}
Q = 10
J = 10
K = 10
"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    ace_card = {'A'}
    face_card = {'J','Q','K'}
    if card in ace_card:
        return 1
    elif card in face_card : 
        return 10
    else:
        return int(card)
    pass


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    if val1 > val2:
      return card_one
    elif val2 > val1:
      return card_two
    elif val1 == val2:
      return card_one, card_two
    else :
      return card_one, card_two
    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    in_hand = {card_one , card_two}
    if "A" in in_hand:
       return 1 
    elif val1 + val2 > 10: 
       return 1
    else :
       return 11
    pass


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    in_hand = {card_one, card_two}
    if 'A' in in_hand and (val1 == 10 or val2 == 10) :
      return True
    else:
      return False
    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    if val1 == val2: 
        return True
    else: 
        return False 
    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    val3 = val1 + val2

    if val3 >= 9 and val3 <= 11:
        return True 
    else: 
        return False 
    pass
