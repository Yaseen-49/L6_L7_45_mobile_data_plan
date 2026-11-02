
import pytest

from mobile_data_plan import (
    overage_charge,
    recharge_allowed,
    validity_status,
)


# Invalid input branches
def test_unknown_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        overage_charge("gold", 5, False, False)


def test_negative_data_usage():
    with pytest.raises(ValueError, match="invalid data usage"):
        overage_charge("basic", -1, False, False)


# Overage charge branches
def test_within_included_data():
    assert overage_charge("standard", 3, False, False) == 0


def test_loyal_customer_included_data():
    assert overage_charge("standard", 6, False, True) == 0


def test_loyal_premium_customer():
    assert overage_charge("premium", 12, False, True) == 30


def test_normal_overage_charge():
    assert overage_charge("standard", 7, False, False) == 30


def test_roaming_overage_charge():
    assert overage_charge("basic", 4, True, False) == 80


def test_high_non_roaming_overage():
    assert overage_charge("basic", 13, False, False) == 275


def test_high_roaming_overage():
    assert overage_charge("basic", 13, True, False) == 605


# Recharge decision branches
def test_kyc_pending_allowed():
    assert recharge_allowed(200, 5, True) is True


def test_kyc_pending_not_allowed():
    assert recharge_allowed(201, 1, True) is False


def test_recharge_above_limit():
    assert recharge_allowed(2001, 1, False) is False


def test_recharge_with_pending_count_allowed():
    assert recharge_allowed(500, 2, False) is True


def test_recharge_with_too_many_pending():
    assert recharge_allowed(500, 3, False) is False


# Validity decision branches
def test_prepaid_active():
    assert validity_status(0, True, False) == "active"


def test_non_prepaid_active_with_addon():
    assert validity_status(5, False, True) == "active"


def test_grace_period():
    assert validity_status(4, False, True) == "grace"


def test_expired_validity():
    assert validity_status(-11, False, True) == "expired"
