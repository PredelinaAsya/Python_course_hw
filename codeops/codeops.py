import types
import typing as tp
import dis


def count_operations(source_code: types.CodeType) -> tp.Dict[str, int]:
    """Count byte code operations in given source code.

    :param source_code: the bytecode operation names to be extracted from
    :return: operation counts
    """
    ans = {}
    for instruction in dis.get_instructions(source_code):
        instr_name = instruction.opname
        if instr_name not in ans.keys():
            ans[instr_name] = 0
        ans[instr_name] += 1
        if isinstance(instruction.argval, types.CodeType):
            edge_dict = count_operations(instruction.argval)
            for k, v in edge_dict.items():
                if k not in ans.keys():
                    ans[k] = 0
                ans[k] += v
    return ans
