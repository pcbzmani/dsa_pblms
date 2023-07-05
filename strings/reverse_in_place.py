# Union just
from typing import Union

def reverse_in_place(s: Union[str, int]) -> Union[str, int]:
    if type(s) == str:
        return s[::-1]
    elif type(s) == int:
        str_val = str(s)
        return int(str_val[::-1])
    else:
        raise()
