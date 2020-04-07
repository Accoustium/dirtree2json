import os
import sys
import pytest

my_path = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(my_path, ".."))
from dirtree2json import Tree, File, Directory, FileTypeError


@pytest.fixture
def tree_at_source():
    return Tree()


def test_tree_instance(tree_at_source):
    assert isinstance(tree_at_source, Tree)
