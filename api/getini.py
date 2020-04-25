# coding=utf-8
import  sys
import  base64
import  re
import  requests
import  urllib3
import  urllib
import  json
import  time
import codecs
#import  api.aff
urllib3.disable_warnings()
def Retry_request(url): #远程下载
    i = 0
    for i in range(2):
        try:
            res = requests.get(url) # verify =false 防止请求时因为代理导致证书不安全
            return res.text
        except Exception as e:
            i = i+1
            print('重新下载：'+url)

def writeini(url):             # 自定义规则
    
    try:
        inicustom = Retry_request(url)   
        inicustom = inicustom.split('[emojis]')[1].split('[server]')[0]
        inicustom = '[common]\n\
api_mode=false\n\
default_url=\n\
clash_rule_base=simple_base.yml\n\
surge_rule_base=surge.conf\n\
surfboard_rule_base=surfboard.conf\n\
mellow_rule_base=mellow.conf\n\
proxy_ruleset=SYSTEM\n\
proxy_subscription=NONE\n\
append_proxy_type=false\n\
rename_node=\(?((x|X)?(\d+)(\.?\d+)?)((\s?倍率?)|(x|X))\)?@$1x\n\
[managed_config]\n\
write_managed_config=true\n\
managed_config_prefix=http://127.0.0.1:25500\n[emojis]\n'+inicustom+'[server]\n\
listen=0.0.0.0\n\
port=10010\n\
[advanced]\n\
print_debug_info=false\n\
max_pending_connections=10240\n\
max_concurrent_threads=1\n'         
        with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
            f.writelines(inicustom)                         
    except Exception as e:
        print(e)
        return(e)

#print(Retry_request('http://127.0.0.1:10010/clash?url=https%3A//stc-dns.com/link/jSkLx7LgGRRfgSFw%3Fmu%3D2'))
#custom_proxy_group=UrlTest`url-test`.*`http://www.gstatic.com/generate_204`300
#custom_proxy_group=FallBack`fallback`.*`http://www.gstatic.com/generate_204`300
#custom_proxy_group=LoadBalance`load-balance`.*`http://www.gstatic.com/generate_204`300

