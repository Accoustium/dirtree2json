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
                self.curr_dir = os.getcwd()
            else:
                raise SyntaxError
        else:
            raise TypeError
    
    def __repr__(self):
        return f"Tree(source={self.source})"
    
    def __str__(self):
        return f"{self.tree}"

    def __walk_path(self) -> list:
        path_list = os.listdir()
        for index, file_dir in enumerate(path_list):
            if os.path.isdir(file_dir):
                os.chdir(file_dir)
                path_list[index] = {
                    file_dir: self.__walk_path()
                }
                os.chdir('..')
        
        return path_list

    def walk_tree(self):
        if os.getcwd() != self.source:
            os.chdir(self.source)
        
        self.tree.update({
            'source': self.__walk_path()
        })

        if os.getcwd() != self.curr_dir:
            os.chdir(self.curr_dir)
