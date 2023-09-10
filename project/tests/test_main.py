import pytest
import sys

print(sys.path)

from app import add


@pytest.mark.parametrize(
    "a, b, expected",
    (
        (1, 2, 3),
        (0, 0, 0),
        (1, 0, 1),
    ),
)
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected
