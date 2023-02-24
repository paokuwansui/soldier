from concurrent.futures import ThreadPoolExecutor
import threading
import queue
import os


class Hreading:
    def __init__(
        self, POC, succeed_file_name="succeed.txt", failed_file_name="failed.txt"
    ):
        self._POC = POC
        self._poc_return_queue = queue.Queue()
        self._hreading_down_flag = False
        self._dir = os.path.dirname(os.path.abspath(__file__))
        self._succeed_file = open(self._dir + "/POC_RESULTS/" + succeed_file_name, "w")
        self._failed_file = open(self._dir + "/POC_RESULTS/" + failed_file_name, "w")

    def write_file(self, message):
        if message[0] == "failed_write":
            self._failed_file.write(message[1] + '\n')
        elif message[0] == "succeed_write":
            self._succeed_file.write(message[1] + '\n')

    def write_file_start(self):
        while True:
            if self._poc_return_queue.qsize() != 0:
                self.write_file(self._poc_return_queue.get())
            else:
                if self._hreading_down_flag:
                    break  
        self._succeed_file.close()
        self._failed_file.close()

    def start(self, url, time_out):
        poc = self._POC(url, time_out)
        if poc.start():
            self._poc_return_queue.put(("succeed_write", poc.succeed()))
        else:
            self._poc_return_queue.put(("failed_write", poc.failed()))

    def threading_start(self, url_list, threading_num=16, time_out=5):
        self.ready()
        pool = ThreadPoolExecutor(max_workers=threading_num)
        threading_pool_list = []
        for i in url_list:
            threading_pool_list.append(pool.submit(self.start, i, time_out))
        for i in threading_pool_list:
            i.done()
        pool.shutdown()
        self.end()

    def ready(self):
        self._write_file_hreading = threading.Thread(target=self.write_file_start)
        self._write_file_hreading.start()

    def end(self):
        self._hreading_down_flag = True
        self._write_file_hreading.join()

    def test_start(self, url_list, time_out=5):
        self.ready()
        for url in url_list:
            self.start(url, time_out)
        self.end()
