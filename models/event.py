from datetime import date
class Event():
    def __init__(self,year,month,day,name,num_guests,room,description,recurring):
        self.date=date(year,month,day)
        self.name=name
        self.num_guest=num_guests
        self.room=room
        self.description=description
        self.recurring=recurring
