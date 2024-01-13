#!/usr/bin/python3
"""This is the init file of models module."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
storage.save()
