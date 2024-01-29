def part1(arr):
    empty_rows = {i for i in range(len(arr))}
    empty_cols = {i for i in range(len(arr[0]))}
    galaxies = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '.':
                if j in empty_cols:
                    empty_cols.remove(j)
                if i in empty_rows:
                    empty_rows.remove(i)
                galaxies.append((i, j))

    res = 0
    for i in range(len(galaxies) - 1):
        for j in range(i+1, len(galaxies)):
            res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            for row in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
                if row in empty_rows:
                    res += 1
            for col in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])):
                if col in empty_cols:
                    res += 1

    return res

def part2(arr):
    empty_rows = {i for i in range(len(arr))}
    empty_cols = {i for i in range(len(arr[0]))}
    galaxies = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '.':
                if j in empty_cols:
                    empty_cols.remove(j)
                if i in empty_rows:
                    empty_rows.remove(i)
                galaxies.append((i, j))

    res = 0
    for i in range(len(galaxies) - 1):
        for j in range(i+1, len(galaxies)):
            res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            for row in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
                if row in empty_rows:
                    res += 1000000 - 1
            for col in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])):
                if col in empty_cols:
                    res += 1000000 - 1

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
