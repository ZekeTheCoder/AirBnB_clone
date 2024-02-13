#!/usr/bin/python3
"""
This is the docstring for the models package.

import the FileStorage class from the models.engine.file_storage module
and create a FileStorage instance named storage
and calls the reload() method on this storage instance.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
