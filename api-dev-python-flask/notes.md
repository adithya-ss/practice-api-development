#### Packages Installed in Virtual Environment:
1. flask: Web framework for building web applications and APIs in Python.
2. flask_restful: Extension for Flask that simplifies building RESTful APIs.
3. flask_sqlalchemy: ORM (Object-Relational Mapping) extension for Flask that integrates SQLAlchemy for database interactions.

----------------------------------------------------------

#### ORM (Object-Relational Mapping)
- A programming technique/method, which allows for developers to interact with a database using object-oriented code instead of writing raw SQL queries. Ex., using the add() method instead of the INSERT query.

----------------------------------------------------------

A Flask application can be run using one of the following 2 commands:
1. python file_name_of_the_app.py
2. flask run --app file_name_of_the_app.py 
    * Optional parameters: --debug or --no-debug / --port=<port_number> / --host=<hostname/ip_address>

### Flask Notes:
* To handle query strings in the URL, we make use of the request.args from the request module from the flask package.
    > from flask import request
* To specify which method of the API call an endpoint would support, use the methods parameter in the app.route.
    > app.route('/route', method(s)=[GET(,POST, PUT, DELETE)])
* To return a custom response, or response code, include it in the return statement in the function of a particular endpoint.
    > return <whatever_to_be_returned>, <custom_status_code>
    <br/>Ex: return my_message, 200
    * To make a full custom reponse, we can make use of the make_response module from flask, by importing it just like the requests module.
    > from flask import make_response

    * And in the implementation (function for endpoint/route):
    > response = make_response('your_response_message')
    <br/> response.status_code = 1234
    <br/> response.headers['content-type'] = 'application/json
    <br/> return response
    * Use the -I flag with the curl command to validate/check the custom message.
    > curl -I http://127.0.0.1:5556/greet/RCB
    
#### Rendering Templates:
* To render a html template in a flask application, we make use of the render_template method, by passing the name of the HTML file intended to be rendered.
* Values can be passed from the App to the HTML file, using parameters to the render_template funtion. The key of the parameter is used to finally render the desired value. Conditions can be applied for rendering a value in the HTML.
* Template can also be rendered using dynamic URL loading. This is done by using the name of the function for a route in the href for an anchor tag.
    > Ex: If the name of the function for route is test, then in the anchor tag, we use `<a href="{{ url_for('test') }}">`
    * We can also make use of the redirect function and set where the redirection has to happen. This can be defined as a route, similar to other routes, but for redirection.
        > Ex: from flask import redirect 
        <br/> @app.route('/redirect')
        <br/> def redirect():
        <br/> &nbsp;&nbsp;&nbsp;&nbsp;return redirect(url_for('page_to_redirect'))

### Filters
* Filters in Jinja can be used to modify or work with the data being passed to the HTML Page.
* There are already pre-exisising (default) filters available, such as lower, upper, replace etc. However, custom filters can also be created.
* Custom filters can be created using the template_filter function on the app, similar to the route function on the app.
    > Ex: app.template_filter('custom_filter')

### Forms and Requests
* When working with forms, it is important to note that the name of the form field is to be used in request.form.get().
* When working with files, we get the file by using request.files.get(), instead of request.forms.get()