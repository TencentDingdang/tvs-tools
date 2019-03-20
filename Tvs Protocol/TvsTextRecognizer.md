### 文本识别事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsTextRecognizer",
            "name": "Recognize",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "text": "{{STRING}}"
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
|    text                            |    string    |    Yes    |    文本                                |