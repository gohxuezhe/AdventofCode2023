def part1(arr):
    res = 1

    times = [int(time) for time, _ in arr]
    distances = [int(distance) for _, distance in arr]
    
    for time, distance in list(zip(times, distances)):
        curr = 0
        for i in range(time):
            if distance <= i * (time - i):
                curr += 1
        res *= curr

    return res

def part2(arr):
    res = 0

    times = int(''.join([time for time, _ in arr]))
    distances = int(''.join([distance for _, distance in arr]))

    for i in range(times):
        if distances <= i * (times - i):
            res += 1

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        times, distances = content.split('\n')
        times = times.split()[1:]
        distances = distances.split()[1:]
        content = list(zip(times, distances))
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
