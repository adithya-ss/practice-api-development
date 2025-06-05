from flask import Flask

starter_app = Flask(__name__)

@starter_app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    starter_app.run(host='0.0.0.0', port=5555, debug=True)
    # Debug mode is enabled for development purposes.
    # In production, consider setting debug=False and using a proper WSGI server.
# To run the application, use the command: python starter_app.py
# Make sure to install Flask using: pip install Flask