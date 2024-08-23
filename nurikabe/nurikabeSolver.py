from typing import Any

from utils import (find_diagonal_neighbours, find_neighbour_fields,
                   if_mathematically_reachable)


def simple_operations(
        field: list[list[int]],
        size: int) -> list[list[Any]]:
    for index_row in range(size):
        for index_col in range(size):
            neigbours = find_neighbour_fields(
                index_row,
                index_col,
                size
            )
            diagonal_neighbours = find_diagonal_neighbours(
                index_row,
                index_col,
                size
            )
            if (isinstance(field[index_row][index_col], int) and
                    field[index_row][index_col] == 0):
                pass

    return field


def advanced_methods(
        field: list[list[int]],
        size: int) -> list[list[Any]]:
    return field


def solve_nurikabe(
        field: list[list[int]],
        size: int) -> list[list[Any]]:
    '''Основная функция решения'''
    iteration = 0
    i_no_change = 0
    while i_no_change > 3:
        if iteration < 3:
            simple_operations(field, size)


def normal_print_answer(list_of_fields, size):
    separator = '----' * size
    print(separator)
    for row in list_of_fields:
        print('|', end='')
        for ffield in row:
            if ffield == 0:
                print('   ', end='')
            elif ffield == 'b':
                print(' B ', end='')
            elif ffield == 'w':
                print(' W ', end='')
            else:
                print(f' {ffield} ', end='')
            print('|', end='')
        print()

        print(separator)


def main() -> None:
    '''Главная функция для вызова'''
    field: list[list[int]] = [
        [0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 3, 0, 0],
        [1, 0, 0, 1, 0, 0, 5, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 1, 0],
    ]
    size: int = len(field[0])
    print("initial task:")
    normal_print_answer(field, size)
    # answer_field: list[list[Any]] = solve_nurikabe(field, size)


if __name__ == '__main__':
    main()
