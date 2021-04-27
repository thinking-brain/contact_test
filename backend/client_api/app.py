from flask import Flask, render_template, jsonify;
from flask_cors import CORS;
from flasgger import Swagger
import contact.blueprints.contact_blueprint as contact

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
swagger = Swagger(app)
logger = app.logger

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.errorhandler(422)
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
def handle_error(err):
    messages = None
    # if err.code == 404:
    #     messages = {
    #         "general": err.description
    #     }
    # elif err.data:
    #     messages = err.data.get("messages", {
    #         "general": "Invalid request."
    #     })
    # messages_list = []
    # for message_key in messages.keys():
    #     messages_list.append("{}: {}".format(message_key, messages[message_key]))
    #     ('Request ended with error', *{
    #     "code": err.code,
    #     "messages": messages_list,
    # })
    return jsonify({
        "error_code": err.code,
        "errors": err.description
    }), err.code


@app.errorhandler(500)
@app.errorhandler(Exception)
def handle_error(err):
    logger.error(err)
    messages = {
        "general": "Error desconocido."
    }
    messages_list = []
    for message_key in messages.keys():
        messages_list.append("{}: {}".format(message_key, messages[message_key]))
    logger.error('Request ended with error', *{
        "code": 500,
        "messages": messages_list
    })
    return jsonify({
        "error_code": 500,
        "errors": messages_list
    }), 500


@app.after_request
def after_request(response):
    logger.info('Request completed', *{
        "custom_tags": ["service_request"]
    })
    return response


# Adding blueprints
app.register_blueprint(contact.contact_resources)

if __name__ == '__main__':
    app.run(debug=True)

