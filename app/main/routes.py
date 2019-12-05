from flask import render_template,  redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.models import Task
from flask import request, redirect


from app.main.forms import AppointmentForm
from app.models import Appointment
import datetime
from datetime import timedelta


@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("main/index.html")


@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():

        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()


        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)



@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):


    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))




@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():


        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()

        return redirect(url_for('main.todolist'))

    current_task = Task.query.filter_by(task_id=task_id).first_or_404()


    form.task_desc.data =     current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)



@bp.route('/appointment', methods=['GET','POST'])
def appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_appointment = Appointment(appointment_customer_name= form.appointment_customer_name, appointment__date= form.appointment_date,
                                      appointment_status=form.appointment_status_completed, appointment_location= form.appointment_location,
                                      appointment_desc=form.appointment_desc)

        #new_appointment.appointment_customer_name = form.appointment_customer_name.data
        #new_appointment.appointment__date = form.appointment_date.data
        #new_appointment.appointment_status = form.appointment_status_completed.data
        #new_appointment.appointment_location = form.appointment_location.data
        #new_appointment.appointment_desc = form.appointment_desc.data


        db.session.add(new_appointment)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.appointment'))

    new_appointment = db.session.query(Appointment).all()

    return render_template("main/appointment.html", form=form, new_appointment=new_appointment,)


@bp.route('/appointment/remove/<int:appointment_id>', methods=['GET','POST'])
def remove_appointment(appointment_id):


    Appointment.query.filter(Appointment.appointment_id == appointment_id).delete()
    db.session.commit()

    return redirect(url_for('main.appointment'))



@bp.route('/appointment/edit/<int:appointment_id>', methods=['GET','POST'])

def edit_appointment(appointment_id):
    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():

        current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.appointment_desc =  form.appointment_desc.data
        current_appointment.appointment_status = form.appointment_status_completed.data

        current_appointment.appointment_title =  form.appointment_title.data
        current_appointment.appointment_customer_name =  form.appointment_customer_name.data
        current_appointment.appointment_location =  form.appointment_location.data
        current_appointment.appointment_date =  form.appointment_date.data

        db.session.add(current_appointment)
        db.session.commit()

        return redirect(url_for('main.appointment'))


    current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()


    form.appointment_desc.data = current_appointment.appointment_desc
    form.appointment_status_completed.data = current_appointment.appointment_status



    return render_template ("main/appointment_edit_view.html",form=form, appointment_id = appointment_id)