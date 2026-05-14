import pytest

from ex_pipeline import add, divide


class TestAdd:
    def test_add_positive_numbers(self) -> None:
        assert add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self) -> None:
        assert add(10, -5) == 5

    def test_add_zero(self) -> None:
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, -3) == -3


class TestDivide:
    def test_divide_positive_numbers(self) -> None:
        assert divide(10, 2) == 5.0

    def test_divide_negative_numbers(self) -> None:
        assert divide(-10, 2) == -5.0

    def test_divide_mixed_numbers(self) -> None:
        assert divide(10, -2) == -5.0

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_by_very_small_number(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 1e-11)

    def test_divide_with_invalid_type(self) -> None:
        with pytest.raises(TypeError, match="Inputs must be numeric"):
            divide("10", 2)  # type: ignore

    def test_divide_with_float_inputs(self) -> None:
        assert divide(7.5, 2.5) == 3.0
