import math


def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of a / b

    Raises:
        ValueError: If b is zero or very close to zero
        TypeError: If inputs are not numeric
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(
            f"Inputs must be numeric, got {type(a).__name__} and {type(b).__name__}"
        )

    if math.isclose(b, 0, abs_tol=1e-10):
        raise ValueError("Cannot divide by zero")

    result = a / b

    if math.isinf(result) or math.isnan(result):
        raise ValueError(f"Division resulted in invalid value: {result}")

    return result
