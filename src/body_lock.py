
name = "locked"

def doData():
    data = getServerStatus()
    print name + ".value " + str( data["globalLock"]["lockTime"] )

def doConfig():
    print "graph_title MongoDB write lock percentage"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    print name + ".label " + name
    print name + ".type DERIVE"
