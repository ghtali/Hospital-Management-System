
from .database import Session
from .models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, username: str, hashed_password: str) -> None:
        user = User(username=username, hashed_password=hashed_password)
        self.session.add(user)
        self.session.commit()

    def get_user_by_username(self, username: str) -> User:
        return self.session.query(User).filter_by(username=username).first()
