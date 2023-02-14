#!/usr/bin/python3
"""Module for create an instance FileStorage"""
from .engine.file_storage import FileStorage
from models.base_model import BaseModel


classes = {
    "BaseModel": BaseModel
}

storage = FileStorage()
storage.reload()