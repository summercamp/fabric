from fabric.api import cd
from fabric.api import env
from fabric.api import execute
from fabric.api import local
from fabric.api import run
from fabric.api import task


@task(default=True)
def update_code_and_restart():
    execute(push_changes_to_remote_repo)
    env.user = 'summercamp'
    env.password = ')FINxUyu5ZD#Yo@Xb(mj'
    execute(update_remote_host, hosts=['s6.mydevil.net'])


def push_changes_to_remote_repo():
    try:
        local("git commit -am'I have changed stuff.'")
        local('git push')
    except:
        local('echo encountered an error')


def update_remote_host():
    env.warn_only = True
    # with cd('~/fabric/'):
    run('echo git checkout master')
    run('echo pkill -9 -f run.py')
    run('echo git pull')
    run('echo ~/env/fabric/bin/python run.py')
