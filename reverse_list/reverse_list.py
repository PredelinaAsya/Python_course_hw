import typing as tp


def reverse(a: tp.Sequence[int]) -> tp.List[int]:
    """
    Return reversed list. You can use only iteration
    :param a: input list
    :return: reversed list
    """
    n = len(a)
    arr = []
    for i in range(n - 1, -1, -1):
        arr.append(a[i])
    return arr


def reverse_inplace(a: tp.MutableSequence[int]) -> None:
    """
    Revert list inplace. You can use only iteration
    :param a: input list
    :return: None
    """
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    return
