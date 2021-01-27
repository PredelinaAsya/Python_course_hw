import typing as tp


def find_value(nums: tp.Sequence[int], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    if len(nums) == 0:
        return False
    left = 0
    right = len(nums)
    while right - left > 1:
        m = (left + right) // 2
        if nums[m] <= value:
            left = m
        else:
            right = m
    if nums[left] == value:
        return True
    else:
        return False
