# shuffle a deck of cards, which should be a perfect shuffle

import random

def cards_shf1(cards):
    in_cards = list(cards)
    out_cards = []
    while in_cards != []:
        index = int(random.random() * len(in_cards))
        out_cards.append(in_cards[index])
        in_cards.pop(index)
    return out_cards


def cards_shf2(cards):
    out_cards = list(cards)
    for i in range(len(out_cards)):
        index = int(random.random() * (len(out_cards)-i))+i
        temp = out_cards[index]
        out_cards[index] = out_cards[i]
        out_cards[i] = temp
    return out_cards


cards = list(range(1,53))
print cards_shf2(cards)
