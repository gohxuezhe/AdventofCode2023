from collections import defaultdict
import re

def part1(arr):
    res = 0

    for step in arr:
        curr_res = 0
        for char in step:
            curr_res += ord(char)
            curr_res *= 17
            curr_res %= 256
        res += curr_res

    return res

def part2(arr):
    res = 0

    boxes = defaultdict(list)

    for step in arr:
        label = re.search('[a-zA-Z]+', step).group(0)
        box = 0
        for char in label:
            box += ord(char)
            box *= 17
            box %= 256

        num_exist = re.search('[0-9]+', step)
        if num_exist:
            num = int(num_exist.group(0))
            for lens in range(len(boxes[box])):
                if boxes[box][lens][0] == label:
                    boxes[box][lens][1] = num
                    break
            else:
                boxes[box].append([label, num])
        else:
            for lens in range(len(boxes[box])):
                if boxes[box][lens][0] == label:
                    boxes[box].pop(lens)
                    break
    
    for box, lenses in boxes.items():
        if lenses:
            for slot, lens in enumerate(lenses):
                _, focal_length = lens
                res += (box + 1) * (slot + 1) * focal_length

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split(',')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
