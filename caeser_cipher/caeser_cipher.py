import string


def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    ans = ""
    for symb in message:
        if symb in alphabet_lower:
            index0 = alphabet_lower.index(symb)
            index_new = (index0 + n) % (len(alphabet_lower))
            ans += alphabet_lower[index_new]
            continue
        if symb in alphabet_upper:
            index0 = alphabet_upper.index(symb)
            index_new = (index0 + n) % (len(alphabet_upper))
            ans += alphabet_upper[index_new]
            continue
        ans += symb
    return ans
