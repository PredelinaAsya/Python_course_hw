# type: ignore
# flake8: noqa


def f0():
    return None
    pass


def f1():
    a = 0
    return a
    pass


def f2():
    a = 0
    print(a)
    return None
    pass


def f3():
    a = 0
    a += 1
    print(a)
    return None
    pass


def f4():
    return range(10)
    pass


def f5():
    for i in range(10):
        print(i)
    return None
    pass


def f6():
    a = 0
    for i in range(10):
        a += 1
    print(a)
    return None
    pass


def f7():
    return [1, *(2, 3), 4]
    pass


def f8():
    x, y = (1, 2)
    return None
    pass


def f9():
    if 1 == 1:
        return 1
    return 2
    pass


def f10():
    for i in range(10):
        if i == 3:
            break
    return None
    pass


def f11():
    list_ = [1, 2, 3]
    dict_ = {'a': 1, 'b': 2}
    return (list_, dict_)
    pass


def f12():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    return a + (b * c) / (d ** e)
    pass
