import re

def part1(arr):
    res = 0

    dish = [''.join([arr[i][j] for i in range(len(arr))]) for j in range(len(arr[0]))]
    max_load = len(dish[0])

    for lane in dish:
        track, seek = 0, 0
        while seek < max_load:
            if lane[seek] == 'O':
                res += max_load - track
                track += 1
            elif lane[seek] == '#':
                track = seek + 1
            seek += 1

    return res

### Credit: https://www.reddit.com/r/adventofcode/comments/18i0xtn/comment/kdb0h11/?utm_source=share&utm_medium=web2x&context=3

def rotate(rocks):
    return tuple(''.join(rocks[y][x] for y in range(len(rocks) - 1, -1, -1))
                 for x in range(len(rocks[0])))

def roll(rocks):
    for row in rocks:
        subs = 1
        while subs:
            row, subs = re.subn(r'(\.+)(O+)', r'\2\1', row)
        yield row

def load(rocks):
    return sum((len(rocks) - y) * row.count('O') for y, row in enumerate(rocks))

def cycle(rocks, n):
    rocks = rotate(rotate(rotate(rocks)))
    seen = {rocks: 0}
    for i in range(1, n + 1):
        for _ in range(4):
            rocks = rotate(tuple(roll(rocks)))
        phase = i - seen.setdefault(rocks, i)
        if phase:
            return cycle(rotate(rocks), (n - i) % phase)
    return rotate(rocks)

def part2(arr):
    return load(cycle(arr, 1000000000))

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
