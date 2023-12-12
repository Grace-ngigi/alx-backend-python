#!/usr/bin/env python3
"""
Annotate the below function’s parameters
and return values with the appropriate types
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''duck type an interable object'''
    return [(i, len(i)) for i in lst]
