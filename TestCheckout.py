import pytest

from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_canCalculateTotal(checkout):
    checkout.addItemPrice("a",1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1