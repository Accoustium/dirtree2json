import os
import sys
import pytest

mypath = os.path.join(os.path.split(__file__)[:-1][0])
sys.path.append(os.path.join(mypath, '..'))
from dirtree2json import Tree


@pytest.fixture
def tree_at_source():
    return Tree()


def test_tree_instance(tree_at_source):
    assert isinstance(tree_at_source, Tree)
