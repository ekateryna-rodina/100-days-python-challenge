from unittest.mock import patch
import pytest
from collectionspy.states import States

@pytest.fixture(scope='module')
def states():
    self_ = States()
    return self_
    
def test_get_every_nth_state(states):
    assert States.get_every_nth_state(states, n=10) == ['Arizona', 'Arkansas', 'Kentucky', 'Oklahoma', 'South Carolina']

@pytest.mark.parametrize('arg, ret', [('Michigan', 'MI'), ('Test_not_found', 'N/A')])
def test_get_state_abbrev(states, arg, ret):
    assert States.get_state_abbrev(states, state_name=arg) == ret