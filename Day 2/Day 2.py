import sys

bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def main1(arr):
    invalid_set = set()
    for index, game in enumerate(arr):
        for round in game:
            count_colors = round.split(', ')
            for count_color in count_colors:
                count, color = count_color.split(' ')
                if color in bag and int(count) > bag[color]:
                    invalid_set.add(index+1)
                    break
            if index+1 in invalid_set:
                break
    res = 0
    for i in range(1, len(arr)+1):
        if i not in invalid_set:
            res += i
    return res

def main2(arr):
    res = 0
    for game in arr:
        bag = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for round in game:
            count_colors = round.split(', ')
            for count_color in count_colors:
                count, color = count_color.split(' ')
                bag[color] = max(bag[color], int(count))

        res += bag["red"] * bag["green"] * bag["blue"]
            
    return res

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.split('\n')
            new_content = []
            for line in content:
                colon_index = line.index(':')
                new_content.append(line[colon_index+2:].split('; '))
            print("Part 1:", main1(new_content))
            print("Part 2:", main2(new_content))
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
