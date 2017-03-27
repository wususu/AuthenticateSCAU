from checkLogin import Authenticate
from identifyCode import RClient
import config
import os, sys


def run(username, password):
    student = Authenticate(username, password)
    student.getPic()
    rc = RClient(config.username, config.password, config.soft_id, config.soft_key)
    im = open(os.path.dirname(os.path.abspath(__file__))+'/'+username+'.jpg', 'rb').read()
    try:
        code = rc.rk_create(im, config.typeid)['Result']
        name = student.postForms(code)
        if name is False:
            return 0
    except Exception:
        return 0
    return name


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    name = run(username, password)
    sys.exit(name)