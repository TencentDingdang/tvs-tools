### 语义识别事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsSemanticRecognizer",
            "name": "Recognize",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "semantic": "{{STRING}}"
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

|    Parameter                    |    Type        |    必选    |    描述                                                        |
|    :---------------------------    |    :--------    |    :-----    |    :-------------------------------------------------------    |
|    semantic                    |    string    |    Yes    |    语义信息(领域将语义序列化为Json格式)    |



***能力***

能够让终端直接携带明确语义请求TVS。功能与`SpeechRecognizer.Recognize`一致，只是`SpeechRecognizer.Recognize`是语音触发。