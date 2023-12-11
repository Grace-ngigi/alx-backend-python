#!/usr/bin/env python3
"""
type-annotated function sum_list
takes a list input_list of floats as argument
returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return sum as float """
    return float(sum(input_list))
