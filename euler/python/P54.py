"""
Poker Hands
Problem 54
"""

POKER_TXT = "P54.txt"
CARDS = 5
CARD_VALUES = map(str, range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']
VALUE, SUIT = 0, 1

# Returns the numerical value of the given card
def value_of(card):
    return CARD_VALUES.index(card[VALUE])

def generic_matching(hand, unique, repeat):
    # Find all values with repeats equal to repeat
    values = map(value_of, hand)
    found_values = []
    for value in values:
        if values.count(value) >= repeat and value not in found_values:
            found_values.append(value)
    # If we found the wrong number of values, return None
    if len(found_values) != unique:
        return None
    # Otherwise we return those cards appended to the numeric value of the rest
    other_cards = sorted(filter(lambda x: x not in found_values, values), reverse = True)
    return sorted(found_values, reverse = True) + other_cards

def high_card(hand):
    return sorted(map(value_of, hand), reverse = True)

def one_pair(hand):
    return generic_matching(hand, 1, 2)

def two_pair(hand):
    return generic_matching(hand, 2, 2)

def three_of_a_kind(hand):
    return generic_matching(hand, 1, 3)

def straight(hand):
    values = sorted(map(value_of, hand))
    if range(values[0], values[-1] + 1) == values:
        return high_card(hand)

def flush(hand):
    if len({card[SUIT] : True for card in hand}) == 1:
        return high_card(hand)

def full_house(hand):
    if two_pair(hand):
        return three_of_a_kind(hand)

def four_of_a_kind(hand):
    return generic_matching(hand, 1, 4)

def straight_flush(hand):
    if flush(hand):
        return straight(hand)

# An array containing each possible hand
HANDS = [
    high_card,
    one_pair,
    two_pair,
    three_of_a_kind,
    straight,
    flush,
    full_house,
    four_of_a_kind,
    straight_flush
]

def player(hands):
    # Each function returns either nil if the hand does not have that function applicable, or
    # the card value (numerically) of the card representing that function's hand. It also returns
    # an array of the rest of the card values that were not used to make that hand.
    player_hands = [None, None]
    for player in xrange(len(player_hands)):
        for i in xrange(len(HANDS)):
            hand = HANDS[i](hands[player])
            if hand:
                player_hands[player] = max([i] + hand, player_hands[player])
    return player_hands[0] > player_hands[1]

def process_poker_hands():
    # Opens the poker file and makes it readable
    hands = map(lambda x: x[:-1].split(" "), open(POKER_TXT, 'r').readlines())
    return map(lambda x: map(lambda y: map(tuple, y), [x[:CARDS], x[CARDS:]]), hands)

if __name__ == '__main__':
    print sum(player(hand) for hand in process_poker_hands())
