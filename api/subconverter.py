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
    return 'erro'

def writeini(name,custom,method,ini):             # 自定义规则,历史脚本，不起作用
    try:
        if ini == '' or ini == None:
            if custom == '' or custom == None:   #不分组的情况
                with open("./config/prefserver.ini", "r",encoding = 'utf-8') as f:
                    rule = f.read() 
                with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                    f.writelines(rule)            
            else:
                with open("./config/prefserver.ini", "r",encoding = 'utf-8') as f:
                    rule = f.read()
                names = str(name).split('@')                
                groups = str(custom).split('@')
                methods = str(method).split('@')
                if len(groups) == len(names):  #分组填写正常的的情况
                        inicustom = str(rule).split(';NicoNewBeee')
                        inigroup = ''
                        groupname = '`'
                        for i in range(1,len(groups)):
                            if methods[i] == 'sl':
                                inigroup += 'custom_proxy_group='+str(names[i])+'手动选择`select`'+str(groups[i])+'\n'
                                groupname += '[]'+str(names[i])+'手动选择`'
                            if methods[i] == 'ut':
                                inigroup += 'custom_proxy_group='+str(names[i])+'延迟最低`url-test`'+str(groups[i])+'`http://www.gstatic.com/generate_204`500\n'
                                groupname += '[]'+str(names[i])+'延迟最低`'
                            if methods[i] == 'fb':
                                inigroup += 'custom_proxy_group='+str(names[i])+'故障切换`fallback`'+str(groups[i])+'`http://www.gstatic.com/generate_204`500\n'
                                groupname += '[]'+str(names[i])+'故障切换`'
                            if methods[i] == 'lb':
                                inigroup += 'custom_proxy_group='+str(names[i])+'负载均衡`load-balance`'+str(groups[i])+'`http://www.gstatic.com/generate_204`500\n'
                                groupname += '[]'+str(names[i])+'负载均衡`'

                        proxygroup =   'custom_proxy_group=🔰 节点选择`select'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=📲 电报吹水`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=📹 YouTube`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=🎥 NETFLIX`select`[]🔰 节点选择`'+groupname+'`(NF|解锁)`[]DIRECT\n\
                                        custom_proxy_group=📺 巴哈姆特`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=🌍 国外媒体`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=🌏 国内媒体`select`[]DIRECT`[]🔰 节点选择\n\
                                        custom_proxy_group=🍎 苹果服务`select`[]DIRECT`[]🔰 节点选择`\n\
                                        custom_proxy_group=🛑 全球拦截`select`[]REJECT`[]DIRECT\n\
                                        custom_proxy_group=🐟 漏网之鱼`select`[]🔰 节点选择`[]DIRECT`'+groupname+'\n'

                        inicustom[1] = proxygroup+inigroup                
                        with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                            f.writelines(str(inicustom[0])+str(inicustom[1])+str(inicustom[2])) 
                else:                           #分组填写不正常的的情况
                    with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                        f.writelines(rule)  
        else:
            with open("./config/inibase.ini", "r",encoding = 'utf-8') as f:
                    rule = f.read()
            ini = Retry_request(ini)
            if '[common]' in ini or '[server]' in ini or '[advanced]' in ini or '[managed_config]' in ini or '[ruleset]' in ini:
                return 'ini'
            ini = ini.split(';NicoNewBeee')[1]
            rule =  rule + '\n;ini客制化\n'+ini
            with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                    f.writelines(rule)                             
    except Exception as e:
        print(e)


def getgroups(name,custom,method):             # 节点分组相关函数 
    try:
            if custom == '' or custom == None:   #不分组的情况
                return ''          
            else:
                names = str(name).split('@')                
                groups = str(custom).split('@')
                methods = str(method).split('@')
                if len(groups) == len(names):  #分组填写正常的的情况
                        inigroup = ''
                        groupname = '`'
                        for i in range(1,len(groups)):
                            if methods[i] == 'sl':
                                inigroup += '@'+str(names[i])+'`select`'+str(groups[i])+''
                                groupname += '[]'+str(names[i])+'`'
                            if methods[i] == 'ut':
                                inigroup += '@'+str(names[i])+'`url-test`'+str(groups[i])+'`http://www.gstatic.com/generate_204`500'
                                groupname += '[]'+str(names[i])+'`'
                            if methods[i] == 'fb':
                                inigroup += '@'+str(names[i])+'`fallback`'+str(groups[i])+'`http://www.gstatic.com/generate_204`500'
                                groupname += '[]'+str(names[i])+'`'
                            if methods[i] == 'lb':
                                inigroup += '@'+str(names[i])+'`load-balance`'+str(groups[i])+'`http://www.gstatic.com/generate_204`500'
                                groupname += '[]'+str(names[i])+'`'
                        proxygroup = api.aff.proxygroup.format(groupname=groupname)
                        inicustom = proxygroup+inigroup                
                        return inicustom                         
    except Exception as e:
        return 'erro'


def getini(iniin):             # 自定义规则   
    try:
        rulesets = iniin.split(';设置规则标志位')[1].replace('surge_ruleset=','@').replace('\n','').replace('\r','')              
        groups =  iniin.split(';设置分组标志位')[1].replace('custom_proxy_group=','@').replace('\n','').replace('\r','') 
        inicustom = rulesets+'&'+groups               
        return inicustom    
        """
        else:
            
            ini = Retry_request(iniin)
            rulesets = ini.split(';设置规则标志位')[1].replace('surge_ruleset=','@').replace('\n','')              
            groups =  ini.split(';设置分组标志位')[1].replace('custom_proxy_group=','@').replace('\n','') 
            inicustom = rulesets+'&'+groups 
                         
            return inicustom 
        """                                     
    except Exception as e:
        return 'erro'


#getini('https://raw.githubusercontent.com/lzdnico/SSRClash/master/config/default.ini')