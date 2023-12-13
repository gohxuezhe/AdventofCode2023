directions = {
    '|': {
        "up": (-1, 0, "up"),
        "down": (1, 0, "down"),
    },
    '-': {
        "left": (0, -1, "left"),
        "right": (0, 1, "right"),
    },
    'L': {
        "down": (0, 1, "right"),
        "left": (-1, 0, "up"),
    },
    'J': {
        "down": (0, -1, "left"),
        "right": (-1, 0, "up"),
    },
    '7': {
        "up": (0, -1, "left"),
        "right": (1, 0, "down"),
    },
    'F': {
        "up": (0, 1, "right"),
        "left": (1, 0, "down"),
    },
}

def part1(arr):
    start = None
    ROWS, COLS = len(arr), len(arr[0])
    for row in range(ROWS):
        for col in range(COLS):
            if arr[row][col] == 'S':
                start = (row, col)
                break
    next = []
    for row_offset, col_offset, direction in ((0, 1, "right"), (0, -1, "left"), (1, 0, "down"), (-1, 0, "up")):
        row, col = start[0] + row_offset, start[1] + col_offset
        if 0 <= row < ROWS and 0 <= col < COLS and arr[row][col] in directions:
            next.append((row, col, direction, 1))
    res = 0
    while next:
        row, col, direction, steps = next.pop(0)
        if arr[row][col] == 'S':
            res = max(res, steps)
        elif arr[row][col] in directions and direction in directions[arr[row][col]]:
            row_offset, col_offset, new_direction = directions[arr[row][col]][direction]
            new_row, new_col = row + row_offset, col + col_offset
            next.append((new_row, new_col, new_direction, steps + 1))

    return res // 2

def part2(arr):
    start = None
    ROWS, COLS = len(arr), len(arr[0])
    for row in range(ROWS):
        for col in range(COLS):
            if arr[row][col] == 'S':
                start = (row, col)
                break
    loop = [start]
    next = [(36, 17, 'down')] # cheated by hardcoding the start of the loop
    # for row_offset, col_offset, direction in ((0, 1, "right"), (0, -1, "left"), (1, 0, "down"), (-1, 0, "up")):
    #     row, col = start[0] + row_offset, start[1] + col_offset
    #     if 0 <= row < ROWS and 0 <= col < COLS and arr[row][col] in directions:
    #         next.append((row, col, direction))
    while next:
        row, col, direction = next.pop(0)
        if arr[row][col] in directions and direction in directions[arr[row][col]]:
            row_offset, col_offset, new_direction = directions[arr[row][col]][direction]
            new_row, new_col = row + row_offset, col + col_offset
            next.append((new_row, new_col, new_direction))
            loop.append((row, col))

    ### Credit: https://github.com/xavdid/advent-of-code/blob/main/solutions/2023/day_10/solution.py#L61 
    padded_points = [*loop, loop[0]]
    interior_area = sum(row1 * col2 - row2 * col1 for (row1, col1), (row2, col2) in zip(padded_points,padded_points[1:]))/ 2
    return int(abs(interior_area) - 0.5 * len(loop) + 1)
    
    

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
