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
        contacts = [Contact(x.id,x.name,x.birthdate,x.contact_type,x.description, x.phone) for x in data]
        return contacts


    def get(self,id) -> Contact:
        """Find a Contact by it's ID

        Args:
            id (int): ID of the Contact

        Returns:
            Contact: Contact if was found
        """
        data=ContactSet.query.get(id)
        if data:
            contact = Contact(data.id,data.name,data.birthdate,data.contact_type,data.description, data.phone)
            return contact
        return None

    def create(self,contact: Contact) -> bool:
        """Create a new Contact

        Args:
            contact (Contact): Contact object to persist in the database

        Returns:
            bool: True or False if the persist operation was successfull
        """
        try:
            contact_new=ContactSet(name=contact.name,birthdate=contact.birthdate
                ,contact_type=contact.contact_type, description=contact.description, phone=contact.phone)
            db.session.add(contact_new)
            db.session.commit()
            return True
        except Exception as ex:
            app.logger.error('Error creating a new Contact. {}'.format(ex))
            return False

    def update(self, id, contact: Contact) -> bool:
        """Update the Contact

        Args:
            id (int): ID of the Contact object to update
            contact (Contact): Contact object to update in the database

        Returns:
            bool: True or False if the update operation was successfull
        """
        try:
            data=ContactSet.query.get(id)
            data.name = contact.name
            data.birthdate = contact.birthdate
            data.contact_type = contact.contact_type
            data.description = contact.description
            data.phone = contact.phone
            db.session.commit()
            return True
        except Exception as ex:
            app.logger.error('Error updating a Contact. {}'.format(ex))
            return False

    def delete(self, id) -> bool:
        """Delete the Contact

        Args:
            id (int): ID of the Contact object to delete

        Returns:
            bool: True or False if the delete operation was successfull
        """
        try:
            data=ContactSet.query.get(id)
            db.session.delete(data)
            db.session.commit()
            return True
        except Exception as ex:
            app.logger.error('Error deleting a Contact. {}'.format(ex))
            return False


class ContactSet(db.Model):
    """Contact Set"""
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    contact_type = Column(Enum(ContactType), nullable=False)
    description = Column(Text,nullable=True)
    phone = Column(Text,nullable=True)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
