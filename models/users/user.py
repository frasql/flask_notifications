from typing import Dict
import uuid
from models.model import Model
import models.users.errors as UserErrors

from dataclasses import dataclass, field
from apputils.utils import Utils


@dataclass
class User(Model):
    """[summary]

    Args:
        Model ([User]): [description]

    Raises:
        UserErrors.UserNotFoundError: [description]
        UserErrors.InvalidEmailError: [description]
        UserErrors.UserAlreadyRegisteredError: [description]
        UserErrors.IncorrectPasswordError: [description]

    """
    collection: str = field(init=False, default="users")
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)


    def json(self) -> Dict:
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def find_by_email(cls, email):
        """[summary]

        Args:
            email ([str]): [user email]

        Raises:
            UserErrors.UserNotFoundError

        Returns:
            [User]: [user model object]
        """
        try:
            return cls.find_one_by("email", email)
        except TypeError:
            raise UserErrors.UserNotFoundError("An user with this email does not exists.")

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        """[summary]

        Args:
            email (str): [user email]
            password (str): [user password]

        Raises:
            UserErrors.InvalidEmailError
            UserErrors.UserAlreadyRegisteredError

        Returns:
            bool
        """
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The email does not have the right format.")

        try:
            cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError("The email already exists")
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        """[summary]

        Args:
            email (str): [description]
            password (str): [description]

        Raises:
            UserErrors.IncorrectPasswordError

        Returns:
            bool: [description]
        """
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(user.password, password):
            raise UserErrors.IncorrectPasswordError("Your password is incorrect.")
        return True
        


