import pytest
from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]

def test_dict():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data, "vcs", "git") == "mercurial"
    assert dicts.get_val(data, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == 'git'
    assert dicts.get_val({}, "vcs", "bazaar") == 'bazaar'

@pytest.fixture
def coll1():
    return [1, 2, 3]

def test_get1(coll1):
    assert arrs.get(coll1, 2, "test") == 3

def test_slice1(coll1):
    assert arrs.my_slice(coll1, 1) == [2, 3]