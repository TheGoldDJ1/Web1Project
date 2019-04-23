from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import json
# import yaml

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)
db = SQLAlchemy(app)


@app.before_first_request
def setup():
    db.Model.metadata.drop_all(bind=db.engine)
    db.Model.metadata.create_all(bind=db.engine)

# When the Flask app is shutting down, close the database session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

from models import CodeName, ErrorSolution, ErrorTable, Registration


@app.route("/")
def hello():
    return render_template('homePage.html')

# ErrorTable table
@app.route('/errortable', methods=['GET'])
def show_all_errors():
    print(request)
    records = ErrorTable.query.all()
    records = list(map(lambda x: x.toDict(), records))
    response = jsonify(records)
    response.status_code = 200
    return response

@app.route('/errortable', methods=['POST'])
def save_errors():
    if request.content_type  == 'application/json':
        request_text = request.json
        if 'username' in request_text:
            print(request_text)
            p = ErrorTable(request_text['username'])
        else:
            response = jsonify({'message': 'Invalid fields specified'})
            response.status_code = 400
            return response

        if 'errorcode' in request_text:
            p.errorcode = request_text['errorcode']

        db.session.add(p)
        db.session.commit()
        response = jsonify({
            'id': p.id,
            'username': p.username,
            'errorcode': p.errorcode
        })
        response.status_code = 201
        return response
    else:
        response = jsonify({'message': 'Invalid format of data in the request'})
        response.status_code = 400
        return response

# CodeName Table
@app.route('/codename', methods=['GET'])
def show_all_errorcodes():
    print(request)
    records = CodeName.query.all()
    records = list(map(lambda x: x.toDict(), records))
    response = jsonify(records)
    response.status_code = 200
    return response

@app.route('/codename', methods=['POST'])
def save_errorcodes():
    if request.content_type  == 'application/json':
        request_text = request.json
        if 'errorcode' in request_text:
            print(request_text)
            p = CodeName(request_text['errorcode'], request_text['codename'])
        else:
            response = jsonify({'message': 'Invalid fields specified'})
            response.status_code = 400
            return response

        # if 'codename' in request_text:
        #     p.codename = request_text['codename']

        db.session.add(p)
        db.session.commit()
        response = jsonify({
            'errorcode': p.errorcode,
            'codename': p.codename
        })
        response.status_code = 201
        return response
    else:
        response = jsonify({'message': 'Invalid format of data in the request'})
        response.status_code = 400
        return response


# ErrorSolution Table
@app.route('/errorsolution', methods=['GET'])
def show_all_errorsolutions():
    print(request)
    records = ErrorSolution.query.all()
    records = list(map(lambda x: x.toDict(), records))
    response = jsonify(records)
    response.status_code = 200
    return response

@app.route('/errorsolution', methods=['POST'])
def save_errorsolutions():
    if request.content_type  == 'application/json':
        request_text = request.json
        if 'errorcode' in request_text:
            print(request_text)
            p = ErrorSolution(request_text['errorcode'], request_text['message'])
        else:
            response = jsonify({'message': 'Invalid fields specified'})
            response.status_code = 400
            return response

        # if 'codename' in request_text:
        #     p.codename = request_text['codename']

        db.session.add(p)
        db.session.commit()
        response = jsonify({
            'errorcode': p.errorcode,
            'message': p.message
        })
        response.status_code = 201
        return response
    else:
        response = jsonify({'message': 'Invalid format of data in the request'})
        response.status_code = 400
        return response

@app.route("/home-page", methods=["GET"])
def show_home():
    return render_template("homePage.html")

@app.route("/chart-page", methods=["GET"])
def show_charts():
    return render_template("chart.html")

@app.route("/topics-page", methods=["GET"])
def show_topics():
    return render_template("topics.html")

@app.route("/IO-page", methods=["GET"])
def show_IO():
    return render_template("IO-problem.html")

@app.route("/registration", methods=['GET', 'POST'])
def registration():

    if request.form:
        try:
            person = Registration(firstname=request.form.get("firstname"),lastname = request.form.get("lastname"), address = request.form.get("Address"), email = request.form.get("Email"),  password = request.form.get("Password"), phonenumber = request.form.get("Phone Number"), dateofbirth = request.form.get("dateofBirth"), description = request.form.get("message"))
            db.session.add(person)
            db.session.commit()
            return redirect("home-page")
        except Exception as e:
            print("Failed to add person")
            print(e)


    return render_template('registerPage.html')