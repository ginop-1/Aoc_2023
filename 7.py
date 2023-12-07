from enum import Enum

# this solution is really bad, ngl. enum not needed, dict was better
# class approach is okay but way overwill for this problem


class Cards1(Enum):
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Cards2(Enum):
    J = 1
    T = 11
    Q = 13
    K = 14
    A = 15


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    def __init__(self, raw_hand: str, bid: str, part: int) -> None:
        if part == 1:
            Card = Cards1
        else:
            Card = Cards2
        self.cards = [
            int(letter) if letter.isdigit() else Card[letter].value
            for letter in raw_hand
        ]
        self.detect_type(part)
        self.bid = int(bid)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.cards) + " - bid: " + str(self.bid)

    def detect_type(self, part: int):
        cards_count = [(card, self.cards.count(card)) for card in set(self.cards)]
        if part == 2:
            Js = [0, 0]
            high = [0, 0]
            for card in cards_count:
                if card[0] == 1:  # J found
                    Js = card
                if card[1] > high[1] and card[0] != 1:
                    high = list(card)
            if Js == (1, 5):
                self.hand_type = HandType["FIVE_OF_A_KIND"].value
                return
            if Js != [0, 0]:
                high[1] += Js[1]
                cards_count.remove(Js)
                for card in cards_count:
                    if card[0] == high[0]:
                        cards_count.remove(card)
                        cards_count.append(list(high))
        cards_count = [card_count[1] for card_count in cards_count]
        cards_count.sort()
        if cards_count == [5]:
            self.hand_type = HandType["FIVE_OF_A_KIND"].value
        elif cards_count == [1, 4]:
            self.hand_type = HandType["FOUR_OF_A_KIND"].value
        elif cards_count == [2, 3]:
            self.hand_type = HandType["FULL_HOUSE"].value
        elif cards_count == [1, 1, 3]:
            self.hand_type = HandType["THREE_OF_A_KIND"].value
        elif cards_count == [1, 2, 2]:
            self.hand_type = HandType["TWO_PAIR"].value
        elif cards_count == [1, 1, 1, 2]:
            self.hand_type = HandType["ONE_PAIR"].value
        elif cards_count == [1, 1, 1, 1, 1]:
            self.hand_type = HandType["HIGH_CARD"].value

    def __le__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        for mycard, othercard in zip(self.cards, other.cards):
            if mycard < othercard:
                return True
            if mycard > othercard:
                return False
        return False


def p1(f):
    hands = [(line.split()[0], line.split()[1]) for line in f.read().splitlines()]
    hands = [Hand(hand[0], hand[1], 1) for hand in hands]
    ranked_cards = []
    for hand in hands:
        if not ranked_cards:
            ranked_cards.append(hand)
        else:
            for ix, ranked in enumerate(ranked_cards):
                if hand <= ranked:
                    ranked_cards.insert(ix, hand)
                    break
            if hand not in ranked_cards:
                ranked_cards.append(hand)
    result = sum((ix + 1) * card.bid for ix, card in enumerate(ranked_cards))
    return result


def p2(f):
    hands = [(line.split()[0], line.split()[1]) for line in f.read().splitlines()]
    hands = [Hand(hand[0], hand[1], 2) for hand in hands]
    ranked_cards = []
    for hand in hands:
        if not ranked_cards:
            ranked_cards.append(hand)
        else:
            for ix, ranked in enumerate(ranked_cards):
                if hand <= ranked:
                    ranked_cards.insert(ix, hand)
                    break
            if hand not in ranked_cards:
                ranked_cards.append(hand)
    result = sum((ix + 1) * card.bid for ix, card in enumerate(ranked_cards))
    return result


if __name__ == "__main__":
    with open("input7.txt") as f:
        print(p1(f))
