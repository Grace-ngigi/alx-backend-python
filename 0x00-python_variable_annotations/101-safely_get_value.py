#!/usr/bin/env python3
"""
Given the parameters and the return values
add type annotations to the function

Hint: look into TypeVar
"""
from typing import TypeVar, Any, Optional, Mapping, Union

T = TypeVar('T')
Opt = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> Opt:
    ''' add type annonations to the fun '''
    if key in dct:
        return dct[key]
    else:
        return default
