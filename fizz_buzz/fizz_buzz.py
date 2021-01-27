import typing as tp


def get_fizz_buzz(n: int) -> tp.List[tp.Union[int, str]]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 -  "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    arr = []
    for value in range(1, n + 1):
        if value % 15 == 0:
            arr.append("FizzBuzz")
        elif value % 3 == 0:
            arr.append("Fizz")
        elif value % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(value)
    return arr
