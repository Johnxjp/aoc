from functools import cmp_to_key
from typing import Sequence
import sys


def is_correctly_ordered(update: Sequence[int], rules: dict[int, list[int]]) -> bool:
    for i, first in enumerate(update):
        for second in update[i + 1 :]:
            # If there is no rule for 'second' then accept
            if second in rules and first in rules[second]:
                return False

    return True


class OrderedItems:

    def __init__(self, item: int, rules: dict[int, list[int]]):
        """Rules are common across all ordered items"""
        self.item = item
        self.rules = rules

    def __eq__(self, other):
        """There is no equal"""
        return False

    def __lt__(self, other: "OrderedItems"):
        """Less than, means should appear first which means other should be in list of values"""
        # If item not in rules, then either rule doesn't exist or greater than or equal
        # print(self.item, other.item, self.rules)
        return self.item in self.rules and other.item in self.rules[self.item]

    def __gt__(self, other: "OrderedItems"):
        """item is in the list of values belonging to key other."""
        # print(self.item, other.item, self.rules)
        return other.item in self.rules and self.item in self.rules[other.item]

    def __hash__(self):
        return self.item


class OrderedItems:

    def __init__(self, item: int, rules: dict[int, list[int]]):
        """Rules are common across all ordered items"""
        self.item = item
        self.rules = rules

    def __eq__(self, other):
        """There is no equal"""
        return False

    def __lt__(self, other: "OrderedItems"):
        """Less than, means should appear first which means other should be in list of values"""
        # If item not in rules, then either rule doesn't exist or greater than or equal
        # print(self.item, other.item, self.rules)
        return self.item in self.rules and other.item in self.rules[self.item]

    def __gt__(self, other: "OrderedItems"):
        """item is in the list of values belonging to key other."""
        # print(self.item, other.item, self.rules)
        return other.item in self.rules and self.item in self.rules[other.item]

    def __hash__(self):
        return self.item


class OrderedArray:
    """Custom array that compares elements based on ordering rules"""

    def __init__(self, items: list[int], rules: dict[int, list[int]]):
        """
        Initialize the ordered array with items and comparison rules.

        Args:
            items: List of integers to store
            rules: Dictionary where key > all values in its list
        """
        self.items = items
        self.rules = rules

    def _compare(self, a: int, b: int) -> int:
        """
        Compare two items based on the rules.

        Returns:
            -1 if a < b (a should come before b)
             1 if a > b (a should come after b)
             0 if no ordering defined
        """
        # Check if b is in the list of items less than a
        if a in self.rules and b in self.rules[a]:
            return 1  # a > b

        # Check if a is in the list of items less than b
        if b in self.rules and a in self.rules[b]:
            return -1  # a < b

        # No direct ordering defined
        return 0

    def sort(self) -> None:
        """Sort the array in-place using the custom comparison rules"""
        self.items.sort(key=cmp_to_key(self._compare))

    def sorted(self) -> "OrderedArray":
        """Return a new sorted OrderedArray"""
        new_array = OrderedArray([x for x in self.items], self.rules)
        new_array.sort()
        return new_array

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        """Make the array iterable"""
        return iter(self.items)


def correct_update(update: Sequence[int], rules: dict[int, list[int]]) -> list[int]:
    """This is a sorting algorithm but with rules. The check for greater or less than is based on rule ordering"""
    update_custom = OrderedArray(update, rules)
    return update_custom.sorted().items


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

    # PART 1

    total_p1 = 0
    incorrect_updates = []
    for u in updates:
        if is_correctly_ordered(u, rule_map):
            print("CORRECT", u)
            total_p1 += u[len(u) // 2]
        else:
            incorrect_updates.append(u)

    # PART 2

    total_p2 = 0
    for u in incorrect_updates:
        u_correct = correct_update(u, rule_map)
        print(u, " CORRECTED TO ", u_correct)
        total_p2 += u_correct[len(u) // 2]

    print(total_p1, total_p2)
