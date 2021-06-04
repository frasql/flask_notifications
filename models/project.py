from datetime import datetime
from os import name
from typing import Dict, List
import uuid
from dataclasses import dataclass, field
from models.model import Model
from models.users.user import User
from models.activity import Activity
import models.users.errors as UserErrors
from apputils.utils import Utils
import functools


@dataclass(eq=False)
class Project(Model):
    collection: str = field(init=False, default="projects")
    name: str
    description: str
    deadline: float
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
 

    def __post_init__(self) -> None:
        self.user = User.find_by_email(self.user_email)
        self.activities = Activity.find_many_by("project_id", self._id)

    
    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "description": self.description,
            "deadline": self.deadline,
            "user_email": self.user_email
        }
        
    
    @property
    def total_time(self):
        return sum(act.time_to_complete for act in self.activities)
    
    def is_on_schedule(self):
        return self.deadline < self.total_time
    
    @property
    def remaining_time(self):
        return self.deadline - self.total_time
        
    
        
    


  

