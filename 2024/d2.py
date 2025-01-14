from typing import List


def process_file(file: str):
    with open(file) as f:
        reports = [
            [int(a) for a in line.split()] for line in f.read().splitlines()
        ]
    return reports


def is_report_safe(report: List[int]) -> bool:
    if len(report) < 2:
        return True

    is_increasing = None
    min_diff = 1
    max_diff = 3
    for index in range(1, len(report)):
        diff = report[index] - report[index - 1]
        if abs(diff) < min_diff or abs(diff) > max_diff:
            return False

        if diff > 0:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                return False

        else:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                return False

    return True


def d1():
    reports = process_file("d2.txt")
    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    d1()
    # d2()
