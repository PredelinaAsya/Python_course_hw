import typing as tp


def find_min(nums: tp.Sequence[int]) -> int:
    """
    Find minimum in rotated not empty sorted sequence without dublicates.
    :param nums: sequence of integer
    :return: minimum value
    """
    if nums[0] <= nums[len(nums) - 1]:
        return nums[0]
    left = -1
    right = len(nums) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if mid != 0 and mid != len(nums) - 1:
            if nums[mid] >= nums[0]:
                left = mid
            else:
                right = mid
        elif mid == 0:
            left = mid
        else:
            right = mid
    return nums[right]
