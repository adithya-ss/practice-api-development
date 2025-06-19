from flask import Flask, render_template

app = Flask(__name__, template_folder='templates_static', static_folder='static_files', static_url_path='/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)