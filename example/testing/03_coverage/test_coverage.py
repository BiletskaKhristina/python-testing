import pytest

from app import calculate_discount, classify_number


@pytest.mark.unit
def test_discount():
    assert calculate_discount(100, 20) == 80


@pytest.mark.unit
def test_discount_zero():
    assert calculate_discount(100, 0) == 100


@pytest.mark.unit
def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_discount(-10, 20)


@pytest.mark.unit
def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)


@pytest.mark.unit
def test_positive_number():
    assert classify_number(5) == "positive"


@pytest.mark.unit
def test_negative_number():
    assert classify_number(-3) == "negative"


@pytest.mark.unit
def test_zero():
    assert classify_number(0) == "zero"