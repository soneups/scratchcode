# !/usr/bin/env python

import telnetlib
import time;
import os;
import subprocess;
from decimal import Decimal, ROUND_DOWN


host='127.0.0.1'; 
port='13666';
data = ""



tn = telnetlib.Telnet(host, port)
tn.write("hello\r");

data += tn.read_until("\n");
tn.write("screen_add G\n");
data += tn.read_until("\n");

tn.write("widget_add G 1 title\n");
data += tn.read_until("\n");

tn.write("widget_set G 1 \"Raspberry Pi\"\n");
data += tn.read_until("\n");

tn.write("widget_add G 2 string\n");
data += tn.read_until("\n");

tn.write("widget_add G 3 string\n");
data += tn.read_until("\n");


var = 1;
while var == 1 :

  cmd1 = "cat /sys/class/thermal/thermal_zone0/temp"
  process = subprocess.Popen(cmd1, stdout=subprocess.PIPE , shell=True)
  os.waitpid(process.pid, 0)[1]
  cpu = process.stdout.read().strip()
  
  cmd2 = "cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"
  process2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE , shell=True)
  os.waitpid(process2.pid, 0)[1]
  spd = process2.stdout.read().strip()


  tn.write("widget_set G 2 1 2 \"Temperature: %.2sc\" \n" % (cpu));
  tn.write("widget_set G 3 1 3 \"CPU Speed: %sMHz\" \n" % (spd[:-3]));
  data += tn.read_until("\n");

  time.sleep(2);
