"""Unit tests for cinema_price.ticket_price.

Each test id (e.g. TP-01) matches a row in the Test Case Specification.
"""
import pytest

from cinema_price import ticket_price


# --- Valid inputs: equivalence partitions and boundaries (REQ P1, P2) ---

def test_zero_tickets_costs_zero():
    """TP-01: zero tickets must cost 0 (boundary, REQ P2)."""
    assert ticket_price(0) == 0


@pytest.mark.parametrize(
    "ticket_count, expected",
    [
        pytest.param(1, 1200, id="TP-02-one-ticket"),
        pytest.param(2, 2400, id="TP-03-two-tickets"),
        pytest.param(10, 12000, id="TP-04-ten-tickets"),
        pytest.param(1000, 1200000, id="TP-05-large-count"),
    ],
)
def test_total_is_count_times_1200(ticket_count, expected):
    """TP-02..05: total price is ticket_count * 1200 cents (REQ P1)."""
    assert ticket_price(ticket_count) == expected


def test_return_type_is_int():
    """TP-06: result must be an int in cents, not float or bool (REQ G1)."""
    result = ticket_price(3)
    assert type(result) is int


# --- Out-of-range inputs raise ValueError (REQ G4) ---

@pytest.mark.parametrize(
    "ticket_count",
    [
        pytest.param(-1, id="TP-07-minus-one"),
        pytest.param(-100, id="TP-08-large-negative"),
    ],
)
def test_negative_count_raises_value_error(ticket_count):
    """TP-07..08: negative counts are outside the permitted range."""
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


# --- Invalid data types raise TypeError (REQ G2, G3) ---

@pytest.mark.parametrize(
    "bad_value",
    [
        pytest.param("3", id="TP-09-str"),
        pytest.param(3.0, id="TP-10-float"),
        pytest.param(None, id="TP-11-none"),
        pytest.param(True, id="TP-12-bool-true"),
        pytest.param(False, id="TP-13-bool-false"),
        pytest.param([3], id="TP-14-list"),
        pytest.param(-1.0, id="TP-15-negative-float"),
    ],
)
def test_invalid_type_raises_type_error(bad_value):
    """TP-09..15: non-int input (including bool) raises TypeError."""
    with pytest.raises(TypeError):
        ticket_price(bad_value)
