from datetime import datetime
from os import name
from typing import Dict, List
import uuid
from dataclasses import dataclass, field
from models.note import Note
from models.model import Model
from models.users.user import User
import models.users.errors as UserErrors


@dataclass(eq=False)
class Alert(Model):
    collection: str = field(init=False, default="alerts")
    name: str
    note_id: str 
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
 

    def __post_init__(self) -> None:
        self.note = Note.get_by_id(self.note_id)
        self.user = User.find_by_email(self.user_email)

    
    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "note_id": self.note_id,
            "user_email": self.user_email
        }


    def notify_if_time_elapsed(self):
        current_time = datetime.utcnow()
        if current_time > self.note.end_time:
            print("opoooooooooooops")


