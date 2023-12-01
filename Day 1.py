import sys

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

def main(arr):
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

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.split('\n')
            res = main(content)
            print("res:", res)
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
