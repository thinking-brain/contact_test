from flask import Flask, render_template, jsonify;
from flask_cors import CORS;
from flasgger import Swagger
from .contact.blueprints import contact_blueprint as contact
from .contact.repositories.contact_repository import IContactRepository
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_injector import FlaskInjector
from . import config



app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
swagger = Swagger(app)
logger = app.logger

#  Config
app.config.from_object(config)

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importando Entidades
# from .contact.entities.contact import Contact
from .contact.infrastructure.repositories.contact_repository import ContactRepository

# Inject
def configure(binder):
    binder.bind(IContactRepository,to=ContactRepository)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.errorhandler(422)
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
def handle_error(err):
    logger.error(err)
    messages = None
    if err.code == 404:
        messages = {
            "general": err.description
        }
    elif err.data:
        messages = err.data.get("messages", {
            "general": "Invalid request."
        })
    messages_list = []
    for message_key in messages.keys():
        messages_list.append("{}: {}".format(message_key, messages[message_key]))
    return jsonify({
        "error_code": err.code,
        "errors": messages_list
    }), err.code


@app.errorhandler(500)
@app.errorhandler(Exception)
def handle_error(err):
    messages = {
        "general": "Server Error. {}".format(err)
    }
    logger.error("Server Error. {}".format(err))
    return jsonify({
        "error_code": 500,
        "errors": messages
    }), 500


@app.after_request
def after_request(response):
    logger.info('Request completed', *{
        "custom_tags": ["service_request"]
    })
    return response


# Adding blueprints
app.register_blueprint(contact.contact_resources)

FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True)

