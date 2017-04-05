from checkLogin import Authenticate
from identifyCode import RClient
import config
import os, sys


def run(username, password, times = ''):
    path = os.path.dirname(os.path.abspath(__file__))+'/'+username + times  +'.jpg'
    student = Authenticate(username, password)
    student.getPic(path)

    rc = RClient(config.username, config.password, config.soft_id, config.soft_key)
    im = open(path, 'rb').read()
    try:
        result = rc.rk_create(im, config.typeid)
        code = result['Result']
        id = result['Id']
        name = student.postForms(code)
        if name == False:
            if id != None:
                rc.rk_report_error(id)
                return 0
    except Exception:
        return 0
    return name


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    time = 0
    name = run(username, password)
    # 返回姓名
    print(name)
    sys.exit(name)