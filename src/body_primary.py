

def doData():
    ss = getServerRequest('replSetGetStatus')

    # On non-replication servers we get an errmsg
    if ss.get('errmsg', False):
        exit(1)

    members = ss["members"]
    primary = -1
    for _, member in enumerate(members):
        if member['stateStr'] == 'PRIMARY':
            primary = member['_id']

      
    print 'primary.value %i' % primary

def doConfig():
    ss = getServerRequest('replSetGetStatus')

    # On non-replication servers we get an errmsg
    if ss.get('errmsg', False):
        exit(1)

    set = ss['set']
    count = len(ss["members"])

    print 'graph_title MongoDB %s current primary' % set
    print 'graph_category MongoDB'
    print 'graph_vlabel Member ID'
    print 'graph_args -l %d' % count
    print 'primary.label Current primary'

