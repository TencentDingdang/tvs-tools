# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install requests`
import base64
import json
import time
import sys
import wav

usage = '''
####
#   usage:
#   python tts.py Outfile Text
#   Outfile, 输出文件
#   Text, TTS需要合成的文本
####
'''

if (3 > len(sys.argv)) :
    print (usage);
    sys.exit(0);

# 腾讯叮当提供的Bot Key/Secret，请填入自己的bot_key
botKey = "XXXX";
botSecret = b"YYYY";

## 获取请求数据(也就是HTTP请求的Body)
postData = '''
{
    "header": 
    {
        "guid": "guid",
        "qua": "QV=3&PL=ADR&PR=chvoice&VE=7.6&VN=3350&PP=com.tencent.mtt&DE=TV",
        "user": 
        {
            "user_id": ""
        },
        "ip": "", 
        "lbs":
        {
            "latitude":30.5434, 
            "longitude":104.068
        }
    },
    "payload": 
    {
        "speech_meta":
        {
            "compress":"WAV",
            "person":"DAJI"
        },
        "session_id":"",
        "index":0,
        "single_request":false,
        "content":
        {
            "text":"双鱼座今天的运势很好，不管是生意上，还是工作上，今天的你都会有很好的机遇，记得要低调，低调，再低调！"
        }
    }
}
'''

jsonReq = json.loads(postData);
if (3 >= len(sys.argv)) :
    jsonReq["payload"]["content"]["text"] = sys.argv[2];
    
requestUrl = 'https://aiwx.html5.qq.com/api/tts'

print ('Begin request...')
print ('Request Url = ' + requestUrl)

## 使用requests.session保持长连接
session = requests.session();

allRawData = b"";
error = 0;
while 1 :
    # ***** Task 1: 拼接请求数据和时间戳 *****
    ## 获得ISO8601时间戳
    credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

    ## 拼接数据
    signingContent = json.dumps(jsonReq) + credentialDate

    # ***** Task 2: 获取Signature签名 *****
    signature = hmac.new(botSecret, signingContent.encode('utf-8'), hashlib.sha256).hexdigest()

    # ***** Task 3: 在HTTP请求头中带上签名信息
    authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + botKey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature

    headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorizationHeader};
    
    session.headers.update(headers)   
    # **** Send the request *****
    
    reqTime = time.time();
    r = session.post(requestUrl, data = json.dumps(jsonReq).encode('utf-8'))
    respTime = time.time();
    
    print ('Response...')
    print ('HTTP Status Code:%d' % r.status_code, 'cost:%f(ms)' %((respTime - reqTime) * 1000));

    if 200 != r.status_code : 
        print("出错了！");
        break;

    jsonResp = json.loads(r.text);
    allRawData += base64.b64decode(jsonResp["payload"]["speech_base64"]);
    
    if True == jsonResp["payload"]["speech_finished"] :
        print("结束了！");
        break;
    else :
        if 0 == len(jsonResp["header"]["session"]["session_id"]) :
            error = 1;
            print("出错了!");
            break;
        else :
            jsonReq["payload"]["session_id"] = jsonResp["header"]["session"]["session_id"];
            jsonReq["payload"]["index"] += 1;

if (0 == error) :
    file = open(sys.argv[1], "wb+");
    fileData = b"";
    if (False == jsonReq["payload"]["single_request"]) :
        fileData = wav.genWaveHeader(allRawData) + allRawData;
    else :
        fileData = allRawData;
    file.write(fileData);            
    file.close();

    
