from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.String(64))
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Text)
    q4 = db.Column(db.String(64))
    q5 = db.Column(db.Text)
    q6 = db.Column(db.String(64))
    q7 = db.Column(db.String(64))
    q8 = db.Column(db.String(64))
    q9 = db.Column(db.String(64))
    q10 = db.Column(db.Text)
    comments = db.Column(db.Text)
