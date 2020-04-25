# Docker运行
  - 1.安装Docker运行环境： 
  ```bash
  docker pull niconewbeee/subweb:basic
  ```
  - 2.下载源码：
  ```bash
  cd 
  git clone https://github.com/lzdnico/subweb.git 
  ```
  - 3.客制化（必须修改）：
  ```bash 
  chmod 777 /root/subweb/config/subconverter                  修改后端权限
  \cp /root/subweb/docker/mydocker.sh /root/subweb/docker.sh  修改启动脚本
  chmod 777 /root/subweb/docker.sh                            修改启动脚本权限
  修改api/aff.py                                              subip 和 apiip 分别为docker映射前的前端地址和后端地址 
  ```
  - 4.客制化（可选）：
  ```bash 
  修改config/perf.ini                                          端口10010不用修改，可以通过docker映射自定义访问端口
  修改templates                                                文件下的网页html
  ```
  - 5.开始运行：
  -p 前端端口号：10086 -p 后端端口号：10010                      这个前/后端端口号需要与api/aff.py中的一致
  ```bash 
  docker run  -d --restart=always -v /root/subweb:/subweb -p 10086:10086 -p 10010:10010  niconewbeee/subweb:basic
  ```