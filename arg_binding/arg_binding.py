from types import FunctionType
from typing import Any, Dict

CO_VARARGS = 4
CO_VARKEYWORDS = 8

ERR_TOO_MANY_POS_ARGS = 'Too many positional arguments'
ERR_TOO_MANY_KW_ARGS = 'Too many keyword arguments'
ERR_MULT_VALUES_FOR_ARG = 'Multiple values for arguments'
ERR_MISSING_POS_ARGS = 'Missing positional arguments'
ERR_MISSING_KWONLY_ARGS = 'Missing keyword-only arguments'


def bind_args(func: FunctionType, *args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Bind values from `args` and `kwargs` to corresponding arguments of
    `func`

    :param func: function to be inspected
    :param args: positional arguments to be bound
    :param kwargs: keyword arguments to be bound
    :return: `dict[argument_name] = argument_value` if binding was successful,
             raise TypeError with one of `ERR_*` error descriptions otherwise
    """
    varnames = func.__code__.co_varnames
    amount_args = func.__code__.co_argcount
    amount_def_args = 0
    if func.__defaults__ is not None:
        amount_def_args = len(func.__defaults__)
    amount_non_def_args = amount_args - amount_def_args
    fl_varargs = func.__code__.co_flags & CO_VARARGS
    amount_kwargs = func.__code__.co_kwonlyargcount
    amount_def_kwargs = 0
    if func.__kwdefaults__ is not None:
        amount_def_kwargs = len(func.__kwdefaults__.keys())
    amount_non_def_kwargs = amount_kwargs - amount_def_kwargs
    fl_varkwargs = func.__code__.co_flags & CO_VARKEYWORDS
    position_var = varnames[:amount_args]
    ans = {}
    last_ind = len(varnames)
    if fl_varkwargs:
        last_ind -= 1
        kwargs_name = varnames[last_ind]
    if fl_varargs:
        last_ind -= 1
        args_name = varnames[last_ind]
    kw_var = varnames[amount_args:last_ind]
    if len(args) > amount_args and not fl_varargs:
        raise TypeError(ERR_TOO_MANY_POS_ARGS)
    iter = 0
    for elem in args:
        if iter < len(position_var):
            ans[position_var[iter]] = elem
            iter += 1
        else:
            if args_name not in ans.keys():
                ans[args_name] = []
            ans[args_name].append(elem)
    for k, v in kwargs.items():
        if k in ans.keys():
            if ans[k] != v:
                raise TypeError(ERR_MULT_VALUES_FOR_ARG)
        else:
            if k in varnames:
                ans[k] = v
            else:
                if not fl_varkwargs:
                    raise TypeError(ERR_TOO_MANY_KW_ARGS)
                if kwargs_name not in ans.keys():
                    ans[kwargs_name] = {}
                ans[kwargs_name][k] = v
    names_default_args = position_var[amount_non_def_args:amount_args]
    default_val_args = func.__defaults__
    names_default_kwargs = kw_var[amount_non_def_kwargs:amount_kwargs]
    default_dict_kwargs = func.__kwdefaults__
    for i in range(len(names_default_args)):
        if names_default_args[i] not in ans.keys():
            ans[names_default_args[i]] = default_val_args[i]
    for name in names_default_kwargs:
        if name not in ans.keys():
            ans[name] = default_dict_kwargs[name]
    for name in position_var:
        if name not in ans.keys():
            raise TypeError(ERR_MISSING_POS_ARGS)
    for name in kw_var:
        if name not in ans.keys():
            raise TypeError(ERR_MISSING_KWONLY_ARGS)
    if fl_varkwargs and kwargs_name not in ans.keys():
        ans[kwargs_name] = {}
    if fl_varargs and args_name not in ans.keys():
        ans[args_name] = ()
    if fl_varargs:
        ans[args_name] = tuple(ans[args_name])
    return ans
