from fabric.api import execute, env, local, task, cd, run

host = ['s6.mydevil.net']
password = ')FINxUyu5ZD#Yo@Xb(mj'
user = 'summercamp'

@task(default=True)
def task(arg):
    push_to_repo(arg)
    execute(update_host, hosts=host)


def push_to_repo(arg):
    local("git commit -am '{}'".format(arg))
    local("git push origin master")


def update_host():
    env.password = password
    env.user = user
    with cd('fabric'):
        run('git pull')
        run("pkill -9 -f 'run.py'")
        run('~/fabric/bin/python run.py & disown')
