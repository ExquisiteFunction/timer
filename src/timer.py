import datetime 
import argparse

class Timer(object):
    """docstring for Timer"""
    def __init__(self):
        super(Timer, self).__init__()
        #self.arg = arg
        self.logname = str(datetime.date.today()) + ".txt"
        self.logfile = open("../log/" + self.logname, "a")
        self.oldact = "start"
        self.newact = ""
        self.oldtime = datetime.datetime.now()
        self.newtime = 0
        return 

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
        return

    def stop(self):
        self.logfile.close()
        return

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
        return

def argsParse():
    descStr = "\n  This program is used to time what you do in a daily routing. \n"
    descStr += "  Obviously, without hardware support, what you actually do is only what you say.\n"
    descStr += "  But the programm, which always runs in a single console quietly, may \n"
    descStr += "  give you some pressure to force on what you really do.\n\n"

    ver_help = "print the version number and exit\n"
    remind_help = "remind you after some time. s for second, m for minute and h for hours.\n"
    remind_type_help = "the type you like to remind you when time out, txt or audio, the latter depends on pygame.\n"

    parser = argparse.ArgumentParser(description=descStr)
    #group = parser.add_mutually_exclusive_group()

    parser.add_argument('-v', action='store_true', required=False, help=ver_help)
    parser.add_argument('-r', action='store', dest='duration', required=False, help=remind_help)
    parser.add_argument('-t', action='store', dest='type', required=False, help=remind_type_help)
    # nargs='?', const = 'audio', 
    args = parser.parse_args()

    return args

        
def main():

    args = argsParse()
    
    timer = Timer()

    if args.v:
        print("Version 0.3.")
        return

    if args.duration:
        print(args.duration)
        d = int(args.duration[:-1])
        if args.type in ['txt', 'audio']:
            timer.alarm(d, args.type)
        else:
            print("invalid type.")
        return

    while 1:
        line = input()

        if line == "":
            continue

        timer.update(line)

        if line == "stop":
            timer.stop()
            break

if __name__ == '__main__':
    main()
