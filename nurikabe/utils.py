from typing import Tuple, Any


def if_mathematically_reachable(
        initial_coordinate: int,
        coordinate_to_reach: int,
        number_of_steps: int) -> int:
    '''Возвращает True - если в теории есть возможность
    достичь из иходной точки до нужной, иначе False.'''
    minimum_steps = (abs(initial_coordinate[0]-coordinate_to_reach[0]) +
                     abs(initial_coordinate[1]-coordinate_to_reach[1]))
    if minimum_steps > number_of_steps:
        return False
    return True


def find_neighbour_fields(
        field_row: int,
        field_column: int,
        size: int) -> Tuple[Any]:
    '''Возвращает координаты соседних полей по вертикали и горизонтали.'''
    answer: list[Tuple[int]] = [(field_row-1, field_column),
                                (field_row, field_column+1),
                                (field_row+1, field_column),
                                (field_row, field_column-1)]
    for ind in range(4):
        if (answer[ind][0] < 0 or answer[ind][1] < 0 or
                answer[ind][0] > (size-1) or answer[ind][1] > (size-1)):
            answer[ind] = None

    return tuple(answer)


def find_diagonal_neighbours(
        field_row: int,
        field_column: int,
        size: int) -> Tuple[Any]:
    '''Возвращает координаты соседних полей по диагонали.'''
    answer: list[Tuple[int]] = [(field_row-1, field_column+1),
                                (field_row+1, field_column+1),
                                (field_row+1, field_column-1),
                                (field_row-1, field_column-1)]
    for ind in range(4):
        if (answer[ind][0] < 0 or answer[ind][1] < 0 or
                answer[ind][0] > (size-1) or answer[ind][1] > (size-1)):
            answer[ind] = None
    return tuple(answer)
