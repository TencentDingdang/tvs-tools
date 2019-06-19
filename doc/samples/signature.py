# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install request`
import json, sys, time, base64

# 开放平台提供的appkey/accessToken，请填入自己的appkey
appkey = "XXXX";
accessToken = b"YYYYY";


# ***** 第一步: 拼接请求数据和时间戳 *****

## 获取请求数据(也就是HTTP请求的Body)
postData = '''
{
    "header": 
    {
        "device": {
            "serial_num":"myserial"
        },
        "qua": "QV=3&PL=ADR&PR=chvoice&VE=7.6&VN=3350&PP=com.tencent.mtt&DE=TV",
        "lbs":
        {
            "latitude":30.5434, 
            "longitude":104.068
        }
    },
    "payload": 
    {
        "query": "今天天气如何"
    }
}
'''

jsonReq = json.loads(postData);
 
## 这里修改query
jsonReq["payload"]["query"] = "今天天气如何";

## 使用requests.session保持长连接
session = requests.session()

## 获得ISO8601时间戳
credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
print("时间戳:"+credentialDate)
## 拼接数据
signingContent = json.dumps(jsonReq) + credentialDate
print("signingContent为:\n"+signingContent)
print("\n")
# ***** 第二步: 获取Signature签名 *****
signature = hmac.new(accessToken, signingContent.encode('utf-8'), hashlib.sha256).hexdigest()
print("签名为:"+signature)

# ***** 第三步: 组装Authorization，在HTTP请求头中带上签名信息
authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + appkey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature
print("Authorization拼接结果为:"+authorizationHeader)

headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorizationHeader}
 

 
 