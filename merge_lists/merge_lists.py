import typing as tp


def merge(a: tp.Sequence[int], b: tp.Sequence[int]) -> tp.List[int]:
    """
    Merge two sorted lists in one sorted list
    :param a: first sorted list
    :param b: second sorted list
    :return: merged sorted list
    """
    arr = []
    p1 = 0
    p2 = 0
    while p1 < len(a) and p2 < len(b):
        if a[p1] <= b[p2]:
            arr.append(a[p1])
            p1 += 1
        else:
            arr.append(b[p2])
            p2 += 1
    else:
        while p1 < len(a):
            arr.append(a[p1])
            p1 += 1
        while p2 < len(b):
            arr.append(b[p2])
            p2 += 1
    return arr
