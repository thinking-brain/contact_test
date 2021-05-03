from datetime import datetime
from enum import Enum
import json

class ContactType(Enum):
    Contact_type_1 = 1
    Contact_type_2 = 2
    Contact_type_3 = 3

class Contact(object):
    id: int
    name: str
    birthdate: datetime
    contact_type: ContactType
    description: str

    def __init__(self, name: str, birthdate: datetime,contact_type: ContactType, description: str):
        self.name = name
        self.birthdate = birthdate
        self.contact_type = contact_type
        self.description = description
