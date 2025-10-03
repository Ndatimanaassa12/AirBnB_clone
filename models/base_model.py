#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage  # import the FileStorage instance

class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if kwargs:  # Re-create from dictionary
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":  # ignore class key
                    setattr(self, key, value)
        else:  # New instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)  # register new instance in FileStorage

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at and save to FileStorage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d

