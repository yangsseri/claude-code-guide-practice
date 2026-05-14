from ex_pipeline import add


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
