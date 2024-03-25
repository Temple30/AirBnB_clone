#!/usr/bin/python3
"""
__init__ for models directory
"""
from models.engine.file_storage import FileStorage

# Create a FileStorage instance
storage = FileStorage()

# Reload data into the FileStorage instance
storage.reload()
