from datetime import datetime
from flask import Blueprint
from flask.json import jsonify
import inject
from marshmallow import fields, validate
from webargs.flaskparser import use_args, use_kwargs

contact_resources = Blueprint(
    "contact_resources",
    __name__,
    url_prefix="/contact")
# contact_resources.json_encoder = FlaskCustomJsonEncoder
# enable_cors(contact_resources)

@contact_resources.route("/", methods=["GET"])
@inject.autoparams()
def list(*args, **kwargs):
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
    responses:
      200:
        description: Return a list of the contacts.
        content:
            application/json:
              schema:
                type: array
                $ref: '#/definitions/Contact'
    """

    example_contact = {
        'name': 'Name',
        'birthdate': datetime(2021,2,12),
        'contact_type': 'type1',
        'description': 'Description of the Contact',
    }
    contacts = [example_contact]
    return jsonify(contacts)

@contact_resources.route("/<id>", methods=["GET"])
@use_kwargs(
    {
        "id":
        fields.Int(required=True)
    },
    error_status_code=400)
@inject.autoparams()
def get(*args, **kwargs):
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
    contact = {
        'name': 'Name',
        'birthdate': '2021-02-01',
        'contact_type': 'type1',
        'description': 'Description od the Contact',
    }
    return contact

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
        fields.Str(required=False)
    },
    error_status_code=400)
@inject.autoparams()
def create(*args, **kwargs):
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
              type: string
              enum: ['type1', 'type2', 'type3']
              example: 'type1
            description:
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
    return {
        'status': True,
        'description': 'Contact Created successfully.'
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
        fields.Str(required=False)
    },
    error_status_code=400)
@inject.autoparams()
def update(*args, **kwargs):
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
              enum: ['type1', 'type2', 'type3']
              example: 'type1
            description:
              type: string
    responses:
      200:
        description: Return successfull response.
        schema:
          $ref: '#/definitions/StatusResponse'
    """
    return {
        'status': True,
        'description': 'Contact Updated successfully.'
    }

@contact_resources.route("/<id>", methods=["DELETE"])
@use_kwargs(
    {
        "name":
        fields.Str(required=True),
        "birthdate":
        fields.Date(required=True),
        "contact_type":
        fields.Str(required=True),
        "description":
        fields.Str(required=False)
    },
    error_status_code=400)
@inject.autoparams()
def delete(*args, **kwargs):
    """Create a new Contact.
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
    return {
        'status': True,
        'description': 'Contact Deleted successfully.'
    }
