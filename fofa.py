import requests
import base64
import sys
from load_config import config


class FofaSelect:
    def __init__(self):
        """
        初始化fofa的email和api_key参数
        """
        print()
        # fofa_email =
        # api_key =
        self._email = config.get_config()["fofa"]["email"]
        self._api_key = config.get_config()["fofa"]["api_key"]
        self._api = (
            r"https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&size={}"
        )
        self._select_size = 0
        self._results = None

    def get_select_len(self):
        """
        查询当前查询的条数有多少
        """
        return self._select_size

    def get_select_data(self):
        """
        查询当前查询的结果
        """
        return self._results

    def select(self, key, size=10000):
        """
        函数作用:
        调用fofa的api查询

        参数:
        key是关键字, 示例:app="致远互联-OA"
        size是查询条数,10000条是上限
        """
        # ,size是查询调试,10000条是上限
        flag = base64.b64encode(key.encode()).decode()
        print(self._api.format(self._email, self._api_key, flag, size))
        response = requests.get(
            self._api.format(self._email, self._api_key, flag, size)
        )
        self._results = response.json()["results"]
        self._select_size = len(self._results)

    def save_file(self, path, name, model="w"):
        """
        函数作用:
        将查询结果保存到文件中

        参数:
        path是保存文件路径
        name是保存文件的文件名
        model是保存文件模式, 有w写模式,a追加模式,a+在文件尾追加模式
        """
        file_name = path + name
        f = open(file_name, model)
        for addr in self._results:
            f.write(addr[0] + "\n")
        f.close()


fofa = FofaSelect()
