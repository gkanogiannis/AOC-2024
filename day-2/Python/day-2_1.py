def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    within_range = all(1 <= abs(diff) <= 3 for diff in differences)

    return (all_increasing or all_decreasing) and within_range

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe(report))

def main():
    with open("../input.txt", "r") as f:
        lines = f.readlines()

    reports = [list(map(int, line.split())) for line in lines]

    safe_count = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_count}")

if __name__ == "__main__":
    main()