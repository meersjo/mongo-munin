
#%# family=auto
#%# capabilities=autoconf

import urllib2
import sys
import os

try:
    import json
except ImportError:
    import simplejson as json

host = os.environ.get('HOST', '127.0.0.1')
port = os.environ.get('PORT', 28017)

def getServerRequest(action):
    url = "http://%s:%s/%s" % (host, port, action)
    req = urllib2.Request(url)
    raw = urllib2.urlopen(req).read()
    return json.loads( raw )

def getServerStatus():
    return getServerRequest('_status')['serverStatus']

def doAutoConf():
    try:
        raw = urllib2.urlopen( "http://%s:%d/_status" % (host, port) ).read()
        print "yes"
        return True
    except urllib2.URLError as detail:
        print "no (", detail, ")"
        return False
