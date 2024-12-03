import pytest
from advent2024 import total_calculator, array_sorter

class TestsTotalCalculator():
    def test_returns_integer(self):
        array = [1,2]
        assert type(total_calculator(array)) is int

    def test_returns_simple_addiction(self):
        array = [1, 2]
        assert total_calculator(array) == 3

    def test_returns_complex_addiction(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert total_calculator(array) == 55

class TestsArraySorter():
    def test_returns_sorted_array(self):
        array1 = [4, 2, 7]
        assert array_sorter(array1) == [2, 4, 7]
