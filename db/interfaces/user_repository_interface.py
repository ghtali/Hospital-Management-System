
from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, username: str, hashed_password: str) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> 'User':
        pass
