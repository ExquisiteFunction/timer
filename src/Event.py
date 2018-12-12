import datetime

class Event(object):
    """docstring for Event"""
    def __init__(self):
        super(Event, self).__init__()
        self.name = ""
        self.start_time = datetime.datetime(2018,12,1)
        self.end_time = datetime.datetime(2018,12,1)
        self.duration = 0