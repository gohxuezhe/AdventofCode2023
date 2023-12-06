import sys

def main1(arr):
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

def main2(arr):
    res = 0

    times = int(''.join([time for time, _ in arr]))
    distances = int(''.join([distance for _, distance in arr]))

    for i in range(times):
        if distances <= i * (times - i):
            res += 1

    return res

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            times, distances = content.split('\n')
            times = times.split()[1:]
            distances = distances.split()[1:]
            content = list(zip(times, distances))
            print("Part 1:", main1(content))
            print("Part 2:", main2(content))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
    else:
        file_path = sys.argv[1]
        read_file(file_path)
