from ..entities.contact import Contact, ContactType
import json
from ..repositories.contact_repository import IContactRepository
from datetime import datetime
from flask import Blueprint
from flask.json import jsonify
from injector import inject
from marshmallow import fields, validate
from webargs.flaskparser import use_args, use_kwargs

contact_resources = Blueprint(
    "contact_resources",
    __name__,
    url_prefix="/contact")
# contact_resources.json_encoder = FlaskCustomJsonEncoder
# enable_cors(contact_resources)

class ContactJsonEncoder(json.JSONEncoder):
    @staticmethod
    def to_json(obj: Contact):
        return {
              'id': obj.id,
              'name': obj.name,
              'birthdate': obj.birthdate.strftime('%Y-%m-%d'),
              'contact_type': '{}'.format(obj.contact_type.value),
              'description': obj.description,
              'phone': obj.phone,
            }

@contact_resources.route("/", methods=["GET"])
@inject
def list( contact_repo: IContactRepository, *args, **kwargs):
    """List all Contacts.
    ---
    tags:
      - Contacts
    definitions:
      Contact:
        type: object
        properties:
          id:
            type: number
            description: ID of the Contact.
          name:
            type: string
            description: Name of the Contact.
          birthdate:
            type: date
            description: Birthday of the Contact.
          contact_type:
            type: string
            description: Type of the Contact.
          description:
            type: string
            description: Description of the Contact
          phone:
            type: string
            description: Phone number of the Contact
    responses:
      200:
        description: Return a list of the contacts.
        content:
            application/json:
              schema:
                type: array
                $ref: '#/definitions/Contact'
    """

    contacts = contact_repo.list()
    return jsonify([ContactJsonEncoder.to_json(x) for x in contacts])

@contact_resources.route("/<id>", methods=["GET"])
@inject
def get(contact_repo: IContactRepository,*args, **kwargs):
    """Get a Contact by his ID.
    ---
    tags:
      - Contacts
    parameters:
      - name: id
        in: path
        type: number
        description: ID of the Contact.
        required: true
        example: 1
    responses:
      200:
        description: Return tha Contact that has the ID requested.
        schema:
          $ref: '#/definitions/Contact'
    """
    id = kwargs['id']
    contact = contact_repo.get(id)
    if contact is not None:
        return ContactJsonEncoder.to_json(contact)
    return None

@contact_resources.route("/", methods=["POST"])
@use_kwargs(
    {
        "name":
        fields.Str(required=True),
        "birthdate":
        fields.Date(required=True),
        "contact_type":
        fields.Str(required=True),
        "description":
        fields.Str(required=False),
        "phone":
        fields.Str(required=False)
    },
    error_status_code=400)
@inject
def create(contact_repo: IContactRepository,*args, **kwargs):
    """Create a new Contact.
    ---
    tags:
      - Contacts
    parameters:
      - name: payload
        in: body
        description: JSON like payload.
        schema:
          type: object
          required:
            - name
            - birthdate
            - contact_type
          properties:
            name:
              type: string
              example: 'Your Name'
            birthdate:
              type: date
              example: 1987-06-07
            contact_type:
              type: number
              enum: [1, 2, 3]
              example: 1
            description:
              type: string
            phone:
              type: string
    definitions:
      StatusResponse:
        type: object
        properties:
          status:
            type: boolean
            description: Indicate if the resquest was successfull.
          description:
            type: string
            description: Description of the response
    responses:
      200:
        description: Return successfull response.
        schema:
          $ref: '#/definitions/StatusResponse'
    """
    name = kwargs['name']
    birthdate = kwargs['birthdate']
    contact_type = kwargs['contact_type']
    description = kwargs['description'] if 'description' in kwargs else None
    phone = kwargs['phone'] if 'phone' in kwargs else None
    contact = Contact(0,name,birthdate,contact_type,description, phone)
    result = contact_repo.create(contact)
    if result:
        return {
          'status': True,
          'description': 'Contact Created successfully.'
      }
    else:
          return {
          'status': False,
          'description': 'Error occurred when creating Contact.'
      }

@contact_resources.route("/<id>", methods=["PUT"])
@use_kwargs(
    {
        "name":
        fields.Str(required=True),
        "birthdate":
        fields.Date(required=True),
        "contact_type":
        fields.Str(required=True),
        "description":
        fields.Str(required=False),
        "phone":
        fields.Str(required=False)
    },
    error_status_code=400)
@inject
def update(contact_repo: IContactRepository,*args, **kwargs):
    """Update an existed Contact.
    ---
    tags:
      - Contacts
    parameters:
      - name: payload
        in: body
        description: JSON like payload.
        schema:
          type: object
          required:
            - name
            - birthdate
            - contact_type
          properties:
            name:
              type: string
              example: 'Your Name'
            birthdate:
              type: date
              example: 1987-06-07
            contact_type:
              type: string
              enum: [1, 2, 3]
              example: 1
            description:
              type: string
            phone:
              type: string
    responses:
      200:
        description: Return successfull response.
        schema:
          $ref: '#/definitions/StatusResponse'
    """
    id = kwargs['id']
    name = kwargs['name']
    birthdate = kwargs['birthdate']
    contact_type = kwargs['contact_type']
    description = kwargs['description'] if 'description' in kwargs else None
    phone = kwargs['phone'] if 'phone' in kwargs else None
    contact = Contact(id,name,birthdate,contact_type,description, phone)
    result = contact_repo.update(id, contact)
    if result:
        return {
          'status': True,
          'description': 'Contact Updated successfully.'
      }
    else:
          return {
          'status': False,
          'description': 'Error occurred when updating Contact.'
      }

@contact_resources.route("/<id>", methods=["DELETE"])
@inject
def delete(contact_repo: IContactRepository,*args, **kwargs):
    """Delete an existing Contact.
    ---
    tags:
      - Contacts
    parameters:
      - name: id
        in: path
        type: number
        description: ID of the Contact.
        required: true
        example: 1
    responses:
      200:
        description: Return successfull response.
        schema:
          $ref: '#/definitions/StatusResponse'
    """
    id = kwargs['id']
    result = contact_repo.delete(id)
    if result:
        return {
          'status': True,
          'description': 'Contact Deleted successfully.'
      }
    else:
          return {
          'status': False,
          'description': 'Error occurred when deleting Contact.'
      }
