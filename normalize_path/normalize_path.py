def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """
    if not len(path):
        return "."
    while "//" in path:
        path = path.replace("//", "/")
    arr_names = path.split("/")
    arr_stack = []
    for name in arr_names:
        if len(arr_stack) >= 2 and arr_stack[len(arr_stack) - 1] == '.':
            arr_stack.pop()
        if name == "..":
            num = len(arr_stack)
            if num:
                last = arr_stack[num - 1]
            if num and len(last) and last != "." and last != "..":
                arr_stack.pop()
                continue
            if len(arr_stack) == 1 and arr_stack[0] == "":
                continue
            if len(arr_stack) == 1 and arr_stack[0] == ".":
                arr_stack.pop()
        if len(arr_stack) and arr_stack[len(arr_stack) - 1] == ".":
            arr_stack.pop()
        arr_stack.append(name)
    if not len(arr_stack):
        return "."
    ans = ""
    for path in arr_stack:
        ans += (path + "/")
    if ans == "/":
        return ans
    return ans[:-1]
