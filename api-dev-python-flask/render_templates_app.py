from flask import Flask, render_template

rendering_template_app = Flask(__name__, template_folder='templates')

@rendering_template_app.route('/')
def index():
    list_of_items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', list_of_items=list_of_items)

@rendering_template_app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    rendering_template_app.run(host='0.0.0.0', debug=True)