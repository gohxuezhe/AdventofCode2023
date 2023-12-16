def part1(arr):
    res = set()

    visited = set()
    next = []
    start = (0, -1, 0, 1)
    next.append(start)
    while next:
        curr = next.pop()
        if curr in visited:
            continue
        visited.add(curr)
        y, x, dy, dx = curr
        res.add((y, x))
        new_y, new_x = y + dy, x + dx
        if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]):
            continue
        if arr[new_y][new_x] == '.':
            next.append((new_y, new_x, dy, dx))
        elif arr[new_y][new_x] == '|':
            if dx == 0:
                next.append((new_y, new_x, dy, dx))
            else:
                next.append((new_y, new_x, -1, 0))
                next.append((new_y, new_x, 1, 0))
        elif arr[new_y][new_x] == '-':
            if dy == 0:
                next.append((new_y, new_x, dy, dx))
            else:
                next.append((new_y, new_x, 0, -1))
                next.append((new_y, new_x, 0, 1))
        elif arr[new_y][new_x] == '\\':
            if dx == 0:
                if dy == -1:
                    next.append((new_y, new_x, 0, -1))
                else:
                    next.append((new_y, new_x, 0, 1))
            else:
                if dx == -1:
                    next.append((new_y, new_x, -1, 0))
                else:
                    next.append((new_y, new_x, 1, 0))
        elif arr[new_y][new_x] == '/':
            if dx == 0:
                if dy == -1:
                    next.append((new_y, new_x, 0, 1))
                else:
                    next.append((new_y, new_x, 0, -1))
            else:
                if dx == -1:
                    next.append((new_y, new_x, 1, 0))
                else:
                    next.append((new_y, new_x, -1, 0))

    return len(res) - 1

def part2(arr):
    res = 0

    m, n = len(arr), len(arr[0])
    starts = []
    for i in range(m):
        starts.append((i, -1, 0, 1))
        starts.append((i, n, 0, -1))
    for i in range(n):
        starts.append((-1, i, 1, 0))
        starts.append((m, i, -1, 0))

    for start in starts:
        visited = set()
        res_set = set()
        next = []
        next.append(start)
        while next:
            curr = next.pop()
            if curr in visited:
                continue
            visited.add(curr)
            y, x, dy, dx = curr
            res_set.add((y, x))
            new_y, new_x = y + dy, x + dx
            if new_y < 0 or new_y >= len(arr) or new_x < 0 or new_x >= len(arr[0]):
                continue
            if arr[new_y][new_x] == '.':
                next.append((new_y, new_x, dy, dx))
            elif arr[new_y][new_x] == '|':
                if dx == 0:
                    next.append((new_y, new_x, dy, dx))
                else:
                    next.append((new_y, new_x, -1, 0))
                    next.append((new_y, new_x, 1, 0))
            elif arr[new_y][new_x] == '-':
                if dy == 0:
                    next.append((new_y, new_x, dy, dx))
                else:
                    next.append((new_y, new_x, 0, -1))
                    next.append((new_y, new_x, 0, 1))
            elif arr[new_y][new_x] == '\\':
                if dx == 0:
                    if dy == -1:
                        next.append((new_y, new_x, 0, -1))
                    else:
                        next.append((new_y, new_x, 0, 1))
                else:
                    if dx == -1:
                        next.append((new_y, new_x, -1, 0))
                    else:
                        next.append((new_y, new_x, 1, 0))
            elif arr[new_y][new_x] == '/':
                if dx == 0:
                    if dy == -1:
                        next.append((new_y, new_x, 0, 1))
                    else:
                        next.append((new_y, new_x, 0, -1))
                else:
                    if dx == -1:
                        next.append((new_y, new_x, 1, 0))
                    else:
                        next.append((new_y, new_x, -1, 0))
        res = max(res, len(res_set))
    return res - 1

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
