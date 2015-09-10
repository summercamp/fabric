from fabric.api import cd
from fabric.api import execute
from fabric.api import local
from fabric.api import run
from fabric.api import task


GIT_SETTINGS = {
    'user': 'summercamp',
    'password': 'WebInterpret13+',
}

HOSTS = {
    'git': ['github.com/summercamp/fabric'],
    'devil': ['s6.mydevil.net'],
}

REMOTE_CREDS = {
    'user': 'summercamp',
    'pass': ')FINxUyu5ZD#Yo@Xb(mj',
}


@task(default=True)
def summercamp_update_code_and_restart():
    execute(_push_changes_to_remote_repo)
    execute(_update_remote_host, hosts=HOSTS.get('devil'))


def _push_changes_to_remote_repo():
    local("git commit -am'I have changed stuff.'")
    local('echo git push origin/master')

def _update_remote_host():
    print 'update'
    with cd('fabric'):
        run('pkill -9 -f run.py')
        run('git pull')
        run('~/env/fabric/bin/python run.py')
