import os
import json
import argparse
from dataclasses import dataclass


@dataclass()
class Tree:
    tree: dict
    source: str

    def __init__(self, source=os.getcwd()):
        if type(source) == str:
            if os.path.isdir(source):
                self.source = source
                self.tree = {}
            else:
                raise SyntaxError
        else:
            raise TypeError

    def walk_tree(self):
        ...