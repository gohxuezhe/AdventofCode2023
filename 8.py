import math

### Credit: https://github.com/racecraftr/adv_of_code/blob/main/y2023/day8/day8.py

direction_to_index = {
        'L': 0,
        'R': 1,
    }

def part1(instructions, nodes_dict):
    res = 0

    curr_element = 'AAA'
    curr_instruction = 0
    instrunction_length = len(instructions)
    while curr_element != 'ZZZ':
        curr_element = nodes_dict[curr_element][direction_to_index[instructions[curr_instruction]]]
        curr_instruction += 1
        curr_instruction %= instrunction_length
        res += 1

    return res

def part2helper(start, instructions, nodes_dict) -> int:
    steps = 0
    curr = start
    while curr[2] != 'Z':
        curr = nodes_dict[curr][direction_to_index[instructions[steps % len(instructions)]]]
        steps += 1
    return(steps)

def part2(instructions, nodes_dict):
    steps_required = []

    for key in nodes_dict.keys():
        if key[2] == 'A':
            steps_required.append(part2helper(key, instructions, nodes_dict))

    return math.lcm(*steps_required)

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        instructions, nodes = content.split('\n\n')
        nodes = nodes.split('\n')
        nodes = [node.split(' = ') for node in nodes]
        nodes_dict = {}
        for node, left_right in nodes:
            left_right = left_right[1:-1].split(', ')
            nodes_dict[node] = left_right
        print("Part 1:", part1(instructions, nodes_dict))
        print("Part 2:", part2(instructions, nodes_dict))
