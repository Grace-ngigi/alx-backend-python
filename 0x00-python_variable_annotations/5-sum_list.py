#!/usr/bin/env python3
from typing import List
"""
type-annotated function sum_list
takes a list input_list of floats as argument
returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """ return sum as float """
    return sum(input_list)
