import datetime 

class Timer(object):
    """docstring for Timer"""
    def __init__(self, arg):
        super(Timer, self).__init__()
        #self.arg = arg
        a = datetime.datetime.now()
        self.logname = str(a.year) + '-' + str(a.month) + '-' + str(a.day) + ".txt"
        #print(logname)
        self.logfile = open(logname, "a")
        self.oldact = "start"
        self.newact = ""
        self.oldtime = a
        self.newtime = 0


def main():

    a = datetime.datetime.now()
    logname = str(a.year) + '-' + str(a.month) + '-' + str(a.day) + ".txt"
    #print(logname)
    logfile = open(logname, "a")

    oldact = "start"
    newact = ""
    oldtime = a
    newtime = 0

    while 1:
        line = input()
        #print(line)

        if line == "":
            continue

        newact = line
        newtime = datetime.datetime.now()
        message = ""
        message += oldact + "\t" + str(oldtime) + "\t" + \
                str(newtime) + "\t" + str((newtime - oldtime).seconds) + "\n"
        logfile.write(message)
        oldact = newact
        oldtime = newtime

        if line == "stop":
            logfile.close()
            break

if __name__ == '__main__':
    main()
