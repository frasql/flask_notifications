import datetime
from typing import Dict
import uuid
from dataclasses import dataclass, field
from apputils.utils import Utils
from models.model import Model


@dataclass(eq=False)
class Note(Model):
    collection: str = field(init=False, default="notes")
    title: str
    description: str 
    start_time: datetime
    end_time: datetime 
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)


    def json(self) -> Dict:
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "start_time": Utils.datetime_to_string(self.start_time),
            "end_time": Utils.datetime_to_string(self.end_time)
        }


