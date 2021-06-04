from datetime import datetime
from os import name
from typing import Dict, List
import uuid
from dataclasses import dataclass, field
from models.model import Model
from models.users.user import User
import models.users.errors as UserErrors
from apputils.utils import Utils


@dataclass(eq=False)
class Activity(Model):
    collection: str = field(init=False, default="activities")
    name: str
    description: str
    order: int
    time_to_complete: float
    project_id: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    

    
    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "description": self.description,
            "order": self.order,
            "time_to_complete": self.time_to_complete,
            "project_id": self.project_id
        }