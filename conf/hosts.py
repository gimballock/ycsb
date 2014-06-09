from fabric.api import env
import pytz

#user name to ssh to hosts
env.user = 'root'
#user password (the better is to use pubkey authentication)
env.password = 'thumbtack'

env.show = ['debug']

env.roledefs = {
    #list of client hosts
    'client': ['']

    #list of server hosts
    'server': ['']

    #list of all available client hosts
    'all_client': ['']
}

#hosts timezone (required to correctly schedule ycsb tasks)
timezone = pytz.timezone('US/Pacific')
