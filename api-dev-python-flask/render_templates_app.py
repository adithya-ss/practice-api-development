from flask import Flask, render_template

rendering_template_app = Flask(__name__, template_folder='templates')

@rendering_template_app.route('/')
def index():
    list_of_items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', list_of_items=list_of_items)

@rendering_template_app.route('/filters')
def filters():
    sample_text = "This is a sample text to demonstrate filters in Jinja2!"
    return render_template('filters.html', sample_text=sample_text)

@rendering_template_app.template_filter('add_space_between_letters')
def add_space_between_letters(data, my_data=None):
    """Custom filter to add space between letters."""
    return ' '.join(data) + my_data

@rendering_template_app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    rendering_template_app.run(host='0.0.0.0', debug=True)