from collections import Counter

def part1(arr):
    res = 0

    value = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pairs = []
    one_pair = []
    high_card = []

    for line in arr:
        hand, bid = line.split(' ')
        bid = int(bid)
        value_of_hand = 0
        for card in hand:
            value_of_hand = value_of_hand * 100 + value[card]
        hand_counter = Counter(hand)
        if len(hand_counter) == 5:
            high_card.append([value_of_hand, bid])
        elif len(hand_counter) == 4:
            one_pair.append([value_of_hand, bid])
        elif len(hand_counter) == 3:
            if 3 in hand_counter.values():
                three_of_a_kind.append([value_of_hand, bid])
            else:
                two_pairs.append([value_of_hand, bid])
        elif len(hand_counter) == 2:
            if 4 in hand_counter.values():
                four_of_a_kind.append([value_of_hand, bid])
            else:
                full_house.append([value_of_hand, bid])
        else:
            five_of_a_kind.append([value_of_hand, bid])
    high_card.sort()
    one_pair.sort()
    two_pairs.sort()
    three_of_a_kind.sort()
    four_of_a_kind.sort()
    full_house.sort()
    five_of_a_kind.sort()

    rank = 1
    for i in range(len(high_card)):
        res += high_card[i][1] * rank
        rank += 1
    for i in range(len(one_pair)):
        res += one_pair[i][1] * rank
        rank += 1
    for i in range(len(two_pairs)):
        res += two_pairs[i][1] * rank
        rank += 1
    for i in range(len(three_of_a_kind)):
        res += three_of_a_kind[i][1] * rank
        rank += 1
    for i in range(len(full_house)):
        res += full_house[i][1] * rank
        rank += 1
    for i in range(len(four_of_a_kind)):
        res += four_of_a_kind[i][1] * rank
        rank += 1
    for i in range(len(five_of_a_kind)):
        res += five_of_a_kind[i][1] * rank
        rank += 1

    return res

def part2(arr):
    res = 0

    value = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 11,
        '9': 10,
        '8': 9,
        '7': 8,
        '6': 7,
        '5': 6,
        '4': 5,
        '3': 4,
        '2': 3,
        'J': 2
    }

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pairs = []
    one_pair = []
    high_card = []

    for line in arr:
        hand, bid = line.split(' ')
        bid = int(bid)
        value_of_hand = 0
        for card in hand:
            value_of_hand = value_of_hand * 100 + value[card]
        tmp_card = hand.replace('J', '')
        if len(tmp_card) != 0:
            highest_count_card = Counter(tmp_card).most_common(1)[0][0]
            hand = hand.replace('J', highest_count_card)
        hand_counter = Counter(hand)
        if len(hand_counter) == 5:
            high_card.append([value_of_hand, bid])
        elif len(hand_counter) == 4:
            one_pair.append([value_of_hand, bid])
        elif len(hand_counter) == 3:
            if 3 in hand_counter.values():
                three_of_a_kind.append([value_of_hand, bid])
            else:
                two_pairs.append([value_of_hand, bid])
        elif len(hand_counter) == 2:
            if 4 in hand_counter.values():
                four_of_a_kind.append([value_of_hand, bid])
            else:
                full_house.append([value_of_hand, bid])
        else:
            five_of_a_kind.append([value_of_hand, bid])
    high_card.sort()
    one_pair.sort()
    two_pairs.sort()
    three_of_a_kind.sort()
    four_of_a_kind.sort()
    full_house.sort()
    five_of_a_kind.sort()

    rank = 1
    for i in range(len(high_card)):
        res += high_card[i][1] * rank
        rank += 1
    for i in range(len(one_pair)):
        res += one_pair[i][1] * rank
        rank += 1
    for i in range(len(two_pairs)):
        res += two_pairs[i][1] * rank
        rank += 1
    for i in range(len(three_of_a_kind)):
        res += three_of_a_kind[i][1] * rank
        rank += 1
    for i in range(len(full_house)):
        res += full_house[i][1] * rank
        rank += 1
    for i in range(len(four_of_a_kind)):
        res += four_of_a_kind[i][1] * rank
        rank += 1
    for i in range(len(five_of_a_kind)):
        res += five_of_a_kind[i][1] * rank
        rank += 1

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))