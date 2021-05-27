from abc import ABCMeta, abstractmethod
from typing import Dict, List, TypeVar, Type, Union
from apputils.dbutils import Database


T = TypeVar("T", bound="Model")


class Model(metaclass=ABCMeta):
    # subclass need to define collection
    collection: str
    _id: str

    def __init__(self, *args, **kwargs) -> None:
        pass

    
    def save_to_mongo(self):
        Database.update(self.collection, {"_id":self._id}, self.json())

    def remove_from_mogno(self):
        Database.remove(self.collection, {"_id":self._id})


    @classmethod
    def get_by_id(cls: Type[T], _id) -> T: # typevar bind to model
        return cls.find_one_by("_id", _id)


    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements = Database.find(cls.collection, {})
        return [cls(**element) for element in elements]

    @classmethod
    def find_one_by(cls:Type[T], attribute: str, value: Union[str, Dict]) -> T: # find_one_by("name": "username")
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]: # find_one_by("name": "username")
        try:
            data = [cls(**elem) for elem in Database.find_one(cls.collection, {attribute: value})]
            return data
        except Exception:
            return None
        