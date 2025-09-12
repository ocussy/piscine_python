import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """     generate_id():
    returns a random 15-character lowercase string ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name, surname) -> str:
    """     generate_login(name, surname):
    returns a login combining the first letter of name with the full surname"""
    return name[0] + surname


@dataclass
class Student:
    """Student class:
    represents a student with auto-generated ID and login"""
    name: str
    surname: str
    active: bool = True
    id: str = field(default_factory=generate_id, init=False)
    login: str = field(init=False)

    def __post_init__(self):
        """     __post_init__():
        automatically generates the login after initialization"""
        self.login = generate_login(self.name, self.surname)
