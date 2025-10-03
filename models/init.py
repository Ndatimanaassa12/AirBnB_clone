#!/usr/bin/python3
from models.engine.file_storage import FileStorage

storage = FileStorage()  # unique instance
storage.reload()          # load existing objects

