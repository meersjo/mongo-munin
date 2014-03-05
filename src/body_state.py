

def doData():
    ss = getServerRequest('replSetGetStatus')

    # On non-replication servers we get an errmsg
    if ss.get('errmsg', False):
        exit(1)

    members = ss["members"]
    for _, member in enumerate(members):
      name = member['name'].split(':')[0]
      state = member['state']
      print '%s.value %d' % (name, state)


def doConfig():
    ss = getServerRequest('replSetGetStatus')

    # On non-replication servers we get an errmsg
    if ss.get('errmsg', False):
        exit(1)

    set = ss['set']

    print 'graph_title MongoDB %s member state' % set
    print 'graph_category MongoDB'
    print 'graph_vlabel state'

    for _, member in enumerate(ss['members']):
      name = member['name'].split(':')[0]
      print '%s.label %s' % (name, name)

