# Pipeline Module

A simple Python module providing basic arithmetic operations with robust error handling and type safety.

## Functions

### `add(a: int, b: int) -> int`

Adds two integers and returns the result.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- int: Sum of a and b

**Example:**
```python
from ex_pipeline import add

result = add(5, 3)
print(result)  # Output: 8
```

---

### `divide(a: float, b: float) -> float`

Divides a by b with comprehensive error handling for edge cases.

**Parameters:**
- `a` (float): Numerator
- `b` (float): Denominator

**Returns:**
- float: Result of a / b

**Raises:**
- `ValueError`: If b is zero or very close to zero (within 1e-10 tolerance)
- `ValueError`: If division results in infinity or NaN
- `TypeError`: If inputs are not numeric

**Example:**
```python
from ex_pipeline import divide

# Normal division
result = divide(10.0, 2.0)
print(result)  # Output: 5.0

# Mixed numeric types (int and float)
result = divide(7, 2.5)
print(result)  # Output: 2.8

# Error handling - division by zero
try:
    result = divide(10.0, 0.0)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero

# Error handling - very small divisor
try:
    result = divide(10.0, 1e-11)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero

# Error handling - invalid type
try:
    result = divide("10", 2.0)
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: Inputs must be numeric, got str and float
```

## Error Handling

Both functions include robust error handling:
- **Input Validation**: Type checking ensures inputs are correct types
- **Edge Case Handling**: Special values (zero, very small numbers, infinity, NaN) are properly detected
- **Clear Error Messages**: Descriptive error messages help with debugging

## Testing

All functions are covered by comprehensive tests. Run tests with:
```bash
pytest
```

Additional checks:
```bash
ruff check .    # Code style and quality
mypy .          # Type checking
```
