# !/usr/bin/env python  
  
import telnetlib;  
import time;  
  
  
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
  
  time.ctime()
  cur = time.strftime('%l:%M:%S %p')
  date = time.strftime('%a, %d %b %Y')
  tn.write("widget_set G 2 1 2 \"    %s    \"\n" % (cur))
  tn.write("widget_set G 3 1 3 \"  %s    \"\n" % (date))
  data += tn.read_until("\n")
  time.sleep(1)
