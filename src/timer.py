import argparse
import datetime

from Timer import Timer, Event

def argsParse():
    descStr = "\n  This program is used to time what you do in a daily routing. \n"
    descStr += "  Obviously, without hardware support, what you actually do is only what you say.\n"
    descStr += "  But the programm, which always runs in a single console quietly, may \n"
    descStr += "  give you some pressure to force on what you really do.\n\n"

    ver_help = "print the version number and exit\n"
    remind_help = "remind you after some time. s for second, m for minute and h for hours.\n"
    remind_type_help = "the type you like to remind you when time out, txt or audio, the latter depends on pygame.\n"
    statistics_help = "statistics the total time that you have spent on one thing, dafult as current week.\n"
    start_date_help = "starting date for statistics, in the form of 'YYYY-MM-DD'.\n"
    end_date_help = "ending date for statistics, in the form of 'YYYY-MM-DD'.\n"""
    parser = argparse.ArgumentParser(description=descStr)
    #group = parser.add_mutually_exclusive_group()

    parser.add_argument('-v', action='store_true', required=False, help=ver_help)
    parser.add_argument('-r', action='store', dest='duration', required=False, help=remind_help)
    parser.add_argument('-t', action='store', dest='type', required=False, help=remind_type_help)
    parser.add_argument("-stat", action="store", dest="item", required=False, help=statistics_help)
    parser.add_argument("-from", action="store", dest="start_date", required=False, help=start_date_help)
    parser.add_argument("-to", action="store", dest="end_date", required=False, help=end_date_help)
    
    # nargs='?', const = 'audio', 
    args = parser.parse_args()

    return args

        
def main():

    args = argsParse()
    
    # Version
    if args.v:
        print("Version 0.4.")
        return


    timer = Timer()

    # Reminder
    if args.duration:
        d = int(args.duration[:-1])
        if args.type in ['txt', 'audio']:
            timer.alarm(d, args.type)
        else:
            print("invalid type.")
        return

    # Statistics
    if args.item:
        #print(args.item)
        today = datetime.date.today()
        start_time = today - datetime.timedelta(days=today.weekday())
        end_time = today + datetime.timedelta(days=6-today.weekday())
        if args.start_date:
            start_time = datetime.datetime.strptime(args.start_date,"%Y-%m-%d").date()
        if args.end_date:
            end_time = datetime.datetime.strptime(args.end_date,"%Y-%m-%d").date()
        #print(start_time, end_time)
        timer.statistics(args.item, start_time, end_time)
        return

    # Timer
    while 1:
        line = input()
        if line != "":
            timer.update(line)
            if line == "stop":
                timer.stop()
                break

if __name__ == '__main__':
    main()
