# HT - https://gist.github.com/Mebus/7fda568be8dd6fd3efef
# need to replace with sys.arg so that the file can be specified on the command line...
import urllib, os

# if you comment out this line, it will download to the directory from which you run the script.
os.chdir('/tmp/test')

url = 'http://www.mydomain.com/myfile.txt'
urllib.urlretrieve(url)
