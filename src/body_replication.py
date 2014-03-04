

def doData():
    ss = getServerRequest('replSetGetStatus')

    # On non-replication servers we get an errmsg
    if ss.get('errmsg', False):
        exit(1)

    members = ss["members"]
    for _, member in enumerate(members):
        if member.get('self', False):
            me = member
        if member['stateStr'] == 'PRIMARY':
            primary = member

    secs_behind = primary['optime']['$timestamp']['t'] - me['optime']['$timestamp']['t']
      
    print('secs_behind.value %i' % secs_behind)

def doConfig():
    ss = getServerRequest('replSetGetStatus')

    # On non-replication servers we get an errmsg
    if ss.get('errmsg', False):
        exit(1)

    set = ss['set']

    print "graph_title MongoDB %s lag" % set
    print "graph_category MongoDB"
    print "graph_vlabel seconds"
    print "graph_args -l 0"
    print "secs_behind.label Seconds Behind"

