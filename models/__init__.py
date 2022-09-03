#!/usr/bin/python3
""" FileStorage instance """


from models.base_model import BaseModel
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
