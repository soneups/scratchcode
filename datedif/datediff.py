#  HT https://github.com/stuartabramshumphries/datediff/blob/master/daydiff.py

#!/usr/bin/env python

from datetime import datetime
import sys


def main():
    d0 = datetime.strptime(sys.argv[1],'%Y-%m-%d')
    d1 = datetime.strptime(sys.argv[2],'%Y-%m-%d')
    diff = d1 -d0
    print(diff.days)


if __name__ == "__main__":
    main()
