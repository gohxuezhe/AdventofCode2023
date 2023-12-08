numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9    
}

def part1(arr):
    res = 0
    for string in arr:
        l, r = 0, len(string)-1
        while not string[l].isdigit():
            l += 1
        while not string[r].isdigit():
            r -= 1
        res += int(string[l]) * 10 + int(string[r])
    return res

def part2(arr):
    res = 0
    for string in arr:
        digits = []
        for digit in numbers:
            index = string.find(digit)
            if index != -1:
                digits.append((index, numbers[digit]))
        for index, char in enumerate(string):
            if char.isdigit():
                digits.append((index, int(char)))
        digits.sort()
        res += digits[0][1] * 10 + digits[-1][1]
    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
