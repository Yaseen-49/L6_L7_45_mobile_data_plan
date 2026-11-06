
from hypothesis import given, strategies as st
from mobile_data_plan import parse_plan, usage_average, payable_bill


# Test 1: Fuzz parse_plan with random strings and None
@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    result = parse_plan(s)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and isinstance(result[0], str)
        and isinstance(result[1], float)
    )


# Test 2: Fuzz usage_average with random strings and None
@given(st.text() | st.none())
def test_usage_average_no_crash(s):
    result = usage_average(s)
    assert result is None or isinstance(result, int)


# Test 3: Fuzz payable_bill with random strings and None
@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    result = payable_bill(s)
    assert result is None or (
        isinstance(result, (int, float)) and result >= 0
    )


# Test valid inputs
def test_valid_inputs():
    assert parse_plan("standard:5") == ("Standard", 5.0)
    assert usage_average("300,450,800") == 516
    assert payable_bill("399|50") == 420.82


# Test invalid inputs
def test_invalid_inputs():
    assert parse_plan(None) is None
    assert parse_plan(":") is None
    assert usage_average(None) is None
    assert usage_average("") is None
    assert payable_bill(None) is None
    assert payable_bill("|") is None
