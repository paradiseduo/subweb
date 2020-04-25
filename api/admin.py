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
import  api.aff
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

def writeaddress(web,sub):             # 自定义规则 
    try:
        affconfig='aff = '+'\'不限制机场，规则生成失败，请检测调用格式。STC测试可用，注册地址：bilibili.stchk.cloud/auth/register?code=gzI5'
        affconfig = affconfig + '\'\n' + 'subip = \''+web
        affconfig = affconfig + '\'\n' + 'apiip = \''+web
        affconfig = affconfig + '\'\n' + 'passwd = \''+ api.aff.passwd+'\''   
        with codecs.open("./api/aff.py", "w",encoding = 'utf-8') as f:
            f.writelines(affconfig)                         
    except Exception as e:
        return(e)


def writefile(content,file):             # 自定义规则 
    try: 
        with codecs.open(file, "w",encoding = 'utf-8') as f:
            f.writelines(content)                         
    except Exception as e:
        print(e)
        return(e)
def getfile(file):             # 自定义规则 
    try: 
        with open(file, "r",encoding = 'utf-8') as f:
            return( f.read() )                        
    except Exception as e:
        print(e)
        return(e)