import os
import json
import argparse
from dataclasses import dataclass


@dataclass()
class Tree:
    tree: dict
    source: str
    curr_dir: str

    def __init__(self, source: str=os.getcwd()):
        if type(source) == str:
            print(source)
            if os.path.isdir(source):
                self.source = source
                self.tree = {}
                self.walk_tree()
            else:
                raise SyntaxError
        else:
            raise TypeError
    
    def __repr__(self):
        return f"Tree(source={self.source})"
    
    def __str__(self):
        return f"{self.tree}"

    def __walk_path(self, source_path: str) -> list:
        path_list = os.listdir(source_path)
        for index, file_dir in enumerate(path_list):
            if os.path.isdir(file_dir):
                path_list[index] = {
                    file_dir: self.__walk_path(
                        os.path.join(source_path, file_dir)
                    )
                }
        
        return path_list

    def walk_tree(self):
        self.tree.update({
            'source': self.__walk_path(self.source)
        })
