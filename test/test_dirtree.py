import os
import sys
import pytest

file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_path, ".."))
from dirtree2json import Tree, File, Directory, FileTypeError


@pytest.fixture(scope="module")
def tree_at_source():
    return Tree()


def test_tree_instance(tree_at_source):
    assert isinstance(tree_at_source, Tree)


def test_print_tree(tree_at_source):
    print(tree_at_source.display)
