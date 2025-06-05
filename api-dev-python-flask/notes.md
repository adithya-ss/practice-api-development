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
    