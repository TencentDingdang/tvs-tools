# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install requests`
import json
import base64
import time
import sys
import wav;

usage = '''
####
#   usage:
#   python asr.py Infile
#   Infile, 输入文件
####
'''

if (2 > len(sys.argv)) :
    print (usage);
    sys.exit(0);

# 腾讯叮当提供的Bot Key/Secret，请填入自己的bot_key
botKey = 'bot_key'
botSecret = 'bot_secret'

# ***** Task 1: 拼接请求数据和时间戳 *****

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
        "voice_meta":
        {
            "compress":"PCM",
            "sample_rate":"16K",
            "channel":1
        },
        "session_id":"",
        "index":0,
        "voice_finished":false,
        "voice_base64":""
    }
}
'''



# **** Send the request *****
requestUrl = 'https://aiwx.html5.qq.com/api/asr'

print ('Begin request...')
print ('Request Url = ' + requestUrl)

## 使用requests.session保持长连接
session = requests.session();

jsonReq = json.loads(postData);
offset = 0;
file = open(sys.argv[1], "rb");
fileData = file.read();
file.close();
file = open(sys.argv[1], "rb");
if (fileData[0:44] == wav.genWaveHeader(fileData[44:])) :
    file.read(44);
    
while 1 :
    # ***** Task 1: 拼接请求数据和时间戳 *****
    ## 获得ISO8601时间戳
    credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

    data = file.read(3200);
    base64Data = base64.b64encode(data).decode();
    jsonReq["payload"]["voice_base64"] = base64Data;
    print("read length:" + str(len(data)));
    if (len(data) < 3200) :
        jsonReq["payload"]["voice_finished"] = True;
        
    offset += len(data);
    ## 拼接数据
    signingContent = json.dumps(jsonReq) + credentialDate;

    # ***** Task 2: 获取Signature签名 *****
    signature = hmac.new(botSecret, signingContent.encode('utf-8'), hashlib.sha256).hexdigest()

    # ***** Task 3: 在HTTP请求头中带上签名信息
    authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + botKey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature

    headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorizationHeader};
    
    session.headers.update(headers);
    # **** Send the request *****
    
    reqTime = time.time();
    r = session.post(requestUrl, data = json.dumps(jsonReq).encode('utf-8'));
    respTime = time.time();

    print ("reqTime:%f" % reqTime, "respTime:%f" % respTime); 
    print ('Response...')
    print ('HTTP Status Code:%d' % r.status_code, 'cost:%f' %(respTime - reqTime))

    if 200 != r.status_code : 
        file.close();
        print("出错了！");
        break;

    jsonResp = json.loads(r.text);
    print("result:" + jsonResp["payload"]["result"]);
    
    if True == jsonResp["payload"]["final_result"] or True == jsonReq["payload"]["voice_finished"]:
        file.close();
        print("结束了！");
        break;
    else :
        if 0 == len(jsonResp["header"]["session"]["session_id"]) :
            file.close();
            print("出错了!");
            break;
        else :
            jsonReq["payload"]["session_id"] = jsonResp["header"]["session"]["session_id"];
            jsonReq["payload"]["index"] = offset;
            