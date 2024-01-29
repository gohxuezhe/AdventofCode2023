import functools

def part1(arr):
    res = [0]

    def recursion(hot_springs, records, hot_springs_index, records_index):
        if hot_springs_index >= len(hot_springs) and records_index >= len(records):
            res[0] += 1
            return
        if hot_springs_index >= len(hot_springs):
            return
        if records_index >= len(records):
            for i in range(len(hot_springs) - hot_springs_index):
                if hot_springs[hot_springs_index + i] == '#':
                    return
            res[0] += 1
            return
        if hot_springs[hot_springs_index] == '.' or hot_springs[hot_springs_index] == '?':
            recursion(hot_springs, records, hot_springs_index + 1, records_index)
        if hot_springs[hot_springs_index] == '#' or hot_springs[hot_springs_index] == '?':
            for i in range(records[records_index]):
                if hot_springs_index + i >= len(hot_springs) or hot_springs[hot_springs_index + i] == '.':
                    return
            else:
                if (hot_springs_index + records[records_index] < len(hot_springs) and hot_springs[hot_springs_index + records[records_index]] != '#') or hot_springs_index + records[records_index] >= len(hot_springs):
                    recursion(hot_springs, records, hot_springs_index + records[records_index] + 1, records_index + 1)


    for line in arr:
        hot_springs, records = line.split(' ')
        hot_springs = hot_springs
        records = [int(i) for i in records.split(',')]
        
        recursion(hot_springs, records, 0, 0)

    return res[0]

def part2(arr):
    res = 0

    @functools.lru_cache(maxsize=None)
    def recursion(hot_springs, records, hot_springs_index, records_index):
        if hot_springs_index >= len(hot_springs) and records_index >= len(records):
            return 1
        if hot_springs_index >= len(hot_springs):
            return 0
        if records_index >= len(records):
            for i in range(len(hot_springs) - hot_springs_index):
                if hot_springs[hot_springs_index + i] == '#':
                    return 0
            return 1
        curr_res = 0
        if hot_springs[hot_springs_index] == '.' or hot_springs[hot_springs_index] == '?':
            curr_res += recursion(hot_springs, records, hot_springs_index + 1, records_index)
        if hot_springs[hot_springs_index] == '#' or hot_springs[hot_springs_index] == '?':
            for i in range(records[records_index]):
                if hot_springs_index + i >= len(hot_springs) or hot_springs[hot_springs_index + i] == '.':
                    return curr_res
            else:
                if (hot_springs_index + records[records_index] < len(hot_springs) and hot_springs[hot_springs_index + records[records_index]] != '#') or hot_springs_index + records[records_index] >= len(hot_springs):
                    curr_res += recursion(hot_springs, records, hot_springs_index + records[records_index] + 1, records_index + 1)
        return curr_res

    for line in arr:
        hot_springs, records = line.split(' ')
        hot_springs = hot_springs + '?' + hot_springs + '?' + hot_springs + '?' + hot_springs + '?' + hot_springs
        records = tuple([int(i) for i in records.split(',')] * 5)
        
        res += recursion(hot_springs, records, 0, 0)

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
