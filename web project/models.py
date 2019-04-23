from sqlalchemy import Integer, Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app import db



class CodeName(db.Model):
    __tablename__ = 'codename'
    errorcode = Column(Integer, primary_key=True, nullable=False)
    codename = Column(String(30))
    errortables = db.relationship('ErrorTable', backref='codename', lazy='dynamic')

    def __init__(self, errorcode, codename=None):
        self.errorcode = errorcode
        if codename:
            self.codename = codename
    
    def toDict(self):
       return {
            'errorcode': self.errorcode,
            'codename': self.codename
        }

class ErrorSolution(db.Model):
    __tablename__ = 'errorsolution'
    errorcode = Column(Integer, primary_key=True, nullable=False)
    date = Column(DateTime(), server_default=func.now())
    message = Column(String(256))

    def __init__(self, errorcode, message=None):
        self.errorcode = errorcode
        if message:
            self.message = message

    def toDict(self):
       return {
            'errorcode': self.errorcode,
            'date': self.date,
            'message': self.message
        }

class ErrorTable(db.Model):
    __tablename__ = "errortable"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(30), nullable=False)
    errorcode = Column(Integer, ForeignKey('codename.errorcode'))
    date = Column(DateTime(), server_default=func.now())

    def __init__(self, username, errorcode=None):
        self.username = username
        if errorcode:
            self.errorcode = errorcode


    def toDict(self):
       return {
            'id': self.id,
            'username': self.username,
            'errorcode': self.errorcode,
            'date': self.date
        }

class Registration(db.Model):
    __tablename__ = "registration"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    firstname = Column(String(30))
    lastname = Column(String(30))
    address = Column(String(50))
    email = Column(String(30), unique=True)
    password = Column(String(30))
    phonenumber = Column(Integer)
    dateofbirth = Column(DateTime())
    description = Column(String(100))

    def __init__(self, firstname, lastname=None, address=None, email=None, password=None, phonenumber=None, dateofbirth=None, description=None):
        self.firstname = firstname
        if lastname:
            self.lastname = lastname
        if address:
            self.address = address
        if email:
            self.email = email
        if password:
            self.password = password
        if phonenumber:
            self.phonenumber = phonenumber
        if dateofbirth:
            self.dateofbirth = dateofbirth
        if description:
            self.description = description
