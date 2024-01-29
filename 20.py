from collections import defaultdict, deque
from copy import deepcopy
from math import prod

### Credit: https://github.com/vanam/CodeUnveiled/blob/master/Advent%20Of%20Code%202023/20/main.py

def part1(arr):
    modules = defaultdict(lambda: {"dest": [], "type": None, "val": dict()})
    for line in arr:
        name, destinations = line.strip().split(" -> ")
        t = None
        if name[0] in ["%", "&"]:
            t, name = name[0], name[1:]
        module = modules[name]
        module["dest"] = destinations.split(", ")
        module["type"] = t
        if t == '%':
            module["val"] = 0
        for d in module["dest"]:
            if type(modules[d]["val"]) is dict:
                modules[d]["val"][name] = 0

    pulse_counter = [0, 0]

    for _ in range(1000):
        pulses = deque()
        pulses.append(("button", 0, "broadcaster"))

        while pulses:
            sender, pulse_type, receiver = pulses.popleft()
            pulse_counter[pulse_type] += 1
            if modules[receiver]["type"] == '&':
                modules[receiver]["val"][sender] = pulse_type
                pulse_type = not all(modules[receiver]["val"].values())
            elif modules[receiver]["type"] == '%':
                if pulse_type:
                    continue
                pulse_type = modules[receiver]["val"] = not modules[receiver]["val"]
            for d in modules[receiver]["dest"]:
                pulses.append((receiver, pulse_type, d))

    return pulse_counter[0] * pulse_counter[1]

def part2(arr):
    modules = defaultdict(lambda: {"dest": [], "type": None, "val": dict()})
    for line in arr:
        name, destinations = line.strip().split(" -> ")
        t = None
        if name[0] in ["%", "&"]:
            t, name = name[0], name[1:]
        module = modules[name]
        module["dest"] = destinations.split(", ")
        module["type"] = t
        if t == '%':
            module["val"] = 0
        for d in module["dest"]:
            if type(modules[d]["val"]) is dict:
                modules[d]["val"][name] = 0

    conj_module_cycles = {}
    for i in range(1, 10000):
        pulses = deque()
        pulses.append(("button", 0, "broadcaster"))

        while pulses:
            sender, pulse_type, receiver = pulses.popleft()
            if modules[receiver]["type"] == '&':
                modules[receiver]["val"][sender] = pulse_type
                pulse_type = not all(modules[receiver]["val"].values())
                if not pulse_type and receiver not in conj_module_cycles:
                    conj_module_cycles[receiver] = i
            elif modules[receiver]["type"] == '%':
                if pulse_type:
                    continue
                pulse_type = modules[receiver]["val"] = not modules[receiver]["val"]
            for d in modules[receiver]["dest"]:
                pulses.append((receiver, pulse_type, d))

    return prod(conj_module_cycles.values())

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))