import os
import sys
import pytest
from dirtree2json import Tree, File, Directory, FileTypeError


@pytest.fixture
def tree_at_source():
    return Tree()


def test_tree_instance(tree_at_source):
    assert isinstance(tree_at_source, Tree())
