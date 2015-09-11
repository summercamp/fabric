from fabric.api import cd
from fabric.api import env
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
def update_code_and_restart():
    execute(push_changes_to_remote_repo)
    env.user = 'summercamp'
    env.password = ')FINxUyu5ZD#Yo@Xb(mj'
    execute(update_remote_host, hosts=['s6.mydevil.net'])


def push_changes_to_remote_repo():
    print 'pushing changes to repo'
    local("git commit -am'I have changed stuff.'")
    local('git push')


def update_remote_host():
    print 'updating remote host'
    env.warn_only = True
    with cd('fabric'):
        run('pkill -9 -f run.py')
        run('git pull')
        run('~/env/fabric/bin/python run.py')
