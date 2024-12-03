from typing import List

import re


def read_rows() -> List[str]:
    file_numbers = open("input")
    all_lines = file_numbers.readlines()

    return all_lines


def part_one(all_rows: List[str]):
    result = 0
    for row in all_rows:
        found_matches = re.findall("mul\([0-9]+,[0-9]+\)", row)
        for match in found_matches:
            both_numbers = match.replace("mul(", "").replace(")", "").split(",")
            result += (int(both_numbers[0]) * int(both_numbers[1]))
    print(result)


def part_two(all_rows: List[str]):
    result = 0
    merged_str = "".join(all_rows)
    found_matches = re.finditer("mul\([0-9]+,[0-9]+\)", merged_str)
    for match in found_matches:
        previous_dont = merged_str[0:match.start()].rfind("don't()")
        previous_do = merged_str[0:match.start()].rfind("do()")
        if previous_do > previous_dont or previous_dont < 0:
            both_numbers = match.group().replace("mul(", "").replace(")", "").split(",")
            result += (int(both_numbers[0]) * int(both_numbers[1]))
    print(result)


if __name__ == '__main__':
    rows = read_rows()
    part_one(rows)
    part_two(rows)
