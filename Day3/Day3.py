import collections

moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def part1(arr):
    res = 0

    ROWS, COLS = len(arr), len(arr[0])
    for row in range(ROWS):
        curr_num = 0
        indexes = []
        for col in range(COLS):
            if arr[row][col].isdigit() and col != COLS - 1:
                curr_num = curr_num * 10 + int(arr[row][col])
                indexes.append(col)
            else:
                if col == COLS - 1 and arr[row][col].isdigit():
                    curr_num = curr_num * 10 + int(arr[row][col])
                    indexes.append(col)
                if curr_num != 0:
                    for index in indexes:
                        found = False
                        for dy, dx in moves:
                            check_row, check_col = row + dy, index + dx
                            if 0 <= check_row < ROWS and 0 <= check_col < COLS and arr[check_row][check_col] not in "0123456789.":
                                res += curr_num
                                found = True
                                break
                        if found:
                            break
                curr_num = 0
                indexes.clear()
    return res

def part2(arr):
    res = 0

    index_to_nums = collections.defaultdict(list)
    
    ROWS, COLS = len(arr), len(arr[0])
    for row in range(ROWS):
        curr_num = 0
        indexes = []
        for col in range(COLS):
            if arr[row][col].isdigit() and col != COLS - 1:
                curr_num = curr_num * 10 + int(arr[row][col])
                indexes.append(col)
            else:
                if col == COLS - 1 and arr[row][col].isdigit():
                    curr_num = curr_num * 10 + int(arr[row][col])
                    indexes.append(col)
                if curr_num != 0:
                    for index in indexes:
                        found = False
                        for dy, dx in moves:
                            check_row, check_col = row + dy, index + dx
                            if 0 <= check_row < ROWS and 0 <= check_col < COLS and arr[check_row][check_col] not in "0123456789.":
                                index_to_nums[(check_row, check_col)].append(curr_num)
                                found = True
                                break
                        if found:
                            break
                curr_num = 0
                indexes.clear()

    for value in index_to_nums.values():
        if len(value) == 2:
            res += value[0] * value[1]
            
    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
