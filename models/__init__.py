#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""

from models.engine.file_storage import self

storage = self()
storage.reload()
