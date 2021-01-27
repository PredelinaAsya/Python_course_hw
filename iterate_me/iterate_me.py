import typing as tp


def get_squares(elements: tp.List[int]) -> tp.List[int]:
    """
    :param elements: list with integer values
    :return: list with squared values
    """
    arr = []
    for value in elements:
        arr.append(value * value)
    return arr


# ====================================================================================================


def get_indices_from_one(elements: tp.List[int]) -> tp.List[int]:
    """
    :param elements: list with integer values
    :return: list with indices started from 1
    """
    arr = []
    i = 1
    while i <= len(elements):
        arr.append(i)
        i += 1
    return arr

# ====================================================================================================


def get_max_element_index(elements: tp.List[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of maximum element if exists, None otherwise
    """
    if not elements:
        return None
    max_value = max(elements)
    for i, value in enumerate(elements):
        if value == max_value:
            return i

# ====================================================================================================


def get_every_second_element(elements: tp.List[int]) -> tp.List[int]:
    """
    :param elements: list with integer values
    :return: list with each second element of list
    """
    arr = []
    for i, value in enumerate(elements):
        if i % 2 == 1:
            arr.append(value)
    return arr

# ====================================================================================================


def get_first_three_index(elements: tp.List[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of first "3" in the list if exists, None otherwise
    """
    for i, value in enumerate(elements):
        if value == 3:
            return i
    return None

# ====================================================================================================


def get_last_three_index(elements: tp.List[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of last "3" in the list if exists, None otherwise
    """
    n = len(elements)
    for i in range(n - 1, -1, -1):
        if elements[i] == 3:
            return i
    return None
