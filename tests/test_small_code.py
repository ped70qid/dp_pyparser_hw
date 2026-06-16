from proj.small_code import plus
import pytest

def test_plus():
    assert plus(2,3) == 5



def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 + 1
        1 / 0