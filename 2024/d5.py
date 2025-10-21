from typing import Sequence
import sys

def is_correctly_ordered(update: Sequence[int], rules: dict[int, list[int]]) -> bool:
    for i, first in enumerate(update):
        for second in update[i + 1:]:
            # If there is no rule for 'second' then accept
            if second in rules and first in rules[second]:
                return False
    
    return True


if __name__ == "__main__":
    filename = sys.argv[1].strip()
    with open(filename) as f:
        data = f.read().strip()

    ordering_rules, updates = data.split("\n\n")
    ordering_rules = [tuple(map(int, s.strip().split("|"))) for s in ordering_rules.splitlines()]
    rule_map = {}
    for n1, n2 in ordering_rules:
        if n1 in rule_map:
            rule_map[n1].append(n2)
        else:
            rule_map[n1] = [n2]

    updates = [tuple(map(int, u.split(","))) for u in updates.splitlines()]

    total = 0
    for u in updates:
        if is_correctly_ordered(u, rule_map):
           print("CORRECT", u)
           total += u[len(u) // 2]


    print(total)