from nose.tools import *
from challenge import challenge1

def test_challenge1():
    assert_equal(challenge1.new_url(2,38), 274877906944)
