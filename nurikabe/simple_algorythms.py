from typing import Any

# from utils import (find_diagonal_neighbours, find_neighbour_fields,
#                    if_mathematically_reachable)


def check_fields_with_one(field: list[list[Any]], size: int) -> list[list[Any]]:
    for coord in neighbours:
    if coord is not None and field[coord[0]][coord[1]] != 'b':
        field[coord[0]][coord[1]] = 'b'
    return field


def look_for_black_square(field, size) -> list[list[Any]]:
    return field
