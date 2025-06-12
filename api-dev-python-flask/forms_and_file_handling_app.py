import pandas as pd
from flask import Flask, render_template, request, Response

forms_and_file_app = Flask(__name__, template_folder='templates_forms')

@forms_and_file_app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')

        if username == 'testuser' and password == 'testpassword':
            return f"Login successful for {username}!"
        else:
            return f"Login failed for {username}!"

#TODO: Create a seperate endpoint for login, so that index accepts only GET requests.

@forms_and_file_app.route('/file_upload', methods=['POST'])
def file_upload():
    uploaded_file = request.files.get('File')
    if uploaded_file:
        if uploaded_file.content_type == 'text/plain':
            # Process text file
            return uploaded_file.read().decode('utf-8')
        if uploaded_file.content_type == 'application/vnd.ms-excel' or uploaded_file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            # Process Excel file
            dataframe = pd.read_excel(uploaded_file)
            return dataframe.to_html()

@forms_and_file_app.route('/convert_csv', methods=['POST'])
def convert_csv():
    uploaded_file = request.files.get('File')
    if uploaded_file:
        dataframe = pd.read_excel(uploaded_file)
        response = Response(
            dataframe.to_csv(),
            mimetype='text/csv',
            headers={"Content-disposition": "attachment; filename=converted_file.csv"}
        )
        return response
    return "No file uploaded or unsupported file type."

if __name__ == '__main__':
    forms_and_file_app.run(host='0.0.0.0', debug=True)