from typing import List, Tuple

import numpy as np
import re


def read_rows() -> List[str]:
    file_numbers = open("input.txt")
    all_lines = file_numbers.readlines()
    all_limes_trim = [line.strip() for line in all_lines]

    return all_limes_trim


def count_horizontal(all_rows: List[str], word: str):
    counter = 0
    for row in all_rows:
        row_reversed = row[::-1]
        counter += row.count(word)
        counter += row_reversed.count(word)

    return counter


def transform_vertical_list_to_horizontal(all_rows) -> List[str]:
    transformed_rows = []
    for i in range(0, len(all_rows[0])):
        row = ""
        for j in range(0, len(all_rows)):
            row += all_rows[j][i]
        transformed_rows.append(row)

    return transformed_rows


def transform_diagonal_list_to_horizontal(all_rows: List[str]) -> List[str]:
    character_list = [list(row) for row in all_rows]
    transformed_rows = []
    for i in range(0, len(all_rows)):
        transformed_rows.append(''.join(np.diagonal(character_list, offset=i)))
        transformed_rows.append(''.join(np.flipud(character_list).diagonal(offset=i)))
        if i > 0:
            transformed_rows.append(''.join(np.diagonal(character_list, offset=-i)))
            transformed_rows.append(''.join(np.flipud(character_list).diagonal(offset=-i)))

    return transformed_rows



def find_word(all_rows: List[str], word: str):
    horizontal = count_horizontal(all_rows, word)

    vertical_list = transform_vertical_list_to_horizontal(all_rows)
    vertical = count_horizontal(vertical_list, word)

    diagonal_list = transform_diagonal_list_to_horizontal(all_rows)
    diagonal = count_horizontal(diagonal_list, word)

    return horizontal + vertical + diagonal


def do_task_02(all_rows: List[str]):
    counter = 0
    for i in range(0, len(all_rows) - 2):
        for j in range(0, len(all_rows) - 2):
            row1 = all_rows[i][j:j + 3]
            row2 = all_rows[i + 1][j:j + 3]
            row3 = all_rows[i + 2][j:j + 3]

            if row2[1] == 'A' and ((row1[0] == 'M' and row3[2] == 'S') or (row1[0] == 'S' and row3[2] == 'M')) and (
                    (row1[2] == 'M' and row3[0] == 'S') or (row1[2] == 'S' and row3[0] == 'M')):
                counter += 1

    return counter


if __name__ == '__main__':
    rows = read_rows()
    # rows = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']
    task_01 = find_word(rows, "XMAS")
    task_02 = do_task_02(rows)
    print(task_01)
    print(task_02)
