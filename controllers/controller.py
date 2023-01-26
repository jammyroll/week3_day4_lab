from flask import render_template,request
from app import app
from models.event_list import events, add_event, add_sticker
from models.event import Event
from datetime import datetime

@app.route('/events')
def index():
    return render_template('index.html',title='Home',events=events)

@app.route('/events',methods=["POST"])
def add_task():
    event_name=request.form['name']
    event_date=datetime.strptime(request.form['date'],'%Y-%m-%d')
    event_day=event_date.day
    event_month=event_date.month
    event_year=event_date.year
    event_guest_num=request.form['num_guest']
    event_room=request.form['room']
    event_desc=request.form['description']
    event_type=request.form['recurring']
    event_type=add_sticker(event_type)
    print(event_type)
    new_event= Event(event_year,event_month,event_day,event_name,event_guest_num,event_room,event_desc,event_type)
    add_event(new_event)
    return render_template('index.html',title='Home',events=events)