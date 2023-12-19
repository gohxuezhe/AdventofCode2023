from heapq import heappush, heappop

### Credit: https://topaz.github.io/paste/#XQAAAQAxBwAAAAAAAAAzHIoib6py7i/yVWhl9dSCjkM4F45bQbz+k/Gd/0xMj5/xvVMJEQzYHtN76/o3jYVK2PaE7+fl0gIJsFXqMzyfAj8D+6zmr8Sv9ctB4QMbFKvWCgX5OjofFkx07bR4ev6DDKYyPUExYhQxVHV0GxDwienDB9e/VwygG99BtKbBkol093sWGg5mYq7pe64Co/Gad2I7XvOYekKHZhOzHNeEBSHiIOUpIIuCjBZ5PmwCnjruhfMIecqmVgpCT9hfjqdVJbmyDbD29ST4d8f/3ObyBDAyu4egGSJ1ZpcFa6iL5GTRRHIzzpjPU4LMXwR8glmPhKk3oq/KLdHRz9xIzX0pT8rNIYhSwE+twYZ59gUg61pvpOTSLwK3XqdN8wwmj6lTviSKvlA73reDTDpvGsyoLIYcI3NSoL+SS62OTRA7Yji9HSEppcGaCzJyd8Maco7kjGil5K/IGe42fEciYArjoBkSjdSpulXY/ndb/WSHB3ildN4vGwl3sotRr9ZDtYbPpuPBnXh1/WKhSJOyACfHrhjccPmhdQTatCqdc0ndhimC211vus/ChfLuFdA1Go6Y5W7RYjpTYGepKuBsI98H9zFwnKyFfJtU3kjvs6PajECMEBIO0jREdiJ2q+95irpl6oihbBQkaiKyjcWJHCm7iBQDNXKM0PHYrJKBUpOf0NxX3fLgUSXDQvVgojemAn35BGwsWZwsCB6aza1w4XQsu57vicGx8/3ASioYquhtVW8G+SRkgiCC4A4RAgCQ/wrz3VWYKb9jKYhkLQLvcxmRTaqUXpmZFkqgSHaNJMJ2iz991n09tc33ebIiIhtYdBKReNRtGz+2XE9oGCFSs4KgkKukUDNNUOKY60ILGC7ADg6jLk0h/AyYfkTtEBsnOSP/+ZJNGg==

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def part1(arr):
    res = 0

    start = (0, 0)
    end = (len(arr[0]) - 1, len(arr) - 1)
    heap = [(0, start, (0, 0))]
    costs = {(start, (0, 0)): 0}
    visited = set()

    while heap:
        cost, coord, dir = heappop(heap)
        if coord == end:
            res = cost
            break
        if (coord, dir) in visited:
            continue
        visited.add((coord, dir))

        for new_dir in moves:
            if (abs(new_dir[0]) == abs(dir[0]) and abs(new_dir[1]) == abs(dir[1])):
                continue

            new_cost = cost
            for step in range(1, 4):
                new_coord = (coord[0] + step * new_dir[0], coord[1] + step * new_dir[1])
                if new_coord[0] < 0 or new_coord[0] >= len(arr) or new_coord[1] < 0 or new_coord[1] >= len(arr[0]):
                    continue
                new_cost += int(arr[new_coord[0]][new_coord[1]])
                if costs.get((new_coord, new_dir), float('inf')) <= new_cost:
                    continue
                costs[(new_coord, new_dir)] = new_cost
                heappush(heap, (new_cost, new_coord, new_dir))

    return res

def part2(arr):
    res = 0

    start = (0, 0)
    end = (len(arr[0]) - 1, len(arr) - 1)
    heap = [(0, start, (0, 0))]
    costs = {(start, (0, 0)): 0}
    visited = set()

    while heap:
        cost, coord, dir = heappop(heap)
        if coord == end:
            res = cost
            break
        if (coord, dir) in visited:
            continue
        visited.add((coord, dir))

        for new_dir in moves:
            if (abs(new_dir[0]) == abs(dir[0]) and abs(new_dir[1]) == abs(dir[1])):
                continue

            new_cost = cost
            for step in range(1, 11):
                new_coord = (coord[0] + step * new_dir[0], coord[1] + step * new_dir[1])
                if new_coord[0] < 0 or new_coord[0] >= len(arr) or new_coord[1] < 0 or new_coord[1] >= len(arr[0]):
                    continue
                new_cost += int(arr[new_coord[0]][new_coord[1]])
                if step < 4 or costs.get((new_coord, new_dir), float('inf')) <= new_cost:
                    continue
                costs[(new_coord, new_dir)] = new_cost
                heappush(heap, (new_cost, new_coord, new_dir))

    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        content = content.split('\n')
        print("Part 1:", part1(content))
        print("Part 2:", part2(content))
