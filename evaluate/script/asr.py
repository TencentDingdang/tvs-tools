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
requestUrl = 'https://aiwx.sparta.html5.qq.com/api/asr'

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
            