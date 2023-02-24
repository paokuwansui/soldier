from json import loads
class load_config:
    def __init__(self):
        """
        读取config配置文件
        """
        with open('/home/lzh/Project/autoCodeTest/code/config.json', 'r', encoding='utf-8') as config:
            self._config = loads(config.read())

    def get_config(self):
        """
        得到配置文件的字典格式数据
        """
        return self._config

    def updata_config(self):
        """
        更新配置文件内容
        """
        with open('./config.json', 'r', encoding='utf-8') as config:
            self._config = loads(config.read())

config = load_config()
