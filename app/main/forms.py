
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length




class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')


class AppointmentForm(FlaskForm):
    appointment_desc = StringField('appointment_desc', validators=[DataRequired()])

    appointment_title = StringField('appointment_title', validators=[DataRequired()])
    appointment_customer_name = StringField('appointment_customername', validators=[DataRequired()])
    appointment_location = StringField('appointment_location', validators=[DataRequired()])
    appointment_date = StringField('appointment_date', validators=[DataRequired()])

    appointment_status_completed = SelectField('Status', choices=[('Cleaning','Cleaning'),('Repair','Repair'),('Installation','Installation')])

    submit = SubmitField('Add')