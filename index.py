from checkLogin import Authenticate
from identifyCode import RClient
import config
import io, os, sys

# 打印编码设置
sys.stdout = sys.__stdout__ = io.TextIOWrapper( sys.stdout.detach(), encoding='utf-8', line_buffering=True)
sys.stderr = sys.__stderr__ = io.TextIOWrapper( sys.stderr.detach(), encoding='utf-8', line_buffering=True)


def run(username, password, times = ''):
    path = os.path.dirname(os.path.abspath(__file__))+'/images/'+username + times  +'.jpg'
    student = Authenticate(username, password)
    student.getPic(path)

    rc = RClient(config.username, config.password, config.soft_id, config.soft_key)
    im = open(path, 'rb').read()
    try:
        result = rc.rk_create(im, config.typeid)
        code = result['Result']
        id = result['Id']
        name = student.postForms(code)
        # print(name)
        if name == False:
            if id != None:
                # print(1111)
                rc.rk_report_error(id)
                return 0
    except Exception as e:
        # print(e)
        return 0
    return name


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    name = run(username, password)
    # 返回姓名
    print(name)
    sys.exit(name)