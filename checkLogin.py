import requests
from bs4 import BeautifulSoup


class Authenticate:
    """
    通过登录正方系统,验证学生
    """
    def __init__(self, number, passwd):
        self.__conn = requests.Session()
        self.__number = number
        self.__passwd = passwd
        self.__url = "http://202.116.160.166/default2.aspx"
        self.__codeUrl = "http://202.116.160.166/CheckCode.aspx"
        self.__code = ''
        self.__cookies = ''
        self.__imgName = 'code.jpg'
        self.__VIEWSTATE = ''

    def getPic(self):
        """
        提取验证码
        :return:
        """
        resp = self.__conn.get(self.__codeUrl)
        if resp.status_code != 200:
            return False
        with open(self.__imgName, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024):
                f.write(resp.content)
        return True

    def get(self):
        """
        获取__VIEWSTATE
        :return:
        """
        resp = requests.get(self.__url)
        html = BeautifulSoup(resp.content, "html.parser")
        tag = html.find("input", type="hidden")
        attr = tag.attrs['value']
        self.__VIEWSTATE = attr

    def postForms(self, code):
        """
        发送表单 登录
        :param code:
        :return:
        """
        header = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 52.0.2743.116Safari / 537.36',
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
        }
        payload = {
            '__VIEWSTATE':'dDwyODE2NTM0OTg7Oz5dbZZ3b8b2R7WRiuJkc5wPtsTwOg==',
            '__VIEWSTATEGENERATOR':'92719903',
            'txtUserName': self.__number,
            'TextBox2': self.__passwd,
            'txtSecretCode': code,
            'RadioButtonList1': '学生',
            'Button1':'',
            'lbLanguage':'',
            'hidPdrs':'',
            'hidsc':'',
        }
        resp = self.__conn.post(url=self.__url, data=payload, headers=header)
        if resp.status_code != 200:
            Exception("网页打开失败")
        html = BeautifulSoup(resp.content, "html.parser")
        tag_list = html.find_all("span", id="xhxm")
        if len(tag_list) != 0:
            print(tag_list)
            self.name = tag_list[0].text[:-2]
            return self.name
        return False

    def __getData__(self):
        pass

if __name__ == '__main__':
    text = Authenticate('111','222')
    text.getPic()
    code = input()
    print(text.postForms(code))