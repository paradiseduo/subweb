# coding=utf-8
import sys
import flask_restful
from flask import redirect, url_for
import  base64
import  re
import  requests
import urllib3
import urllib
import urllib.parse
import json
import time
import codecs
import api.subconverter
import api.aff
import api.getini
import api.admin
import os
from flask import Flask,render_template,request
urllib3.disable_warnings()

def safe_base64_decode(s): # 解密
    try:
        if len(s) % 4 != 0:
            s = s + '=' * (4 - len(s) % 4)
        base64_str = base64.urlsafe_b64decode(s)
        return bytes.decode(base64_str)
    except Exception as e:
        print('解码错误')   

def safe_base64_encode(s): # 加密
    try:
        return base64.urlsafe_b64encode(bytes(s, encoding='utf8'))
    except Exception as e:
        print('加密错误',e)

app = Flask(__name__)

ip = api.aff.apiip+'/'

@app.route('/',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['submit'] == '基础使用版':
            return redirect(ip+'basic')
        if request.form['submit'] == '节点分组版':
            return redirect(ip+'customgroup')
        if request.form['submit'] == '配置文件版':
            return redirect(ip+'ini')
        if request.form['submit'] == '节点过滤版':
            return redirect(ip+'list')
    return render_template('login.html')

@app.route('/basic', methods=['GET', 'POST'])
def basic():
    try:
        if request.method == "POST":
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                    emoji = request.form.get('emoji')
                    if emoji == None:
                        emoji = 'false'
                    fdn = request.form.get('fdn')
                    if fdn == None:
                        fdn= 'false'                    
                except :
                    return '出现BUG，请反馈'
                if tool == 'clashr':
                        CustomGroupvmess = '{ip}/sub?target=clashr&url={sub}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=clashr&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('clashr.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)    
                if tool == 'loon':
                        CustomGroupvmess = '{ip}/sub?target=loon&url={sub}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=loon&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('loon.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)                                           
                if tool == 'surge':
                        CustomGroupvmess = '{ip}/sub?target=surge&url={sub}&ver=4&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('surge.html',sub = s,custom="默认为surge4，参数为为ver=4。",api=CustomGroupvmess,api2=api2)
                if tool == 'qx':
                        CustomGroupvmess = '{ip}/sub?target=quanx&url={sub}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=quanx&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn)
                        return render_template('quanx.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)  
                if tool == 'mellow':
                        CustomGroupvmess = '{ip}/sub?target=mellow&url={sub}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=mellow&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('mellow.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)
                if tool == 'surfboard':
                        CustomGroupvmess = '{ip}/sub?target=surfboard&url={sub}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=surfboard&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('surfboard.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)                                
                else:
                    return render_template('basic.html')    
            else:
                return '订阅不规范'
        return render_template('basic.html')
    except Exception as e:
        return e

@app.route('/customgroup', methods=['GET', 'POST'])
def customgroup():
    try:
        if request.method == "POST":
            if request.form['submit'] == '点击添加节点分组':            
                ori1 = request.form['custom1']
                ori2 = request.form['custom2']
                ori3 = request.form['custom3']
                add1 = '@'+ request.form['firstname']
                add2 = '@'+request.form['lastname']
                add3='@'+  request.values.get('method')
                if add1 == '@':
                    return '未填写名称'                
                if add2 == '@':
                    return '未填写节点'
                return render_template('index.html',custom1=ori1+add1,custom2=ori2+add2,custom3=ori3+add3)    
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                n=request.form['custom1']           
                c=request.form['custom2']
                method = request.form['custom3']
                len1 = len(str(n).split('@'))
                len2 = len(str(c).split('@'))
                len3 = len(str(method).split('@'))
                if len1 != len2 or len1 != len3 or len2 != len3:
                    return('检查分组是否一一对应')
                groups = str(safe_base64_encode(api.subconverter.getgroups(n,c,method))).split('\'')[1]
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                    emoji = request.form.get('emoji')
                    if emoji == None:
                        emoji = 'false'
                    fdn = request.form.get('fdn')
                    if fdn == None:
                        fdn= 'false'
                except :
                    return '出现BUG，请反馈'             
                if tool == 'clashr':
                        CustomGroupvmess = '{ip}/sub?target=clashr&url={sub}&groups={groups}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=clashr&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('clashr.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)                       
                if tool == 'surge':
                        CustomGroupvmess = '{ip}/sub?target=surge&url={sub}&groups={groups}&ver=4&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('surge.html',sub = s,custom=n+c+method+'\n备用暂时不支持\n'+'默认为surge4，参数为为ver=4。',api=CustomGroupvmess,api2=api2)
                if tool == 'quanx':
                        CustomGroupvmess = '{ip}/sub?target=quanx&url={sub}&groups={groups}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=quanx&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('quanx.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)  
                if tool == 'loon':
                        CustomGroupvmess = '{ip}/sub?target=loon&url={sub}&groups={groups}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=loon&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('loon.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)  
                if tool == 'mellow':
                        CustomGroupvmess = '{ip}/sub?target=mellow&url={sub}&groups={groups}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=mellow&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('mellow.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)
                if tool == 'surfboard':
                        CustomGroupvmess = '{ip}/sub?target=surfboard&url={sub}&groups={groups}&emoji={emoji}&fdn={fdn}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=surfboard&url={sub}&emoji={emoji}&fdn={fdn}'.format(sub=str(sub),emoji=emoji,fdn=fdn) 
                        return render_template('surfboard.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)                                          
                else:
                    return render_template('index.html')    
            else:
                return '订阅不规范'
        return render_template('index.html')
    except Exception as e:
        return e

@app.route('/ini', methods=['GET', 'POST'])
def inigroup():
    try:
        if request.method == "POST":
            iniflag = 'url'                                 #配置文件是本地配置或者远程配置标志位
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                ini=request.form['ini']                            
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                    custom = request.form['custom1']
                    encodecustom=urllib.parse.quote(custom)
                    excustom = request.form['custom2']
                    encodeexcustom=urllib.parse.quote(excustom)
                    emoji = request.form.get('emoji')
                    if emoji == None:
                        emoji = 'false'
                    fdn = request.form.get('fdn')
                    if fdn == None:
                        fdn= 'false'
                except :
                    return '出现BUG，请反馈'
                try:
                    if ';设置规则标志位' in ini and ';设置分组标志位' in ini :
                        ini1 = api.subconverter.getini(ini).split('&')
                        if 'erro' in ini1 :
                            return '检查远程配置文件是否正确'
                        iniflag = 'file'                                #检测到本地配置，标志位设为file
                        rulesets = str(safe_base64_encode(ini1[0])).split('\'')[1]
                        groups = str(safe_base64_encode(ini1[1])).split('\'')[1]  
                    else:
                        ini = urllib.parse.quote(ini)
                except :
                    return '检查远程配置文件是否正确'    
                if tool == 'surge':
                    if iniflag == 'file':
                        CustomGroupvmess = '{ip}/sub?target=surge&url={sub}&ruleset={rulesets}&groups={groups}&ver=4&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom)
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&ruleset={rulesets}&groups={groups}&ver=4&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(sub=str(sub),groups=groups,rulesets=rulesets,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom) 
                        return render_template('surge.html',sub = s,custom=ini+'\n默认为surge4，参数为为ver=4。',api=CustomGroupvmess,api2=api2)
                    if iniflag == 'url':
                        CustomGroupvmess = '{ip}/sub?target={tar}&url={sub}&config={config}&ver=4&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(tar=tool,ip=api.aff.subip,sub=str(sub),config=ini,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom)
                        api2 = 'https://gfwsb.114514.best/sub?target={tar}&url={sub}&config={config}&ver=4&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(tar=tool,sub=str(sub),config=ini,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom) 
                        return render_template('surge.html',sub = s,custom=ini+'\n'+'默认为surge4，参数为为ver=4。',api=CustomGroupvmess,api2=api2)                        
                if iniflag == 'file':
                    CustomGroupvmess = '{ip}/sub?target={tar}&url={sub}&ruleset={rulesets}&groups={groups}&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(tar=tool,ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom)
                    api2 = 'https://gfwsb.114514.best/sub?target={tar}&url={sub}&ruleset={rulesets}&groups={groups}&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(tar=tool,sub=str(sub),groups=groups,rulesets=rulesets,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom) 
                if iniflag == 'url':
                    CustomGroupvmess = '{ip}/sub?target={tar}&url={sub}&config={config}&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(tar=tool,ip=api.aff.subip,sub=str(sub),config=ini,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom)
                    api2 = 'https://gfwsb.114514.best/sub?target={tar}&url={sub}&config={config}&emoji={emoji}&fdn={fdn}&include={custom}&exclude={custom2}'.format(tar=tool,sub=str(sub),config=ini,emoji=emoji,fdn=fdn,custom2=encodeexcustom,custom=encodecustom) 
                return render_template('{tool}.html'.format(tool=tool),sub = s,custom=ini,api=CustomGroupvmess,api2=api2)
            else:
                return '订阅不规范'
        return render_template('ini.html')
        
    except Exception as e:
        return e

@app.route('/list', methods=['GET', 'POST'])
def lists():
    try:
        if request.method == "POST":
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                    custom = request.form['custom1']
                    encodecustom=urllib.parse.quote(custom)
                    excustom = request.form['custom2']
                    encodeexcustom=urllib.parse.quote(excustom)
                    emoji = request.form.get('emoji')
                    if emoji == None:
                        emoji = 'false'
                    fdn = request.form.get('fdn')
                    if fdn == None:
                        fdn= 'false'                    
                except :
                    return '出现BUG，请反馈'
                yourcustom = '包含的节点:'+custom+'           去掉的节点:'+excustom  
                if tool == 'clashnode':
                        CustomGroupvmess = '{ip}/sub?target=clashr&list=true&url={sub}&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=clashr&list=true&url={sub}&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn) 
                        return render_template('clashr.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)                                            
                if tool == 'qxnode':
                        CustomGroupvmess = '{ip}/sub?target=quanx&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=quanx&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('qxnode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)                       
                if tool == 'surnode':
                        CustomGroupvmess = '{ip}/sub?target=surge&url={sub}&ver=4&list=true&udp=true&tfo=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&ver=4&list=true&udp=true&tfo=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('surgenode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)                                 
                if tool == 'ssrnode':
                        CustomGroupvmess = '{ip}/sub?target=ssr&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=ssr&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('othernode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)  
                if tool == 'quannode':
                        CustomGroupvmess = '{ip}/sub?target=quan&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=quan&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('othernode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)   
                if tool == 'ssdnode':
                        CustomGroupvmess = '{ip}/sub?target=ssd&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=ssd&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('othernode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)  
                if tool == 'ssnode':
                        CustomGroupvmess = '{ip}/sub?target=ss&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=ss&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('othernode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)  
                if tool == 'sssubnode':
                        CustomGroupvmess = '{ip}/sub?target=sssub&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=sssub&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('othernode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)  
                if tool == 'v2raynode':
                        CustomGroupvmess = '{ip}/sub?target=v2ray&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,ip=api.aff.subip,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        api2 = 'https://gfwsb.114514.best/sub?target=v2ray&url={sub}&list=true&include={custom}&exclude={custom2}&emoji={emoji}&fdn={fdn}'.format(custom2=encodeexcustom,sub=str(sub),custom=encodecustom,emoji=emoji,fdn=fdn)
                        return render_template('othernode.html',sub = s,custom=yourcustom,api=CustomGroupvmess,api2=api2)                  
                else:
                    return render_template('basic.html')    
            else:
                return '订阅不规范'
        return render_template('list.html')
    except Exception as e:
        return e

@app.route('/ruleset', methods=['GET', 'POST'])
def ruleset():
    try:
        
        if request.method == "POST":
            if request.form['submit'] == '点击添加分流':            
                ori1 = request.form['rulecustom']+'\n'
                ori = request.form['custom1']
                add1 = 'surge_ruleset='+ request.form['rulename'] +','+request.form['rulelist']
                return render_template('ruleset.html',rulecustom=ori1+add1,custom1=ori)    
   
            if request.form['submit'] == '点击添加分组':            
                ori1 = request.form['custom1']+'\n'
                ori = request.form['rulecustom']
                add1 = 'custom_proxy_group='+ request.form['firstname']
                add2 = '`'+request.form['lastname']
                add3='`'+ request.values.get('method')
                if add1 == '`':
                    return '未填写名称'                
                if add2 == '`':
                    return '未填写地址'
                if 'fallback' in add3 or 'url-test' in add3: 
                    add4 = '`http://www.gstatic.com/generate_204`300'
                else:
                    add4 = ''
                return render_template('ruleset.html',rulecustom=ori,custom1=ori1+add1+add3+add2+add4)                                                                             
        return render_template('ruleset.html')
    except Exception as e:
        return e

@app.route('/help', methods=['GET', 'POST'])
def help():
    try:
        content= api.admin.getfile('../help.txt')
        return render_template('content.html',content='帮助文档：\n\n\n'+content)
    except Exception as e:
        return '无帮助文档，请使用管理系统上传帮助文档到../help.txt'

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        if request.method == "POST":
            s = request.form['passwd']
            if api.aff.passwd == s:
                if request.form['submit'] == '上传配置':               
                    content = request.form.get('content')
                    fileadd = request.form.get('file')              
                    api.admin.writefile(content,fileadd)
                    content= api.admin.getfile(fileadd)
                    return render_template('content.html',content=content)  
                if request.form['submit'] == '查看配置': 
                    fileadd = request.form.get('file')              
                    content= api.admin.getfile(fileadd)
                    return render_template('content.html',content=content)         
                if  request.form['submit'] == '重启后端' :
                    os.system('pkill subconverter')
                    return '重启后端成功！！！'
                if  request.form['submit'] == '重启前端' :
                    os.system('pkill -9 -f api.py')
                    return '重启前端成功！！！'
            else:
                return '密码错误'
        return render_template('admin.html')
    except Exception as e:
        return e



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=10086)            #自定义端口