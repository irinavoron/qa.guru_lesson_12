from dataclasses import dataclass
import datetime
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    current_address: str
    permanent_address: str
    gender: Gender
    phone_number: str
    birth_date: datetime.date
    subject: str
    hobby: Hobby
    file: str
    state: str
    city: str


student = User(
    first_name='FirstName',
    last_name='LastName',
    email='student@example.com',
    current_address='Current Address',
    permanent_address='Permanent Address',
    gender=Gender.male.value,
    phone_number='1234567890',
    birth_date=datetime.date(1985, 4, 18),
    subject='English',
    hobby=Hobby.sports.value,
    file='picture.jpg',
    state='Haryana',
    city='Karnal'
)

admin = User(
    first_name='AdminFirstName',
    last_name='AdminLastName',
    email='admin@example.com',
    current_address='AdminCurrentAddress',
    permanent_address='AdminPermanentAddress',
    gender=Gender.male.value,
    phone_number='1234567890',
    birth_date=datetime.date(1985, 4, 18),
    subject='English',
    hobby=Hobby.music.value,
    file='picture.jpg',
    state='Uttar Pradesh',
    city='Lucknow'
)
