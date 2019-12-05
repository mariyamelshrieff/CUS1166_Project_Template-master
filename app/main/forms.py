# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateTimeField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Length, NumberRange


class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')



class AppointmentForm(FlaskForm):
    appointment_desc = StringField('appointment_desc', validators=[DataRequired()])

    #appointment_title = StringField('appointment_title', validators=[DataRequired()])
    #appointment_customername = StringField('appointment_customername', validators=[DataRequired()])
    #appointment_location = StringField('appointment_location', validators=[DataRequired()])
    #appointment_date = StringField('appointment_date', validators=[DataRequired()])

    appointment_status_completed = SelectField('Status', choices=[('upcoming','Upcoming'),('in progress','In Progress'),('completed','Completed')])
    submit = SubmitField('submit')


class AppointmentCreationForm(FlaskForm):
    title = StringField(
        label='Title',
        validators=[DataRequired(),
                    Length(max=255, min=3, message='Title Allow 2-255 chars')],

    )
    customer = StringField(
        label='Customer',
        validators=[DataRequired(),
                    Length(max=255, min=3, message='Customer Allow 2-255 chars')],)
    location = StringField(
        label='Location',
        validators=[DataRequired(),
                    Length(max=255, min=3, message='Location Allow 2-255 chars')
                    ],
    )
    start_time = DateTimeField(
        label='Date and Start Time',
        validators=[DataRequired()],
        format='%Y-%m-%d %H:%M'
    )
    duration = IntegerField(
        label='Meeting Duration(is Minutes)',
        validators=[DataRequired(),
                    NumberRange(min=10, max=1440, message='Meeting Duration should be Integer and between 10-1440')])
    note = TextAreaField(label='Notes')
    submit = SubmitField('submit')


is_completed_choices = [('Not Completed', 'Not Completed', ('Completed', 'Completed'))]

class AppointmentEditionForm(FlaskForm):
    title = StringField(
        label='Title',
        validators=[DataRequired(),
                    Length(max=255, min=3, message='Title Allow 2-255 chars')],

    )
    customer = StringField(
        label='Customer',
        validators=[DataRequired(),
                    Length(max=255, min=3, message='Customer Allow 2-255 chars')], )
    location = StringField(
        label='Location',
        validators=[DataRequired(),
                    Length(max=255, min=3, message='Location Allow 2-255 chars')
                    ],
    )
    start_time = DateTimeField(
        label='Date and Start Time',
        validators=[DataRequired()],
        format='%Y-%m-%d %H:%M'
    )
    duration = IntegerField(
        label='Meeting Duration(is Minutes)',
        validators=[DataRequired(),
                    NumberRange(min=10, max=1440, message='Meeting Duration should be Integer and between 10-1440')])
    note = TextAreaField(label='Notes')
    is_completed = StringField(
        label='Is Completed',
        validators=[DataRequired()]

                               )
    submit = SubmitField('submit')