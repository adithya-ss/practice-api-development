from flask import Flask, request, make_response

learner_app = Flask(__name__)

@learner_app.route('/')
def index():
    return "Hello, World!"

@learner_app.route('/welcome')
def welcome():
    return "Welcome to the Flask API!"

@learner_app.route('/goodbye')
def goodbye():
    return "Goodbye from the Flask API!"

@learner_app.route('/greet/<name>')
def greet(name):
    my_custom_reponse = make_response(f"Hello, {name}!")
    my_custom_reponse.headers['Content-Type'] = 'text/plain'
    my_custom_reponse.headers['Content-Length'] = 20
    my_custom_reponse.status_code = 202
    return my_custom_reponse

@learner_app.route('/handle_url_paramters')
def handle_url_parameters():
    if 'name' in request.args.keys() and 'message' in request.args.keys():
        name = request.args.get('name', 'Guest')
        message = request.args.get('message', 'Hey, there!')
        return f"{name}: {message}"
    else:
        return "Please provide both 'name' and 'message' parameters."


if __name__ == '__main__':
    learner_app.run(host='0.0.0.0', port=5556, debug=True)
# To run the Flask application, use the command: python learner_app.py