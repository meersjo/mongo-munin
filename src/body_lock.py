
collection_name = "set your collection name"

def get():
    return getServerStatus()["locks"][collection_name]["timeLockedMicros"]

def doData():
    for k,v in get().iteritems():
        print( str(k) + ".value " + str(int(v)) )

def doConfig():
    print "graph_title MongoDB collection_name write lock time"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    for k in get():
        print k + ".label " + k
        print k + ".min 0"
        print k + ".type COUNTER"
        print k + ".draw LINE1"
