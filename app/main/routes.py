from flask import render_template,  redirect, url_for, request
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.models import Task, Appointment

from app.main.forms import AppointmentForm, AppointmentCreationForm, AppointmentEditionForm
from app.models import Appointment
from datetime import timedelta, datetime

# Main route of the applicaitons.
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main/index.html")


#
#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)


#
# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):

    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))


#
# Route for editing a task

@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data =     current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)


#  Route for viewing and adding new appointments.
@bp.route('/appointment', methods=['GET','POST'])
def appointment():
    # form = AppointmentForm()
    #
    # if form.validate_on_submit():
    #     # Get the data from the form, and add it to the database.
    #     new_appointment = Appointment()
    #     new_appointment.appointment_desc =  form.appointment_desc.data
    #     new_appointment.appointment_status = form.appointment_status_completed.data
    #     db.session.add(new_appointment)
    #     db.session.commit()
    #
    #     # Redirect to this handler - but without form submitted - gets a clear form.
    #     return redirect(url_for('main.appointment'))
    #
    #     #appointment_title = request.form.get("title")
    #     #appointment_location = request.form.get("location")
    #     #dt = request.form.get("date-time")
    #     #ft = '%Y-%m-%dT%H:%M'
    #     #result = datetime.strptime(dt, ft)
    #
    # new_appointment = db.session.query(Appointment).all()
    #
    # return render_template("main/appointment.html",new_appointment = new_appointment,form= form)
    return redirect(url_for('main.app_list'))

#
# Route for removing a appointment
@bp.route('/appointment/remove/<int:appointment_id>', methods=['GET','POST'])
def remove_appointment(appointment_id):

    # Query database, remove items
    Appointment.query.filter(Appointment.appointment_id == appointment_id).delete()
    db.session.commit()

    return redirect(url_for('main.appointment'))

# Route for editing a appointment

# @bp.route('/appointment/edit/<int:appointment_id>', methods=['GET','POST'])
# def edit_appointment(appointment_id):
#     form = AppointmentForm()
#     print(form.validate_on_submit())
#     if form.validate_on_submit():
#         # Get the data from the form, and add it to the database.
#
#         current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
#         current_appointment.appointment_desc =  form.appointment_desc.data
#         current_appointment.appointment_status = form.appointment_status_completed.data
# #
#         #current_appointment.appointment_title =  form.appointment_title.data
#         #current_appointment.appointment_customername =  form.appointment_customername.data
#         #current_appointment.appointment_location =  form.appointment_location.data
#         #current_appointment.appointment_date =  form.appointment_date.data
#
#         db.session.add(current_appointment)
#         db.session.commit()
#         # After editing, redirect to the view page.
#         return redirect(url_for('main.appointment'))
#
#     # get appointment for the database.
#     current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
#
#     # update the form model in order to populate the html form.
#     form.appointment_desc.data =     current_appointment.appointment_desc
#     form.appointment_status_completed.data = current_appointment.appointment_status
# #
#     #form.appointment_title.data =     current_appointment.appointment_title
#     #form.appointment_customername.data =     current_appointment.appointment_customername
#     #form.appointment_location.data =     current_appointment.appointment_location
#     #form.appointment_date.data =     current_appointment.appointment_date
#
#     return render_template("main/appointment_edit_view.html",form=form, appointment_id = appointment_id)


@bp.route('/appointment/create', methods=['post', 'get'])
def app_create():
    print('hello')
    form = AppointmentCreationForm()
    if form.validate_on_submit():
        appointment = Appointment(
            title=form.title.data,
            customer=form.customer.data,
            location=form.location.data,
            start_time=form.start_time.data,
            duration=form.duration.data,
            note=form.note.data,
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('main.app_list', _id=appointment.id))
    return render_template('main/appointment_create.html', form=form, title='Appointment Creation')


@bp.route('/appointment/edit/<int:_id>', methods=['post', 'get'])
def app_edit(_id):
    a = Appointment.query.get_or_404(_id)
    form = AppointmentEditionForm(
        title=a.title,
        customer=a.customer,
        location=a.location,
        start_time=a.start_time,
        duration=a.duration,
        note=a.note,
        is_completed=a.is_completed

    )

    if form.validate_on_submit():

        a.title = form.title.data
        a.customer = form.customer.data
        a.location = form.location.data
        a.start_time = form.start_time.data
        a.duration = form.duration.data
        a.note = form.note.data
        a.is_completed = form.is_completed.data

        db.session.add(a)
        db.session.commit()
        return redirect(url_for('main.app_view', _id=a.id))
    print(request.method, 'a.is_completed', a.is_completed, form.is_completed.data)
    return render_template('main/appointment_edit.html', form=form, title='Appointment Edit')


@bp.route('/appointment/delete/<int:_id>')
def app_delete(_id):
    a = Appointment.query.get_or_404(_id)
    db.session.delete(a)
    db.session.commit()
    return redirect(url_for('main.app_list'))


@bp.route('/appointment/list')
def app_list():
    query = Appointment.query.order_by(Appointment.id.desc())
    title = request.args.get('title')
    if title:
        query = query.filter(Appointment.title.like('%{}%'.format(title)))
    customer = request.args.get('customer')
    if customer:
        query = query.filter(Appointment.customer.like('%{}%'.format(customer)))
    location = request.args.get('location')
    if location:
        query = query.filter(Appointment.location.like('%{}%'.format(location)))
    note = request.args.get('note')
    if note:
        query = query.filter(Appointment.note.like('%{}%'.format(note)))
    begin = request.args.get('begin')
    try:
        datetime.strptime(begin, '%Y-%m-%d %H:%M')
    except (ValueError, TypeError):
        begin = None

    if begin:
        print(query.count())
        print('query begin', begin)
        query = query.filter(Appointment.start_time >= begin)
        print(query.count())

    end = request.args.get('end')
    try:
        datetime.strptime(end, '%Y-%m-%d %H:%M')
    except (ValueError, TypeError):
        end = None
    if end:
        query = query.filter(Appointment.start_time <= end)

    is_completed = request.args.get('is_completed')
    if is_completed not in ['Not Completed', 'Completed']:
        is_completed = None
    if is_completed:
        print('query is_completed', is_completed)
        query = query.filter(Appointment.is_completed == is_completed)

    page = request.args.get('page', 1)
    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1
    if page <= 0:
        page = 1
    per_page = request.args.get('per_page')
    try:
        per_page = int(per_page)
    except (TypeError, ValueError):
        per_page = 20
    if isinstance(per_page, int) and per_page >= 5:
        pass
    else:
        per_page = 20
    is_overdue = request.args.get('is_overdue')
    if is_overdue == 'Overdue':
        max_per_page = query.count()
    elif is_overdue == 'Not Overdue':
        max_per_page = query.count()
    else:
        is_overdue = None
        max_per_page = 100
    if max_per_page < 100:
        max_per_page = 100

    ls = query.paginate(
        page=page, per_page=per_page, max_per_page=max_per_page, error_out=False
    )
    print(locals())
    return render_template('main/appointment_list.html', ls=ls, is_overdue=is_overdue)


@bp.route('/appointment/view/<int:_id>', methods=['get'])
def app_view(_id):
    a = Appointment.query.get_or_404(_id)
    form = AppointmentEditionForm(
        title=a.title,
        customer=a.customer,
        location=a.location,
        start_time=a.start_time,
        duration=a.duration,
        note=a.note,
        is_completed=a.is_completed
    )
    return render_template('main/appointment_view.html', form=form, title='Appointment View', a=a)