
Munin Plugins for MongoDB
============

[http://docs.mongodb.org/manual/reference/server-status/](http://docs.mongodb.org/manual/reference/server-status/)

Plugins
----------
* mongo_ops          : operations/second
* mongo_mem          : mapped, virtual and resident memory usage
* mongo_btree        : btree access/misses/etc...
* mongo_conn         : current connections
* mongo_lock         : write lock info
* mongo_primary      : Current primary member ID
* mongo_replication  : Seconds behind master on replSet

Requirements
-----------
* simplejson or python >= 2.6
* MongoDB 1.4+ 

Usage
-----------
You can set HOST and PORT for the REST interface in the plugin config.
If you don't, they will default to 127.0.0.1 and 28017 - that should work for
local checks on a default install.

