def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    within_range = all(1 <= abs(diff) <= 3 for diff in differences)

    return (all_increasing or all_decreasing) and within_range

def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if is_safe(temp_report):
            return True

    return False

def count_safe_reports_with_dampener(reports):
    return sum(1 for report in reports if is_safe_with_dampener(report))

def main():
    with open("../input.txt", "r") as f:
        lines = f.readlines()

    reports = [list(map(int, line.split())) for line in lines]

    safe_count = count_safe_reports_with_dampener(reports)
    print(f"Number of safe reports with dampener: {safe_count}")

if __name__ == "__main__":
    main()