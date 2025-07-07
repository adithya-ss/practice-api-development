from flask import Flask, render_template, session, make_response, request

sessions_cookies_app = Flask(__name__, template_folder='templates_sessions_cookies')
sessions_cookies_app.secret_key = 'supersecretkey'

@sessions_cookies_app.route('/')
def index():
    return render_template('index.html', message='Index')

@sessions_cookies_app.route('/set_data')
def set_data():
    session['name'] = 'John Doe'
    session['age'] = 30
    return render_template('index.html', message='Data set in session')

@sessions_cookies_app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'age' in session.keys():
        name = session.get('name', 'Name has not been set')
        age = session.get('age', 'Age has not been set')
        return render_template('index.html', message=f'Name: {name}, Age: {age}')
    else:
        return render_template('index.html', message='No data found in session')
    
@sessions_cookies_app.route('/clear_data')
def clear_data():
    session.clear()
    return render_template('index.html', message='Session data cleared')

@sessions_cookies_app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set'))
    response.set_cookie('username', 'John Doe Cookie Value')
    return response

@sessions_cookies_app.route('/get_cookie')
def get_cookie():
    if 'username' not in request.cookies:
        return render_template('index.html', message='Cookie not found')
    cookie_value = request.cookies.get('username', 'Cookie not found')
    return render_template('index.html', message=f'Cookie Value: {cookie_value}')

@sessions_cookies_app.route('/clear_cookie')
def clear_cookie():
    response = make_response(render_template('index.html', message='Cookie cleared'))
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    sessions_cookies_app.run(host='0.0.0.0', debug=True)