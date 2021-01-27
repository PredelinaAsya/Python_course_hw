import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> tp.List[tp.Tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts
    as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    ans = []

    def dfs_dict(str_of_keys, dict):
        for k, v in dict.items():
            if type(v) == int:
                ans.append((str_of_keys + k, v))
            else:
                dfs_dict(str_of_keys + k + ".", v)
        return
    dfs_dict(prefix, dct)
    return ans


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: tp.List[tp.Tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts
    as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".",
    value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    def dfs_dict(str_of_keys, dict):
        for k, v in dict.items():
            if type(v) == int:
                result.append((str_of_keys + k, v))
            else:
                dfs_dict(str_of_keys + k + ".", v)
        return
    dfs_dict(prefix, dct)
    return result


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> tp.List[tp.Tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts
    as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    ans = []
    stack = []
    stack.append(("", dct))
    while len(stack) != 0:
        last_index = len(stack) - 1
        current_edge = stack[last_index]
        current_dict = current_edge[1]
        current_str = current_edge[0]
        stack.pop()
        for k, v in current_dict.items():
            if type(v) == int:
                ans.append((current_str + k, v))
            else:
                stack.append((current_str + k + ".", v))
    return ans
