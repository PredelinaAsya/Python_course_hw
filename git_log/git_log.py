import typing as tp


def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """
    arr_lines = inp.getvalue().split("\n")
    while arr_lines.count(""):
        arr_lines.remove("")
    for line in arr_lines:
        arr_col = line.split("\t")
        message = arr_col[4]
        s = arr_col[0][:7] + "." * (73 - len(message)) + message + "\n"
        out.write(s)
    return
