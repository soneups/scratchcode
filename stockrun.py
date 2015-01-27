#!/usr/bin/env python
# Python script to retrieve stock information, price and change since last open.
#
# this file -- https://raw.githubusercontent.com/soneups/scratchcode/master/stockrun.py
#
# 27-Jan-2015 v1.0 initial script
# HT - http://www.instructables.com/id/Getting-Stock-Prices-on-Raspberry-Pi-Python/?ALLSTEPS

import sys
import time
import os
import ystockquote

os.system('clear')

# stock symbol from the command line
def StockLookup (symbol):
   allinfo = ystockquote.get_all(symbol)
   price = float(allinfo["price"])
   change = float(allinfo["change"])
   percent = change/(change + price)*100
   print str(time.strftime("%d/%m/%Y"))+" @ "+str(time.strftime("%H:%M"))+" "+str(symbol) + " = " + allinfo["price"]+' ('+str(change)+')'

StockLookup (symbol="");
