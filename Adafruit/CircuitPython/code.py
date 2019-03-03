#.
# Windows 7 countdown to end of support - python datetime library not available :-o
# (c) Gary@Sone.net
# 3March2019
#.

import board
import busio as io
import adafruit_ht16k33.segments
import adafruit_ds3231
from time import sleep

i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg14x4(i2c)
rtc = adafruit_ds3231.DS3231(i2c)
rtcdt = rtc.datetime
rtcmonth = rtcdt.tm_mon
rtcday = rtcdt.tm_mday

# set up the calendar
daysinjan = 14
daysinfeb = 28
daysinmar = 31
daysinapr = 30
daysinmay = 31
daysinjun = 30
daysinjul = 31
daysinaug = 31
daysinsep = 30
daysinoct = 31
daysinnov = 30
daysindec = 31

# we have all we need, start to display it.
display.fill(0)
display.show()
display.brightness = 3

display.print('WIN7')
sleep(0.75)
display.fill(0)

display.print('BY  ')
sleep(0.75)
display.fill(0)

display.print('GARY')
sleep(0.75)
display.fill(0)

display.print('SONE')
sleep(0.75)
display.fill(0)

display.print((rtcdt.tm_year))
sleep(0.75)
display.fill(0)

display.print((rtcdt.tm_mon))
sleep(0.75)
display.fill(0)

display.print((rtcdt.tm_mday))
sleep(0.75)
display.fill(0)

display.print((rtcdt.tm_hour))
sleep(0.75)
display.fill(0)

display.print((rtcdt.tm_min))
sleep(0.75)
display.fill(0)


if rtcmonth == 1:
        display.print((daysinjan-rtcday))
elif rtcmonth == 2:
        display.print((daysinfeb-rtcday))
elif rtcmonth == 3:
        display.print( (daysinmar+daysinapr+daysinmay+daysinjun+daysinjul+daysinaug+daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 4:
        display.print ((daysinapr+daysinmay+daysinjun+daysinjul+daysinaug+daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 5:
        display.print((daysinmay+daysinjun+daysinjul+daysinaug+daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 6:
        display.print((daysinjun+daysinjul+daysinaug+daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 7:
        display.print((daysinjul+daysinaug+daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 8:
        display.print((daysinaug+daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 9:
        display.print((daysinsep+daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 10:
        display.print((daysinoct+daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 11:
        display.print((daysinnov+daysindec+daysinjan)-rtcday)
elif rtcmonth == 12:
        display.print((daysindec+daysinjan)-rtcday)
else:
        display.print('RTC ')
