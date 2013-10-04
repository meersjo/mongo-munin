
names = [ "locked_read", "locked_write", "acquiring_read", "acquiring_write" ]

def doData():
    data = getServerStatus()['locks']
    totals = { 'locked': { 'read': 0, 'write': 0 }, 'acquiring': { 'read': 0, 'write': 0 } }

    for key in data:
      totals['locked']['read'] += data[key]['timeLockedMicros'].get('r', 0)
      totals['locked']['write'] += data[key]['timeLockedMicros'].get('w', 0)
      totals['acquiring']['read'] += data[key]['timeAcquiringMicros'].get('r', 0)
      totals['acquiring']['write'] += data[key]['timeAcquiringMicros'].get('w', 0)

    print names[0] + ".value " + str( totals['locked']['read'] )
    print names[1] + ".value " + str( totals['locked']['write'] )
    print names[2] + ".value " + str( totals['acquiring']['read'] )
    print names[3] + ".value " + str( totals['acquiring']['write'] )

def doConfig():
    print "graph_title MongoDB write lock percentage"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    for name in names:
      print name + ".label " + name
      print name + ".type DERIVE"
      print name + ".cdef " + name + ",10000.0,/"
