import pytest
import sys

from modules.math_eq import count_velocity


class TestClass:
    def test_count_velocity(self):
        v_max = 50
        w_engine_percent = 20
        weight = 100

        assert count_velocity(v_max, w_engine_percent, weight) == 25
