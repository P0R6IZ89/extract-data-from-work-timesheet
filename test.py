from flask import Flask
from flask_sqlalchemy import SQLAlchemy,

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=True)
    user_password = db.Column(db.Integer, unique=False, nullable=True)
    time_line_elem = db.Column(db.Text)
    information_elem = db.Column(db.Text)
    days_list= db.Column(db.Text)

    def __repr__(self):
        return f"User('{self.id}', '{self.user_id}', '{self.user_password}', '{self.time_line_elem}', '{self.information_elem}', '{self.days_list}')"