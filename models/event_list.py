from models.event import Event
from datetime import date
event1= Event(2022,12,12,'Big summer Blow out',5000,23,'Biggest summer blow out of the year',True)
event2 = Event(2022,12,25,'Big winter blow in',20,1,'winter is coming, get wild',False)

events=[event1,event2]

def add_event(new_event):
    events.append(new_event)


def add_sticker(recurring):
    if recurring=='one_off':
        return False
    else:
        return True