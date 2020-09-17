from unittest.mock import patch
import pytest
from collectionspy.states import States

self_ = States()
def test_get_every_nth_state():
    assert States.get_every_nth_state(self_, n=10) == ['Arizona', 'Arkansas', 'Kentucky', 'Oklahoma', 'South Carolina']


@pytest.mark.parametrize('arg, ret', [('Michigan', 'MI'), ('Test_not_found', 'N/A')])
def test_get_state_abbrev(arg, ret):
    assert States.get_state_abbrev(self_, state_name=arg) == ret