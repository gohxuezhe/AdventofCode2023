from collections import defaultdict

def part1(workflows, ratings):
    res = 0

    workflows_dict = {}
    for workflow in workflows.split('\n'):
        open_bracket, close_bracket = workflow.index('{'), workflow.index('}')
        workflow_id = workflow[:open_bracket]
        workflow_rules = workflow[open_bracket+1:close_bracket].split(',')
        workflow_rules_list = []
        for rule in workflow_rules:
            if ':' in rule:
                condition, result = rule.split(':')
                workflow_rules_list.append([condition, result])
            else:
                workflow_rules_list.append([rule])
        workflows_dict[workflow_id] = workflow_rules_list

    for rating in ratings.split('\n'):
        rating = rating[1:-1]
        rating_dict = {}
        for part_rating in rating.split(','):
            category, value = part_rating.split('=')
            rating_dict[category] = int(value)
        curr = "in"
        while curr != "R" and curr != "A":
            rules = workflows_dict[curr]
            for rule, next in rules[:-1]:
                category = rule[0]
                condition = rule[1]
                value = int(rule[2:])
                if condition == '>':
                    if rating_dict[category] > value:
                        curr = next
                        break
                elif condition == '<':
                    if rating_dict[category] < value:
                        curr = next
                        break
            else:
                curr = rules[-1][0]
        if curr == "A":
            for values in rating_dict.values():
                res += int(values)

    return res

### Credit: https://topaz.github.io/paste/#XQAAAQDhBwAAAAAAAAAzHIoib6qqOe07MhJ0XsXE6K08G4Ps1pPQpVZBxq2AayIAGsPQ2ItRWBwwhmAzNBqJd0hNca6gN/1oXMcF0Fnh+0xak9BBHU+wetlSB20RlUuwpHTa5r0nQ/MLZUiNlfQ4fFMpVQmp9VjyBC+6KWukPZ9qq7gVbboN6j2bhc75o8nqL76FdTkQ4cn6yFrqF49JQVXpyXuNf+GPPF8QJizqYC2x/e0NMnmzkHfBAqoXBT85ogJ3yuN++/CRq46AJ5qHWn/0UHbASBJAqdWmDKxuCUnAHI9jzhrAuOFZDpha6eeLLPbsBUalowW9JnyXJ0JzLBK0fktnFEZRcZJLVSTx3lNkE/1ex/LWgGc1mQvh91DBQVBi6QumbkMd2WYyy+R1ImweCGKSPwKBIfhyrmqiYpvu8OaiULHXHi5rdnkobgb9rTadb4BPYc7F376+U6NlOjLbX3e95jOVItyijaQ3FjDngAnfE0O2hr6djRbBiPYOaiNKr0napKYY2j1bHO/x+66T43eUUdvZDHHJlDbCsCQjHefxAeZihtDE2Lpb7e5gpQA7WIe7RI06VIRvFMECROizh7Ia04a+t4AjKhHdtKcEmRgGLakVtUoGYCDgtZQYs2jjfVHkUT4iX/13kaXY6nNbFnxFu7v18s8+tm0a8fPTsUqpKB5DkeBhCedOkXMmgYOmMb1AmE3E6bPtJ2emt2BulzwxjSgKIThPhC9MWHAw85szbjX7aUnvbLQnezBEnIWbykjke0O8cQz1OyYsdSrRamnMJLGUUhY3DP+YPVDGrv1ErMlX8eR+EiS7IvSTP/2KZtnazzTntDAZuxUJhDzFnLDpB986oZwCTCqqynhDbwOxDOB1DAHLU7uLyCASqNLo6EFxVdGvyUUHpYJTQgQMYRRhBOGYgLmOiYPv1ZRCsr2Ycel3IW3wk/yaW/ZNVBaASPS+ia2TrucFy9b1dYDrdmJubZ3/xAeGdw==
def part2(arr):
    res = 0

    workflows_dict = {}
    for workflow in arr.split('\n'):
        open_bracket, close_bracket = workflow.index('{'), workflow.index('}')
        workflow_id = workflow[:open_bracket]
        workflow_rules = workflow[open_bracket+1:close_bracket].split(',')
        workflow_rules = [wf_r.split(":") for wf_r in workflow_rules[:-1]] + [workflow_rules[-1]]
        workflow_rules = [(cond[0], cond[1], int(cond[2:]), final) for cond, final in workflow_rules[:-1]] + [workflow_rules[-1]]
        workflows_dict[workflow_id] = [*workflow_rules[:-1], (None, None, None, workflow_rules[-1])]

    next = [{
        "state": "in",
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000)
    }]
    while next:
        curr = next.pop()
        state = curr["state"]
        if state == "R":
            continue
        elif state == "A":
            curr_total = 1
            for char in "xmas":
                curr_total *= curr[char][1] - curr[char][0] + 1
            res += curr_total
        else:
            for char, cond, bound, rule in workflows_dict[state]:
                split = dict(curr)
                split["state"] = rule
                if cond == "<":
                    split[char] = (split[char][0], bound-1)
                    curr[char] = (bound, curr[char][1])
                elif cond == ">":
                    split[char] = (bound+1, split[char][1])
                    curr[char] = (curr[char][0], bound)
                next.append(split)
        
    return res

if __name__ == "__main__":
    with open('Input.txt', 'r') as file:
        content = file.read()
        workflows, ratings = content.split('\n\n')
        print("Part 1:", part1(workflows, ratings))
        print("Part 2:", part2(workflows))
