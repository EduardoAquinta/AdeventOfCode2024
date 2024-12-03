import pytest
import pytest_describe
from advent2024 import distance_calculation
from advent2024 import array_sorter

def describe_distance_calculation():
    def returns_integer():
        assert type(distance_calculation()) is int

def describe_array_sorter():
    def returns_sorted_array():
        array1 = [4, 2, 7]
        assert array_sorter(array1) == [2, 4, 7]
