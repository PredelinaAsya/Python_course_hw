import typing as tp


def find_peak_index(nums: tp.Sequence[int]) -> int:
    """
    Find `peak` value in sequence and return its index. Peak means that both
    neighbours are less or equals to value.
    :param nums: sequence of integers
    :return: index of peak value
    """
    left = 0
    right = len(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if mid + 1 < right:
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid + 1
        else:
            if nums[left] >= nums[mid]:
                return left
            else:
                return mid
    return left
