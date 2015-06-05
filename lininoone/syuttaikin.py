#!/usr/bin/python
import telnetlib, urllib2

SERVERURL = 'http://10.25.244.23/cgi-bin/syuttaikin.cgi'

def mcuwrite(ch):
    tn = telnetlib.Telnet('localhost', 6571)
    tn.write(ch)
    tn.close()

def geturl(url):
    resbody = None
    try:
        r = None
        r = urllib2.urlopen(url, timeout=60)
        resbody = r.read()
    except Exception, err:
        print 'HTTP error: ', err
    finally:
        if r: r.close()
    return resbody

def main():
    stat = geturl(SERVERURL).rstrip()
    if stat == 'online':
        mcuwrite('1')
    elif stat == 'offline':
        mcuwrite('0')
    else:
        print 'unknown status: ' + stat

if __name__ == "__main__":
    main()
