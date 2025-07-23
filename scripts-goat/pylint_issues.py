# pylint_sample.py
import os, sys        # unused‑import (likely both), bad style for multiple imports
import math           # unused‑import

CONSTANT_value = 3.14  # bad-constant-case (should be UPPER_CASE)

def calculate(x, y=[]):   # dangerous default mutable argument
    """Return x squared and stash it in y."""
    result = x * x
    y.append(result)      # mutates the default list every call
    return result

def unreachable_branch():
    return
    print("This line is unreachable")  # unreachable‑code

def shadow_builtins():
    list = [1, 2, 3]      # redefined‑builtin
    sum = 0               # redefined‑builtin
    for i in list:
        sum += i
    return sum

def broad_exception():
    try:
        1 / 0
    except:               # bare‑except
        pass

def too_many_args(a, b, c, d, e, f, g, h, i):
    """Simply prints its arguments."""
    print(a, b, c, d, e, f, g, h, i)

GLOBAL_VAR = 0
def modify_global():
    global GLOBAL_VAR     # global‑statement
    GLOBAL_VAR += 1

if __name__ == "__main__":
    calculate(10)
    unreachable_branch()
    shadow_builtins()
    broad_exception()
    modify_global()
