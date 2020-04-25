#! /bin/sh 
echo "-----------------------------------Start-------------------------------------"
cd /root/subweb                                                 #默认subweb目录               将本update.sh放置到root/nico或者其他文件夹下
git reset --hard HEAD
sleep 1s
git pull
echo "----------------------------------Update-------------------------------------"
sleep 1s
\cp /root/nico/aff.py /root/subweb/api/aff.py                    #前端，后端地址定义           使用本脚本前在root/nico 文件夹下放置对应的文件
\cp /root/nico/pref.ini /root/subweb/config/pref.ini             #后端基础配置定义
\cp /root/nico/mydocker.sh /root/subweb/docker.sh                #docker进程监控运行脚本       mydocker.sh 可以参考subweb/docker/mydocker.sh 进行修改
\cp /root/nico/templates/* /root/subweb/templates/               #网页自定义
chmod 777 /root/subweb/config/subconverter
chmod 777 /root/subweb/docker.sh
echo "------------------------------------DONE---------------------------------------"