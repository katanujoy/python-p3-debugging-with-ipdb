# testing/ipdb_debugging_test.py
import pytest
from lib.ipdb_debugging import plus_two

class TestIpdbDebugging:
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum'''
        assert plus_two(3) == 5
