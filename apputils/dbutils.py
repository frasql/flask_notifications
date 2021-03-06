import pymongo
from typing import Dict
import os


class Database:
    """Database utils static class"""
    
    URI = os.getenv("MONGODB_URI")
    DATABASE = pymongo.MongoClient(URI).get_database("notification_app")

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert(data)

    
    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection:str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

 
    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection:str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)