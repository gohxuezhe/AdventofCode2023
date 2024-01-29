from collections import deque

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def part1(arr):
    m, n = len(arr), len(arr[0])
    start = None
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 'S':
                start = (i, j)
                break
        if start:
            break

    res = {start}
    for i in range(64):
        new_res = set()
        for y, x in res:
            for dy, dx in moves:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < m and 0 <= new_x < n and arr[new_y][new_x] != '#':
                        new_res.add((new_y, new_x))
        res = new_res

    return len(res)

def part2(arr):
    return

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
