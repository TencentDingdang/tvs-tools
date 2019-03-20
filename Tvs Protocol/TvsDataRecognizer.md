### 数据识别事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsDataRecognizer",
            "name": "Recognize",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "data": "{{STRING}}",
            "token": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId    |    string    |    Yes    |    对话ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                        |
|    :---------------------------    |    :--------    |    :-----    |    :------------------------    |
|    data                            |    string    |    Yes    |    数据(BASE64)        |
|    token                        |    string    |    No    |    token信息(与ExpectData指令中的token对应)    |

### 期待数据指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDataRecognizer",
            "name": "ExpectData",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "token": "{{STRING}}",
            "timeoutInMilliseconds" : {{LONG}}
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId    |    string    |    Yes    |    对话ID                            |


***Payload Paramters***

|    Parameter                        |    Type        |    必选    |    描述                                                    |
|    :-------------------------------    |    :--------    |    :-----    |    :-----------------------------------------------------    |
|    type                                |    string    |    Yes    |    数据类型<br>IMAGE                            |
|    token                            |    string    |    Yes    |    token信息                                            |
|    timeoutInMilliseconds        |    string    |    Yes    |    超时时间(0,不超时)                                |

### 期待数据超时指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDataRecognizer",
            "name": "ExpectDataTimeOut",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |