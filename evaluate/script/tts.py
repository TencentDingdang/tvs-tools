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

# 腾讯叮当提供的Bot Key/Secret
botKey = 'bot_key'
botSecret = 'bot_secret'
botKey = '544fb88b-4944-4110-88f1-8e89b2902c4d'
botSecret = b'bb8b659ae9894d56b8991cd42140de7e'
botKey = 'f6d5a9b8-003c-4ec5-aa79-bac5f2d50f38'
botSecret = b'0ffefed0b8eb4dc6800a3452e50a21ec'
botKey = '24fa48d8-f52e-467c-b896-2ee66a10f644'
botSecret = b'78145981238a4023a92016d29badb553'

# botKey = '1e02ddd9-7528-46c7-903b-1e4b01e8912e'
# botSecret = 'f6ab3a6cc3bc48dca1e3e20470536ff4'



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
    
requestUrl = 'https://aiwx.sparta.html5.qq.com/api/tts'

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
    print ('HTTP Status Code:%d' % r.status_code, 'cost:%f' %(respTime - reqTime));

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

    
