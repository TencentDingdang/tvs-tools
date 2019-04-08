# 1, download the script to local
# 2, chmod 755 xxx
# 3, run script
# 4, check whether include "TLSv1.2" or "TLSv1.1"? if no, you need upgrade.
tls_version=$(openssl ciphers -v | awk '{print $2}' | sort -rV | uniq | head -n 1)
echo "SSL/TLS version : "$tls_version

right_version="TLSv1.1"

#if [ -z "$tls_version" ];then
#echo "TLS version error, you need upgrade!"
#exit 0
#fi

if [ "$tls_version" \> "$right_version" ] || [ "$tls_version" == "$right_version" ];then
	echo "=========================TLS version is OK!========================="  
else
	echo "-------------------------TLS version error, you need upgrade!-------------------------"
fi


