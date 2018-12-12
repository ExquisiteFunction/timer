usage: timer.py \[-h\] \[-v\] \[-r DURATION\] \[-t TYPE\] \[-stat ITEM\]
                \[-from START_DATE\] \[-to END_DATE\]

This program is used to time what you do in a daily routing. Obviously,
without hardware support, what you actually do is only what you say. But the
programm, which always runs in a single console quietly, may give you some
pressure to force on what you really do.

optional arguments:
```
  -h, --help        show this help message and exit
  -v                print the version number and exit
  -r DURATION       remind you after some time. s for second, m for minute and
                    h for hours.
  -t TYPE           the type you like to remind you when time out, txt or
                    audio, the latter depends on pygame.
  -stat ITEM        statistics the total time that you have spent on one
                    thing, dafult as current week.
  -from START_DATE  starting date for statistics, in the form of 'YYYY-MM-DD'.
  -to END_DATE      ending date for statistics, in the form of 'YYYY-MM-DD'.
```
