import typing as tp


def revert(dct: tp.Mapping[str, str]) -> tp.Dict[str, tp.List[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    new_dct = {}
    for k, v in dct.items():
        if v in new_dct:
            new_dct[v].append(k)
        else:
            new_dct.update({v: [k]})
    return new_dct
