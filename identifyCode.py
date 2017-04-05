import requests
import config
from hashlib import md5


class RClient(object):
    """
    验证码识别
    """
    def __init__(self, username, password, soft_id, soft_key):
        self.username = username
        self.password = password
        self.soft_id = soft_id
        self.soft_key = soft_key
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Except': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, image, image_type, timeout=60):
        params = {
            'typeid': image_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {
            'image': image
        }
        response = requests.post("http://api.ruokuai.com/create.json",
                                 data=params,
                                 files=files,
                                 headers=self.headers
                                 )
        return response.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


# if __name__ == '__main__':
#     rc = RClient(config.username, config.password, config.soft_id, config.soft_key)
#     im = open(config.image, 'rb').read()
#     print(rc.rk_create(im, config.typeid))