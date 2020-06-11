import os
from .filetype import File, Directory, FileTypeError


class Tree:
    def __init__(self, source: str = os.getcwd(), depth: int = 1, filler: str = "  "):
        """
        Create a file path tree json object.  Will have both a display option for printing
        in a clean format, and a json object to use in programs.

        :param source: Source directory to start the tree traversal.
        :param depth: How far down you wish to look into the directories.  Setting to 0 will
            continue recursively until all directories are found, with a limit of 1000 depth.  (default = 1)
        :param filler:
        """
        if not 0 <= depth < 1000:
            raise ValueError("Depth cannot be a negative value or greater than 999.")

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
                raise FileTypeError("Source is not a directory.")
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

    def __build_print_display(self, file_dir, indent):
        self.display += f"{self.filler * indent}{file_dir}\n"

    def __walk_path(self, source_path: str, length: int, indent: int = 1) -> list:
        if length == 999:
            return

        length += 1

        try:
            path_list = os.listdir(source_path)
            self.files += len(path_list)
        except PermissionError:
            return ["Permission Denied.  Please verify permissions."]

        for index_, file_dir in enumerate(path_list):
            self.__build_print_display(file_dir, indent)
            test_path = self.__convert_file_type(os.path.join(source_path, file_dir))

            if type(test_path) == Directory:
                if length != self.depth:
                    path_list[index_] = {
                        test_path: self.__walk_path(
                            os.path.join(source_path, file_dir),
                            length + 1,
                            indent + 1,
                        )
                    }
                else:
                    path_list[index_] = {test_path: []}

        return path_list

    def walk_tree(self):
        """
        Walk through the whole directory tree of the provided source directory.

        :return:
        """
        self.tree.update({"source": self.__walk_path(self.source, length=0)})
