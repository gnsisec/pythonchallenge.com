from nose.tools import *
from challenge import challenge2

def test_challenge2_fuck_caption():
    assert_equal(challenge2.too_many_secret("g fmnc"), "i hope")

def test_challenge2_url():
    assert_equal(challenge2.too_many_secret("map"), "ocr")
