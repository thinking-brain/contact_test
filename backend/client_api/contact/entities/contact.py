from datetime import datetime
from enum import Enum

class ContactType(Enum):
    type1 = 'Contact type 1'
    type2 = 'Contact type 2'
    type3 = 'Contact type 3'

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
