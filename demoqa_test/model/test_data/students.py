from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    Accounting = 'Accounting'
    English = 'English'
    History = 'History'
    Mathematics = 'Math'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class Student:
    first_name: str
    last_name: str
    gender: Gender
    email: str = 'jaxym@mailinator.com'
    phone: str = '3457856472'
    birth_day: str = '10'
    birth_month: str = 'September'
    birth_year: str = '1999'
    subjects: Tuple[Subject] = (Subject.History, Subject.English, Subject.Accounting)
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Music)
    picture: str = 'resources/student-photo.jpeg'
    address: str = 'Saint-Petersburg, Sadovaya str, 23'
    state: str = 'Haryana'
    city: str = 'Karnal'
