import datetime

class Timer(object):
    """docstring for Timer"""
    def __init__(self):
        super(Timer, self).__init__()
        self.logname = str(datetime.date.today()) + ".txt"
        self.logfile = open("../log/" + self.logname, "a")
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
        self.logfile.write(message)
        self.oldact = self.newact
        self.oldtime = self.newtime

    def stop(self):
        self.logfile.close()

    def alarm(self, duration, mode):
        import time
        time.sleep(duration)
        
        if "txt" == mode:
            print("Time out.\n")
        elif "audio" == mode:
            from pygame import mixer
            mixer.init()
            mixer.music.load('../Wake-up-sounds/Wake-up-sounds.mp3')
            mixer.music.play()
            time.sleep(2)
