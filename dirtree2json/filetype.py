import os
import time
from abc import ABC


class FileType(ABC):
    def __init__(self, obj):
        self.__dict__.update({"_contents": obj})

    def __repr__(self):
        return NotImplemented

    def __str__(self):
        return NotImplemented

    def __hash__(self):
        return NotImplemented

    def __setattr__(self, name, value):
        raise AttributeError(f"Can't set attribute {name}.")

    def __getattr__(self, name):
        private_name = "_" + name
        return getattr(self, private_name)


class FileTypeError(Exception):
    pass


class File(FileType):
    def __init__(self, obj):
        if os.path.isfile(obj):
            self.__dict__.update(
                {
                    "_contents": os.path.split(obj)[-1],
                    "_file_path": os.path.abspath(obj),
                    "_file_created": time.ctime(os.path.getctime(obj)),
                    "_file_modified": time.ctime(os.path.getmtime(obj)),
                }
            )
        else:
            raise FileTypeError("Attempted to assign non-file to file object.")

    def __repr__(self):
        return f"File({self.contents})"

    def __str__(self):
        return f"File({self.contents})"

    def __hash__(self):
        return hash(repr(self))

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def __getattr__(self, item):
        return super().__getattr__(item)


class Directory(FileType):
    def __init__(self, obj):
        if os.path.isdir(obj):
            self.__dict__.update(
                {
                    "_contents": os.path.split(obj)[-1],
                    "_file_path": os.path.abspath(obj),
                    "_file_created": time.ctime(os.path.getctime(obj)),
                    "_file_modified": time.ctime(os.path.getmtime(obj)),
                }
            )
        else:
            raise FileTypeError(
                "Attempted to assign non-directory to directory object."
            )

    def __repr__(self):
        return f"Directory({self.contents})"

    def __str__(self):
        return f"Directory({self.contents})"

    def __hash__(self):
        return hash(repr(self))

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def __getattr__(self, item):
        return super().__getattr__(item)
