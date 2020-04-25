#! /bin/sh 
echo "-----------------------------------Start-------------------------------------"
pkill subconverter
sleep 1s
pkill python3
sleep 1s
echo "---------------------------------- Kill--- ----------------------------------"
cd /root/subweb
git reset --hard HEAD
sleep 1s
git pull
echo "----------------------------------Update-------------------------------------"
sleep 1s
chmod 777 /root/subweb/config/subconverter
\cp /root/nico/aff.py /root/subweb/api/aff.py
echo "---------------------------------Rewrite File---------------------------------"
sleep 1s
cd /root/subweb/config
./subconverter &
echo "--------------------------------subconverter-----------------------------------"
sleep 1s
cd /root/subweb
python3 api.py &
echo "------------------------------------WEB----------------------------------------"