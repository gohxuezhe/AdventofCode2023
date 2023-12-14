def find_mirror(pattern):
    for mirror in range(len(pattern) - 1):
        mirror_left, mirror_right = mirror, mirror + 1
        while pattern[mirror_left] == pattern[mirror_right]:
            mirror_left -= 1
            mirror_right += 1
            if mirror_left < 0 or mirror_right >= len(pattern):
                return mirror + 1

def part1(arr):
    res = 0

    for pattern in arr:
        horizontal = pattern.split('\n')
        horizontal_mirror = find_mirror(horizontal)

        vertical = [''.join([horizontal[i][j] for i in range(len(horizontal))]) for j in range(len(horizontal[0]))]
        vertical_mirror = find_mirror(vertical)

        if not horizontal_mirror:
            res += vertical_mirror
        elif not vertical_mirror:
            res += horizontal_mirror * 100

    return res

def find_smudged_mirror(pattern):
    for mirror in range(len(pattern) - 1):
        mirror_left, mirror_right = mirror, mirror + 1
        smudge = 0
        while smudge < 2 and mirror_left >= 0 and mirror_right < len(pattern):
            if pattern[mirror_left] != pattern[mirror_right]:
                for i in range(len(pattern[0])):
                    if pattern[mirror_left][i] != pattern[mirror_right][i]:
                        smudge += 1
            mirror_left -= 1
            mirror_right += 1
        if smudge == 1 and (mirror_left < 0 or mirror_right >= len(pattern)):
            return mirror + 1

def part2(arr):
    res = 0

    for pattern in arr:
        horizontal = pattern.split('\n')
        horizontal_mirror = find_smudged_mirror(horizontal)

        vertical = [''.join([horizontal[i][j] for i in range(len(horizontal))]) for j in range(len(horizontal[0]))]
        vertical_mirror = find_smudged_mirror(vertical)

        if not horizontal_mirror:
            res += vertical_mirror
        elif not vertical_mirror:
            res += horizontal_mirror * 100

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
