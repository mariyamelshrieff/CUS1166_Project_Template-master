#from flask import url_for
from app import db
from datetime import datetime


class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

class Appointment(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_desc = db.Column(db.String(128), index=True)
    appointment_status = db.Column(db.String(128))
    appointment_title = db.Column(db.String, unique=True, nullable=False)
    appointment_customer_name = db.Column(db.String, nullable=False)
    appointment_location = db.Column(db.String, nullable=False)
    appointment__date = db.Column(db.DateTime, default=datetime.now)

