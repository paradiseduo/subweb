#! /bin/sh  
proc_name="subconverter"        #进程名
proc_num()                      #查询进程数量
{
    num=`ps -ef | grep $proc_name | grep -v grep | wc -l`
    return $num
}
proc_num  
number=$?                       #获取进程数量
if [ $number -eq 0 ]            #如果进程数量为0
then                            #重新启动服务器，或者扩展其它内容。
    cd /root/subweb/config; ./subconverter
fi