### Session识别事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsSessionRecognizer",
            "name": "Recognize",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "session": "{{STRING}}"
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

|    Parameter                    |    Type        |    必选    |    描述                                |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    session                        |    string    |    Yes    |    SESSION信息                |

### 期待Session指令
```json
{
    "context": [...],
    "directive": {
        "header": {
            "namespace": "TvsSessionRecognizer",
            "name": "ExpectSession",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "timeoutInMilliseconds": {{LONG}}
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

|    Parameter                    |    Type        |    必选    |    描述                                |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    timeoutInMilliseconds    |    long        |    Yes    |    超时时间(0,不超时)            |

### 期待Session超时事件
```json
{                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsSessionRecognizer",
            "name": "ExpectSessionTimeOut",
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