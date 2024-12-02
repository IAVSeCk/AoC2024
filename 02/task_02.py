from typing import List, Tuple


def read_rows() -> List[List[int]]:
    file_numbers = open("input")
    all_lines = file_numbers.readlines()

    rows = []
    for line in all_lines:
        row_str = line.split(" ")
        row = []
        for number in row_str:
            row.append(int(number))
        rows.append(row)

    return rows


def is_safe(row: List[int]) -> bool:
    increasing = row[0] < row[1]
    factor = -1 if increasing else 1
    is_correct = True
    for i in range(1, len(row)):
        product = (row[i - 1] - row[i]) * factor
        if product < 1 or product > 3:
            is_correct = False
            break
    return is_correct


def part_one(rows: List[List[int]]) -> int:
    found = 0

    for row in rows:
        is_correct = is_safe(row)
        if is_correct:
            found += 1

    return found


def part_two(rows: List[List[int]]) -> int:
    found = 0

    for row in rows:
        if is_safe(row):
            found += 1
        else:
            for i in range(0, len(row)):
                level_removed_row = row[0:i] + row[i+1:]
                if is_safe(level_removed_row):
                    found += 1
                    break

    return found


def main():
    rows = read_rows()
    # rows = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]
    solution_one = part_one(rows)
    solution_two = part_two(rows)

    print(solution_one)
    print(solution_two)
    print(rows)


if __name__ == '__main__':
    main()
