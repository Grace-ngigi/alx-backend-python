#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list
takes a list mxd_lst of integers and floats
returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum of mixed lists as float """
    return sum(mxd_lst)
