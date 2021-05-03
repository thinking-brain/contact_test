from typing import List
from ...entities.contact import Contact, ContactType
from ...repositories.contact_repository import IContactRepository
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Date, Enum
# from sqlalchemy.orm import relationship
from ....app import db, app

class ContactRepository(IContactRepository):

    def list(self) -> List[Contact]:
        data=ContactSet.query.all()
        contacts = [Contact(x.name,x.birthdate,x.contact_type,x.description) for x in data]
        return contacts


    def get(self,id) -> Contact:
        """Find a Contact by it's ID

        Args:
            id (int): ID of the Contact

        Returns:
            Contact: Contact if is found
        """
        data=ContactSet.query.get(id)
        if data:
            contact = Contact(data.name,data.birthdate,data.contact_type,data.description)
            return contact
        return None

    def create(self,contact: Contact) -> bool:
        """Create a new Contact

        Args:
            contact (Contact): Contact object to persist in the database

        Returns:
            bool: True or False if the persist operation is successfull
        """
        try:
            contact_new=ContactSet(name=contact.name,birthdate=contact.birthdate
                ,contact_type=contact.contact_type, description=contact.description)
            db.session.add(contact_new)
            db.session.commit()
            return True
        except Exception as ex:
            app.logger.error('Error creating a new Contact'.format(ex))
            return False

    def update(self, id, contact: Contact) -> bool:
        """Update the Contact

        Raises:
            NotImplementedError: If not Implemented
        """
        raise NotImplementedError

    def delete(self, id) -> bool:
        """Delete the Contact

        Raises:
            NotImplementedError: If not Implemented
        """
        raise NotImplementedError


class ContactSet(db.Model):
    """Contact Set"""
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    contact_type = Column(Enum(ContactType), nullable=False)
    description = Column(Text)

    # CategoriaId=Column(Integer,ForeignKey('categorias.id'), nullable=False)
    # categoria = relationship("Categorias", backref="Articulos")

    # def __init__(self, name: str, birthdate: datetime,contact_type: ContactType, description: str):
    #     self.name = name
    #     self.birthdate = birthdate
    #     self.contact_type = contact_type
    #     self.description = description

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
