#!/usr/bin/python
import cgi
import sys, telnetlib

def mcuwrite(ch):
    tn = telnetlib.Telnet('localhost', 6571)
    tn.write(ch)
    tn.close()

print 'Content-Type: text/plain'
print

form = cgi.FieldStorage()
syuttaikin = form.getfirst('syuttaikin', '0')
if syuttaikin == '0':
    mcuwrite('0')
elif syuttaikin == '1':
    mcuwrite('1')
else:
    print 'unknown value: ' + syuttaikin
