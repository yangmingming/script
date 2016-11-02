#!/bin/bash
# @file         install-openvpn.sh 
# @author       ymm
# @brief        安装openvpn
#               /etc/openvpn/easy-rsa/2.0/ 生成客户端配置文件 "client.ovpn"
# @date         2016-11-02	
# @History
# 1. 2016-11-02  author ymm    初步完成

#remote ip
IP="192.168.30.30"

#iptables need
INTERFACE="eth1"

#client name
CLIENT_NAME="ymm"

#check network interface
ifconfig -a |grep "^${INTERFACE}"
if [ "0" != "$?" ];then
    echo "set the network interface error"
    exit 0
fi

yum install epel-release -y
yum install openvpn libssl-dev openssl easy-rsa -y

openvpn --version
if [ "1" != "$?" ];then
    echo "openvpn install error"
    exit 0
fi

mkdir /etc/openvpn/easy-rsa
cp  -r /usr/share/easy-rsa/* /etc/openvpn/easy-rsa/

#must cd the director first
cd /etc/openvpn/easy-rsa/2.0/
#keep default
source /etc/openvpn/easy-rsa/2.0/vars

./clean-all

sed -i 's/--interact//g' ./build-ca 
./build-ca && cp keys/ca.crt /etc/openvpn/

echo "KEY_NAME = $KEY_NAME"

sed -i 's/--interact//g' ./build-key-server
./build-key-server $KEY_NAME && cp keys/EasyRSA.crt keys/EasyRSA.key /etc/openvpn/

./build-dh && cp keys/dh2048.pem /etc/openvpn/

sed -i 's/--interact//g' ./build-key
./build-key ${CLIENT_NAME}

ls keys

cp /usr/share/doc/openvpn-2.3.12/sample/sample-config-files/server.conf /etc/openvpn/

cat <<!
/etc/openvpn/server.conf will modify as follow [only main content]:

port 1194
proto tcp
dev tun
ca ca.crt
cert ${CLIENT_NAME}.crt
key ${CLIENT_NAME}.key
dh dh2048.pem
server 10.18.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 114.114.114.114"
push "dhcp-option DNS 114.114.115.115"
duplicate-cn
keepalive 10 120
comp-lzo
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
verb 3
!
echo "Now, please edit file /etc/openvpn/server.conf"
mv /etc/openvpn/server.conf /etc/openvpn/server.conf.bak
cat /etc/openvpn/server.conf.bak \
|sed 's/^[;]*por tun/port/g' \
|sed 's/^[;]*proto tcp/proto tcp/g' \
|sed 's/^[;]*proto udp/#proto udp/g' \
|sed 's/^[;]*dev tun/dev tun/g' \
|sed 's/^[;]*ca/ca/g' \
|sed "s/^[;]*cert.*$/cert ${KEY_NAME}.crt/g" \
|sed "s/^[;]*key.*$/key ${KEY_NAME}.key/g" \
|sed 's/^[;]*dh/dh/g' \
|sed 's/^[;]*server /server /g' \
|sed 's/^[;]*ifconfig-pool-persist/ifconfig-pool-persist/g' \
|sed 's/^[;]*push \"redirect-gateway def1 bypass-dhcp\"/push \"redirect-gateway def1 bypass-dhcp\"\npush \"dhcp-option DNS 114.114.114.114\"\npush \"dhcp-option DNS 114.114.114.114\"/g' \
|sed 's/^[;]*duplicate-cn/duplicate-cn/g' \
|sed 's/^[;]*keepalive/keepalive/g' \
|sed 's/^[;]*comp-lzo/comp-lzo/g' \
|sed 's/^[;]*user/user/g' \
|sed 's/^[;]*group/group/g' \
|sed 's/^[;]*persist-key/persist-key/g' \
|sed 's/^[;]*persist-tun/persist-tun/g' \
|sed 's/^[;]*status/status/g' \
|sed 's/^[;]*verb/verb/g' \
>/etc/openvpn/server.conf

#cat server.conf|sed  's/^[;]*port/port/g'|sed 's/^[;]*proto tcp/proto tcp/g' |sed 's/^[;]*proto udp/;proto udp/g'|sed  's/^[;]*dev tun/dev tun/g'|grep 'ca ca.crt'

#backup your /etc/sysctl.conf
cp /etc/sysctl.conf /etc/sysctl.conf.$(date +%Y%m%d%H%M%S)
sed 's/net.ipv4.ip_forward.*$/net.ipv4.ip_forward = 1/g' /etc/sysctl.conf

#(eth0根据你的网卡修改)
iptables -t nat -A POSTROUTING -s 10.18.0.0/24 -o ${INTERFACE} -j MASQUERADE 

/etc/init.d/openvpn start
if [ "0" == "$?" ];then
    echo "openvpn start success ..."
fi

{
cat <<!
client
dev tun
proto tcp
resolv-retry infinite
nobind
persist-key
persist-tun
ns-cert-type server
comp-lzo
verb 3

!
echo "remote ${IP} 1194"
echo "<ca>";cat ./keys/ca.crt;echo "</ca>"
echo "<cert>";cat ./keys/${CLIENT_NAME}.crt|sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p';echo "</cert>"
echo "<key>";cat ./keys/${CLIENT_NAME}.key;echo "</key>"
} >client.ovpn

if [ "0" == "$?" ];then
    echo "create client configure file [/etc/openvpn/easy-rsa/2.0/client.ovpn] success"
fi
