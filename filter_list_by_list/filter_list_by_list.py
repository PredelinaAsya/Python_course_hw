import typing as tp


def filter_list_by_list(a: tp.Sequence[int], b: tp.Sequence[int]) \
        -> tp.List[int]:
    """
    Filter first sorted lists by other sorted list
    :param a: first sorted list
    :param b: second sorted list
    :return: filtered sorted list
    """
    arr = []
    p1 = 0
    p2 = 0
    while p1 < len(a) and p2 < len(b):
        if a[p1] < b[p2]:
            arr.append(a[p1])
            p1 += 1
        elif a[p1] == b[p2]:
            p1 += 1
        else:
            p2 += 1
    else:
        while p1 < len(a):
            arr.append(a[p1])
            p1 += 1
    return arr
