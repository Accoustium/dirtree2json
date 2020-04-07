import os
from .filetype import File, Directory, FileTypeError
from dataclasses import dataclass


@dataclass()
class Tree:
    tree: dict
    source: str
    depth: int
    directories: int
    files: int
    display: str
    filler: str

    def __init__(self, source: str = os.getcwd(), depth: int = 1, filler: str = "  "):
        if depth < 0:
            raise ValueError("Depth cannot be a negative value.")

        if type(source) == str:
            if os.path.isdir(source):
                self.source = source
                self.tree = {}
                self.depth = depth
                self.directories = 0
                self.files = 0
                self.filler = filler
                self.display = f"{source}\n"
                self.walk_tree()
                self.display += (
                    f"\ndirectories = {self.directories}"
                    f" files = {self.files}"
                )
            else:
                raise SyntaxError("Source is not a directory.")
        else:
            raise TypeError("Source must be in a string format.")

    def __repr__(self):
        return f"Tree(source={self.source})"

    def __str__(self):
        return f"{self.tree}"

    def __convert_file_type(self, file_test):
        try:
            return File(file_test)
        except FileTypeError:
            self.directories += 1
            self.files -= 1
            return Directory(file_test)

    def __walk_path(self, source_path: str, length: int, indent: int = 1) -> list:
        length += 1

        try:
            path_list = os.listdir(source_path)
            self.files += len(path_list)
        except PermissionError:
            return ["Permission Denied.  Please verify permissions."]

        for index_, file_dir in enumerate(path_list):
            self.display += f"{self.filler * indent}{file_dir}\n"
            test_path = self.__convert_file_type(os.path.join(source_path, file_dir))

            if type(test_path) == Directory:
                if length != self.depth:
                    path_list[index_] = {
                        path_list[index_]: self.__walk_path(
                            os.path.join(source_path, file_dir),
                            length + 1,
                            indent + 1,
                        )
                    }
                else:
                    path_list[index_] = {path_list[index_]: []}

        return path_list

    def walk_tree(self):
        self.tree.update({"source": self.__walk_path(self.source, length=0)})
