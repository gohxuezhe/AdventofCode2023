import re

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

num_to_dir = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

def part1(arr):
    curr = (0, 0)
    loop = [curr]
    for line in arr:
        dir, steps, _ = line.split(' ')
        for _ in range(int(steps)):
            curr = (curr[0] + directions[dir][0], curr[1] + directions[dir][1])
            loop.append(curr)

    padded_points = [*loop, loop[0]]
    interior_area = sum(row1 * col2 - row2 * col1 for (row1, col1), (row2, col2) in zip(padded_points,padded_points[1:]))/ 2
    return int(abs(interior_area) - 0.5 * len(loop) + 1) + len(loop)

def part2(arr):
    curr = (0, 0)
    loop = [curr]
    total_parameter_points = 0
    for line in arr:
        _, _, hex_code = line.split(' ')
        hex_code = re.search(r'#(\w{6})', hex_code).group(1)
        distance_in_hex, dir_num = hex_code[:-1], hex_code[-1]
        distance_in_meters = int(distance_in_hex, 16)
        curr = (curr[0] + directions[num_to_dir[dir_num]][0] * distance_in_meters, curr[1] + directions[num_to_dir[dir_num]][1] * distance_in_meters)
        loop.append(curr)
        total_parameter_points += distance_in_meters

    padded_points = [*loop, loop[0]]
    interior_area = sum(row1 * col2 - row2 * col1 for (row1, col1), (row2, col2) in zip(padded_points,padded_points[1:]))/ 2
    return int(abs(interior_area) - 0.5 * total_parameter_points + 1) + total_parameter_points

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
