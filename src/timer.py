import datetime 
import argparse

class Timer(object):
    """docstring for Timer"""
    def __init__(self):
        super(Timer, self).__init__()
        #self.arg = arg
        a = datetime.datetime.now()
        self.logname = str(a.year) + '-' + str(a.month) + '-' + str(a.day) + ".txt"
        self.logfile = open(self.logname, "a")
        self.oldact = "start"
        self.newact = ""
        self.oldtime = a
        self.newtime = 0

    def update(self, line):
        self.newact = line
        self.newtime = datetime.datetime.now()
        message = ""
        message += self.oldact + "\t" + str(self.oldtime) + "\t" + \
                str(self.newtime) + "\t" + \
                str((self.newtime - self.oldtime).seconds) + "\n"
        self.logfile.write(message)
        self.oldact = self.newact
        self.oldtime = self.newtime

    def stop(self):
        self.logfile.close()
        


def main():

    descStr = "\n  This program is used to time what you do in a daily routing. \n"
    descStr += "  Obviously, without hardware support, what you actually do is only what you say.\n"
    descStr += "  But the programm, which always runs in a single console quietly, may \n"
    descStr += "  give you some pressure to force on what you really do.\n\n"

    parser = argparse.ArgumentParser(description=descStr)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--h', help=descStr)
    args = parser.parse_args()

    timer = Timer()

    while 1:
        line = input()
        #print(line)

        if line == "":
            continue

        timer.update(line)

        if line == "stop":
            timer.stop()
            break

if __name__ == '__main__':
    main()
