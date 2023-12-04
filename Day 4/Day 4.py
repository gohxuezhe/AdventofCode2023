import sys
import collections

def main1(arr):
    res = 0

    for line in arr:
        index = line.find(':')
        winning_nums, my_nums = line[index+1:].split('|')
        winning_nums = set(winning_nums.split())
        my_nums = my_nums.split()
        curr_points = 0
        for num in my_nums:
            if num in winning_nums:
                if curr_points == 0:
                    curr_points += 1
                else:
                    curr_points *= 2
        res += curr_points

    return res

def main2(arr):
    res = 0

    card_count_dict = collections.defaultdict(lambda:1)
            
    for card, line in enumerate(arr):
        index = line.find(':')
        winning_nums, my_nums = line[index+1:].split('|')
        winning_nums = set(winning_nums.split())
        my_nums = my_nums.split()
        match_count = 0
        for num in my_nums:
            if num in winning_nums:
                match_count += 1
        for card_copy in range(card + 1, card + 1 + match_count):
            card_count_dict[card_copy] += card_count_dict[card]

    res += sum(card_count_dict.values()) + 1

    return res

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.split('\n')
            print("Part 1:", main1(content))
            print("Part 2:", main2(content))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
    else:
        file_path = sys.argv[1]
        read_file(file_path)
