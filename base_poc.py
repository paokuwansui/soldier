import json
import re
from urllib import error, request


class base_poc:
    def __init__(self, url, time_out):
        self._time_out = time_out
        self._url = self.init(url)

    def init(self, url):
        # 判断此url是不是ip地址类型的,后面可能会反查域名
        if not url.startswith("http"):
            url = "http://" + url
        url = url.rstrip("\n")
        self._is_ip_flag = self.ip_judgment(url)
        self._live_flag, self._return_code = self.url_is_live(url)
        return url

    def url_is_live(self, url):
        try:
            response = request.urlopen(url, timeout=self._time_out)
            return True, str(response.getcode())
        except error.URLError as e:
            try:
                # 如果网站返回错误，则写入url，code,错误原因
                return False, str(e.getcode())
            except:
                # 如果服务器不存在则写入url,错误原因
                return False, str(e.reason)
        except Exception as e:
            return False, "time out"

    def ip_judgment(self, url):
        compile_rule = re.compile(r"(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])")
        match_list = re.findall(compile_rule, url)
        if match_list:
            return True
        return False

    def fofa_filter(self):
        # 如果网站存活状态是false就返回True退出
        if not self._live_flag:
            return True
        return False

    def start(self):
        try:
            if self.fofa_filter():
                return False
            if self.pyload():
                return True
            return False
        except Exception as e:
            self.error()

    def error(self):
        print(self._url + ':请求出错\n原因:' + srt(e), end='')

    def pyload(self):
        pass

    def succeed(self):
        print("漏洞验证成功: " + self._url + '\n' ,end='')
        return _url

    def failed(self):
        return ''
