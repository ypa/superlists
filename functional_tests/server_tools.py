# Because the tests are in Python3, we can't directly call our Fabric functions,
# which are Python 2. Hence this extra hop and call the `fab` command as a new process


from os import path
import subprocess
THIS_FOLDER = path.abspath(path.dirname(__file__))

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )
