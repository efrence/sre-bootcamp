import base64
import json
import jwt
import hashlib
from sqlalchemy import Column, String
import db

class User(db.Base):
    __tablename__ = 'users'
    username=Column(String, primary_key=True)
    password=Column(String)
    salt=Column(String)
    role=Column(String)
    def __init__(self, password, salt, role):
        self.password = password
        self.salt = salt
        self.role = role

# These functions need to be implemented
class Token:
    def generate_token(self, username, password):
        # check if user exist based on credentials
        token = False
        store_pass = False
        user = db.session.query(User).get(username)
        if user is not None:
            passsalted = '{}{}'.format(password,user.salt)
            store_pass = hashlib.sha512(passsalted.encode()).hexdigest()
        if user is not None and store_pass is not False and store_pass == user.password:
            # use user role to generate the payload
            token = jwt.encode({"role":user.role},"my2w7wjd7yXF64FIADfJxNs1oupTGAuW",algorithm="HS256")
            # return 400
        return token


class Restricted:
    def access_data(self, authorization):
        try:
            payload = jwt.decode(authorization, 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW',algorithms=['HS256'])
            if payload['role'] == 'admin':
                return 'You are under protected data'
            else:
                return False
        except:
            return False
