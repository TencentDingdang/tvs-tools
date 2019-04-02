# 1, download the script to local
# 2, chmod 755 xxx
# 3, run script
# 4, check whether include "TLSv1.2" or "TLSv1.1"? if no, you need upgrade.
openssl ciphers -v | awk '{print $2}' | sort | uniq

