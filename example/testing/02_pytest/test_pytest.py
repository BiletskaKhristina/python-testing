import pytest

from app import add, divide, is_even, get_positive_numbers


@pytest.mark.unit
def test_add():
    assert add(2, 3) == 5


@pytest.mark.unit
def test_divide():
    assert divide(10, 2) == 5


@pytest.mark.unit
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.unit
@pytest.mark.parametrize(
    "number, expected",
    [(2, True), (5, False), (0, True), (-4, True)],
)
def test_is_even(number, expected):
    assert is_even(number) == expected


@pytest.mark.unit
def test_get_positive_numbers():
    assert get_positive_numbers([-2, 0, 3, 5]) == [3, 5]