import typing as tp


def count_util(text: str, flags: tp.Optional[str] = None) -> tp.Dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    arr_lines = text.split("\n")
    if arr_lines[len(arr_lines) - 1] == "":
        arr_lines.pop()
    arr_words = text.split()
    if (flags is None) or (len(flags) == 0):
        flags = ["-mlLw"]
    ans = {}
    for s in flags:
        if "m" in s:
            ans["chars"] = 0
        if "l" in s:
            ans["lines"] = 0
        if "L" in s:
            ans["longest_line"] = 0
        if "w" in s:
            ans["words"] = 0
    for k in ans.keys():
        if k == "chars":
            ans[k] = len(text)
        if k == "lines":
            ans[k] = len(arr_lines)
        if k == "longest_line":
            maxx = 0
            for line in arr_lines:
                maxx = max(maxx, len(line))
            ans[k] = maxx
        if k == "words":
            ans[k] = len(arr_words)
    return ans
