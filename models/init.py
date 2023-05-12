#!/usr/bin/python3
"""
This module initializes the variable storage, an instance of class FileStorage, and
calls the reload method on this variable.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

