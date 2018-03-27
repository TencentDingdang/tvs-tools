# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install request`

# 腾讯叮当提供的Bot Key/Secret
botKey = 'bot_key'
botSecret = 'bot_secret'

# ***** Task 1: 拼接请求数据和时间戳 *****

## 获取请求数据(也就是HTTP请求的Body)
postData = '{"header": {"guid": "guid","qua": "QV=3&PL=ADR&PR=chvoice&VE=7.6&VN=3350&PP=com.tencent.mtt&DE=TV","user": {"user_id": ""},"ip": "", "lbs":{"latitude":30.5434, "longitude":104.068}},"payload": {"query": "今天天气如何"}}'
## 获得ISO8601时间戳
credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

## 拼接数据
signingContent = postData + credentialDate

# ***** Task 2: 获取Signature签名 *****
signature = hmac.new(botSecret, signingContent.encode('utf-8'), hashlib.sha256).hexdigest()

# ***** Task 3: 在HTTP请求头中带上签名信息
authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + botKey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature

headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorizationHeader}

# **** Send the request *****
requestUrl = 'https://aiwx.sparta.html5.qq.com/api/v1/richanswer'

print ('Begin request...')
print ('Request Url = ' + requestUrl)

## 使用requests.session保持长连接
session = requests.session()
session.headers.update(headers)
print ('Request Headers =' + str(session.headers))
print ('Request Body =' + postData)

r = session.post(requestUrl, data = postData.encode('utf-8'))

print ('Response...')
print ('HTTP Status Code:%d' % r.status_code)
print (r.text)
