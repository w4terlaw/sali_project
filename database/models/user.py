from typing import Type

from sqlalchemy.dialects.sqlite import TEXT, INTEGER, FLOAT, DATETIME
from sqlalchemy.orm import Session
from sqlalchemy.schema import Column

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    gender = Column(TEXT)
    title = Column(TEXT)
    first_name = Column(TEXT)
    last_name = Column(TEXT)
    street_number = Column(INTEGER)
    street_name = Column(TEXT)
    city = Column(TEXT)
    state = Column(TEXT)
    country = Column(TEXT)
    postcode = Column(INTEGER)
    latitude = Column(FLOAT)
    longitude = Column(FLOAT)
    timezone_offset = Column(TEXT)
    timezone_description = Column(TEXT)
    email = Column(TEXT)
    uuid = Column(TEXT)
    username = Column(TEXT)
    password = Column(TEXT)
    salt = Column(TEXT)
    md5 = Column(TEXT)
    sha1 = Column(TEXT)
    sha256 = Column(TEXT)
    dob_date = Column(DATETIME)
    dob_age = Column(INTEGER)
    registered_date = Column(INTEGER)
    registered_age = Column(INTEGER)
    phone = Column(TEXT)
    cell = Column(TEXT)
    id_name = Column(TEXT)
    id_value = Column(TEXT)
    picture_large = Column(TEXT)
    picture_medium = Column(TEXT)
    picture_thumbnail = Column(TEXT)
    nat = Column(TEXT)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})>"

    @classmethod
    def get_all(cls, session: Session) -> list[Type["User"]]:
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session: Session, user_id: int) -> "User":
        return session.query(cls).get(user_id)

    def save(self, session: Session) -> None:
        session.add(self)
        session.commit()
