import datetime
import os

class Event(object):
    """docstring for Event"""
    def __init__(self):
        super(Event, self).__init__()
        self.name = ""
        self.start_time = datetime.datetime(2018,12,1)
        self.end_time = datetime.datetime(2018,12,1)
        self.duration = 0

class Timer(object):
    """docstring for Timer"""
    def __init__(self):
        super(Timer, self).__init__()
        self.logname = str(datetime.date.today()) + ".txt"
        self.logfile = None
        self.oldact = "start"
        self.newact = ""
        self.oldtime = datetime.datetime.now()
        self.newtime = 0

    def update(self, line):
        self.newact = line
        self.newtime = datetime.datetime.now()
        message = self.oldact + "\t"
        message += str(self.oldtime) + "\t"
        message += str(self.newtime) + "\t"
        message += str((self.newtime - self.oldtime).seconds) + "\n"
        self.logfile = open("../log/" + self.logname, "a")
        self.logfile.write(message)
        self.logfile.close()
        self.oldact = self.newact
        self.oldtime = self.newtime

    def stop(self):
        return

    def alarm(self, duration, mode):
        import time
        time.sleep(duration)
        
        if "txt" == mode:
            print("Time out.\n")
        elif "audio" == mode:
            from pygame import mixer
            mixer.init()
            mixer.music.load('../Wake-up-sounds/LINE.mp3')
            mixer.music.play()
            time.sleep(2)
            # import subprocess
            # subprocess.Popen(['mpg123', '-q', '../Wake-up-sounds/LINE.mp3'])#.wait()
            # time.sleep(2)

            #TODO

    def insert(self, date, iterm, starttime, stoptime):
        pass

    def statistics(self, iterm, start_date, end_date):
        #start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d")
        #end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")

        l = []
        for dirpath, dirnames, filenames in os.walk(os.getcwd() + "/../log/"):
            for filepath in filenames:
                filedate = datetime.datetime.strptime(filepath.split('.')[0], "%Y-%m-%d").date()
                if filedate >= start_date and filedate <= end_date:
                    with open(os.path.join(dirpath, filepath), 'r') as f:
                        for line in f.readlines():
                            entry = line.split("\t")
                            event = Event()
                            event.name = entry[0].lower()
                            event.start_time = datetime.datetime.strptime(entry[1], "%Y-%m-%d %H:%M:%S.%f")
                            event.end_time = datetime.datetime.strptime(entry[2], "%Y-%m-%d %H:%M:%S.%f")
                            event.duration = (event.end_time-event.start_time).seconds
                            l.append(event)
        duration = sum([e.duration for e in l if iterm in e.name])
        print(duration, "seconds.")
        print(duration/3600.0, "hours.")
        return duration
