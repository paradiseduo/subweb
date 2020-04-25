#! /bin/sh 
echo "-----------------------------------Start-------------------------------------"
echo "------------------------------------While循环----------------------------------------"
while true
do
    proc_name="subconverter"        #subconverter进程名
    proc_num()                      #查询进程数量
    {
        num=`ps -ef | grep $proc_name | grep -v grep | wc -l`
        return $num
    }
    proc_num  
    number=$?                       #获取进程数量
    if [ $number -eq 0 ]            #如果进程数量为0
    then                            #重新启动服务器，或者扩展其它内容。
        cd /subweb/config
        ./subconverter &
    fi
    proc_name="api.py"              #api.py进程名
    proc_num()                      #查询进程数量
    {
        num=`ps -ef | grep $proc_name | grep -v grep | wc -l`
        return $num
    }
    proc_num  
    number=$?                       #获取进程数量
    if [ $number -eq 0 ]            #如果进程数量为0
    then                            #重新启动服务器，或者扩展其它内容。
        python3 /subweb/api.py &   #运行web服务
    fi

    sleep 60s
echo "------------------------------------Sucess----------------------------------------"
done
echo "------------------------------------WEB----------------------------------------"