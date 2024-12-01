from typing import List, Tuple

import bisect


def read_rows() -> Tuple[List[int], List[int]]:
    file_numbers = open("input")
    all_lines = file_numbers.readlines()

    first_row = []
    second_row = []
    for line in all_lines:
        row = line.split("   ")
        bisect.insort(first_row, int(row[0]))
        bisect.insort(second_row, int(row[1]))

    return first_row, second_row


def part_one(first_row: List[int], second_row: List[int]) -> int:
    diffs = 0

    for i in range(0, len(first_row)):
        diffs += abs(first_row[i] - second_row[i])

    return diffs


def part_two(first_row: List[int], second_row: List[int]) -> int:
    first_row, second_row = read_rows()
    score = 0

    for i in range(0, len(first_row)):
        for j in range(0, len(second_row)):
            if first_row[i] == second_row[j]:
                score += first_row[i]

    return score


def main():
    first_row, second_row = read_rows()
    solution_one = part_one(first_row, second_row)
    solution_two = part_two(first_row, second_row)

    print(solution_one)
    print(solution_two)



if __name__ == '__main__':
    main()
