import mathlib
import pytest
import sys


# Skip the test case
@pytest.mark.skip(reason="I do not want to run the test now.")
def test_calc_total():
    total = mathlib.calc_total(10, 5)
    assert total == 15


# skip the result based on condition
@pytest.mark.skipif(
    sys.version_info > (3, 5),
    reason="Do not run the test in python version greater than 3.5",
)
def test_calc_multipy():
    total = mathlib.calc_multiply(10, 3)
    assert total == 30


def test_calc_rec_area():
    result = mathlib.calc_rec_area(4, 5)
    assert result == 20


# Skip the test whose name contains multiply
# COmmand: pytest -k multiply
# This command will skip test whose name contains multipy


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True
