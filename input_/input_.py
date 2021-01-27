import sys
import typing as tp
import io


def input_(prompt: tp.Optional[str] = None,
           inp: tp.Optional[tp.IO[str]] = None,
           out: tp.Optional[tp.IO[str]] = None) -> tp.Optional[str]:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    inp = inp or sys.stdin
    out = out or sys.stdout
    if prompt is not None:
        out.write(prompt)
        out.flush()
    ans = inp.readline().rstrip("\n")
    if not len(ans):
        return None
    return ans
