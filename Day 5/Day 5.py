import sys
from functools import reduce

### Credit: https://topaz.github.io/paste/#XQAAAQC4AwAAAAAAAAA5mWzIdkeB3YAaFzvndN+LqCZhkL+YJtr++JeuPCpp7fxlnbBaB4dZQGuOmX73Qjw5CE9+deVMOb4jP/Xw1FZpFYdeR7AXmGyhVlmyJYdzT+9u0bbzBbcRcr3K+kWrkNxsqwVwnC26G4zs4+t5pSg7vXlkWYALNHP/F8aG4yhYz6TkhEoY1zR3gzHfubbCw2JXPrPZzrHuOiEiyCWvzXR0dF4pYTN09kWF1ymgnQDGJ3BleiMcbJH4sUXzmtyayvGq0LyhK/FKS6rC6c8CfA2biK3tWo3B6cX67tCOp3RixETsmjvJjs/mPoeSoqMnu3V7EGxGib8m8PK7nJ60gW4Iy9M2hKwNuwx7if80RqFNie67Z9HXUuXNy+0HCW0oDcFUu6J4Ht4oDNyxYuuAl7ocTz4A4SDwKgJsyza1g72jHAsFGwkOMImDsB9ktQ+svRQqB2VRiDrU+iEReRVZqnOfqoyApVAhahiaEQjgVUJvzciGovxrKFO4P3HHHQHQ9ihgjG+txn6amcc0e27ooRZphM+/Gn9eOZ/ao2W66OcwNhpECRQK/TkIkw==

def main1(seeds, maps):
    def mapping(seed, _map):
        for output_start, input_start, length in _map:
            if input_start <= seed <= input_start + length:
                return output_start + seed - input_start
        return seed
    return min(reduce(mapping, maps, seed) for seed in seeds)

def main2(seeds, maps):
    start_lengths = list(zip(seeds[::2], seeds[1::2]))
    
    for m in maps:
        new_start_lengths = []
        for seed_start, seed_length in start_lengths:
            for output_start, input_start, map_length in m:
                if seed_start < input_start + map_length and input_start < seed_start + seed_length:
                    new_start = max(seed_start, input_start)
                    new_length = min(seed_start + seed_length, input_start + map_length) - new_start
                    new_start_lengths.append((new_start - input_start + output_start, new_length))
                    if new_start > seed_start:
                        start_lengths += [(seed_start, new_start - seed_start)]
                    if new_start + new_length < seed_start + seed_length:
                        start_lengths.append((new_start + new_length, seed_start + seed_length - new_start - new_length))
                    break
            else:
                new_start_lengths.append((seed_start, seed_length))
        start_lengths = new_start_lengths
    return (min(r for r, _ in start_lengths))

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            seeds, *maps = content.split('\n\n')
            seeds = [int(seed) for seed in seeds.split()[1:]]
            maps = [[[int(i) for i in line.split()] for line in map.splitlines()[1:]] for map in maps]
            print("Part 1:", main1(seeds, maps))
            print("Part 2:", main2(seeds, maps))
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
