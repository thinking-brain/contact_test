from abc import ABC
from typing import List
from ..entities.contact import Contact

class IContactRepository(ABC):
    """Contact repository abstract class
    """

    def list(self) -> List[Contact]:
        """List the Contacts

        Raises:
            NotImplementedError: If not Implemented
        """
        raise NotImplementedError

    def get(self,id) -> Contact:
        """Get a Contact by the ID

        Raises:
            NotImplementedError: If not Implemented
        """
        raise NotImplementedError

    def create(self,contact: Contact) -> bool:
        """Create a new Contact

        Raises:
            NotImplementedError: If not Implemented
        """
        raise NotImplementedError

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
