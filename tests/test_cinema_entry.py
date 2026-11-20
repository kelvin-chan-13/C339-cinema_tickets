"""Unit tests for cinema_entry.can_watch.

Each test id (e.g. CW-03) matches a row in the Test Case Specification.
"""
import pytest

from cinema_entry import can_watch


# --- Below the age limit: may not watch (REQ E2) ---

@pytest.mark.parametrize(
    "age",
    [
        pytest.param(0, id="CW-01-age-0"),
        pytest.param(8, id="CW-02-age-8"),
        pytest.param(15, id="CW-03-age-15"),
    ],
)
def test_under_16_cannot_watch(age):
    """CW-01..03: ages 0-15 return False (lower partition and boundary)."""
    assert can_watch(age) is False


# --- At or above the age limit: may watch (REQ E1) ---

def test_age_16_can_watch():
    """CW-04: age 16 is the exact boundary and must be allowed."""
    assert can_watch(16) is True


@pytest.mark.parametrize(
    "age",
    [
        pytest.param(17, id="CW-05-age-17"),
        pytest.param(40, id="CW-06-age-40"),
        pytest.param(120, id="CW-07-age-120"),
    ],
)
def test_over_16_can_watch(age):
    """CW-05..07: ages above 16 return True."""
    assert can_watch(age) is True


@pytest.mark.parametrize("age", [15, 16])
def test_return_type_is_bool(age):
    """CW-08: result is a real Python bool (REQ E1, E2)."""
    assert type(can_watch(age)) is bool


# --- Out-of-range inputs raise ValueError (REQ G4) ---

@pytest.mark.parametrize(
    "age",
    [
        pytest.param(-1, id="CW-09-minus-one"),
        pytest.param(-100, id="CW-10-large-negative"),
    ],
)
def test_negative_age_raises_value_error(age):
    """CW-09..10: negative ages are outside the permitted range."""
    with pytest.raises(ValueError):
        can_watch(age)


# --- Invalid data types raise TypeError (REQ G2, G3) ---

@pytest.mark.parametrize(
    "bad_value",
    [
        pytest.param("16", id="CW-11-str"),
        pytest.param(16.0, id="CW-12-float"),
        pytest.param(None, id="CW-13-none"),
        pytest.param(True, id="CW-14-bool-true"),
        pytest.param(False, id="CW-15-bool-false"),
        pytest.param([16], id="CW-16-list"),
        pytest.param(-1.0, id="CW-17-negative-float"),
    ],
)
def test_invalid_type_raises_type_error(bad_value):
    """CW-11..17: non-int input (including bool) raises TypeError."""
    with pytest.raises(TypeError):
        can_watch(bad_value)
