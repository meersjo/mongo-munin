
name = "locked"

def doData():
    data = getServerStatus()
    print name + ".value " + str( 100.0 * data["globalLock"]["lockTime"]  / data["globalLock"]["globalTime"] )

def doConfig():
    print "graph_title MongoDB write lock percentage"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    print name + ".label " + name
    print name + ".type DERIVE"
    print name + ".min 0"
