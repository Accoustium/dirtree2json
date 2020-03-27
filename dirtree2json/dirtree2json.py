import os
from dataclasses import dataclass


@dataclass()
class Tree:
    tree: dict
    source: str
    depth: int
    directories: int
    files: int

    def __init__(self, source: str = os.getcwd(), depth: int = 1):
        if depth < 0:
            raise ValueError("Depth cannot be a negative value.")

        if type(source) == str:
            if os.path.isdir(source):
                self.source = source
                self.tree = {}
                self.depth = depth
                self.directories = 0
                self.files = 0
                self.walk_tree()
            else:
                raise SyntaxError("Source is not a directory.")
        else:
            raise TypeError("Source must be in a string format.")

    def __repr__(self):
        return f"Tree(source={self.source})"

    def __str__(self):
        return f"{self.tree}"

    def __walk_path(self, source_path: str, length: int) -> list:
        length += 1
        try:
            path_list = os.listdir(source_path)
        except PermissionError:
            return ["Permission Denied.  Please verify permissions."]

        self.files += len(path_list)

        for index, file_dir in enumerate(path_list):
            if os.path.isdir(os.path.join(source_path, file_dir)):

                self.directories += 1
                self.files -= 1

                if length != self.depth:
                    path_list[index] = {
                        file_dir: [
                            self.__walk_path(
                                os.path.join(source_path, file_dir), length + 1
                            )
                        ]
                    }
                else:
                    path_list[index] = {file_dir: []}

        return path_list

    def walk_tree(self):
        self.tree.update({"source": self.__walk_path(self.source, length=0)})


# TODO: write a function to present the tree to user when called via -m
