def part1(arr):
    res = 0

    def recursion(differences):
        if len(set(differences)) == 1:
            return differences[0]
        return differences[-1] + recursion([differences[i] - differences[i-1] for i in range(1, len(differences))])
    
    for line in arr:
        res += recursion([int(i) for i in line.split(' ')])

    return res

def part2(arr):
    res = 0

    def recursion(differences):
        if len(set(differences)) == 1:
            return differences[0]
        return differences[-1] - recursion([differences[i] - differences[i+1] for i in range(len(differences) - 1)])
    
    for line in arr:
        line = [int(i) for i in line.split(' ')][::-1]
        res += recursion(line)
    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
