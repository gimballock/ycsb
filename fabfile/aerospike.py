from fabric.api import *

@roles('server')
@parallel
def aerospike_start():
    """Starts aerospike on servers"""
    with settings(warn_only=True):
        run('/etc/init.d/aerospike start')

@roles('server')
@parallel
def aerospike_stop():
    """Stops aerospike on servers"""
    with settings(warn_only=True):
        run('/etc/init.d/aerospike stop')

