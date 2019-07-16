### 语音识别器上下文
```json
{
    "header": {
        "namespace": "SpeechRecognizer",
        "name": "RecognizerState"
    },
    "payload": {
		"wakeword": "{{STRING}}",
		"isNoWakeEnabled": {{BOOLEAN}}
    }
}
```

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	wakeword					|	string	|	Yes	|	唤醒词							|
|	isNoWakeEnabled		|	boolean	|	No	|	是否免唤醒开启				|

### 语音识别事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "SpeechRecognizer",
            "name": "Recognize",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "profile": "{{STRING}}",
            "format": "{{STRING}}",
            "initiator": {
                "type": "{{STRING}}",
                "payload": {
                    "wakeWordIndices": {
                        "startIndexInSamples": {{LONG}},
                        "endIndexInSamples": {{LONG}}
                    },
                    "token": "{{STRING}}"   
                }
            },
            "language": "{{STRING}}",
            "resultType": "{{STRING}}",
            "extraOperation": "{{STRING}}",
            "continuation": {
                "token": "{{STRING}}",
                    "dialogRequestId": "{{STRING}}"
            },
            "strategy": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                                |    Type        |    必选    |    描述                                                                            |
|    :---------------------------------------    |    :--------    |    :-----    |    :---------------------------------------------------------------------------    |
|    language                                |    string    |    No    |    语言类型<br>CHINESE:中文<br>ENGLISH:英文            |
|    resultType                                |    string    |    No    |    结果类型<br>DEFAULT,默认;<br>ASR,语音识别            |
|    extraOperation                        |    string    |    No    |    额外操作<br>SEMANTIC_FORCE_SESSION_COMPLETE,语义-强制Session结束    |
|    continuation                            |    object    |    No    |    连续操作                                                                    |
|    continuation.token                    |    string    |    No    |    ExpectSpeech指令的token                                                            |
|    continuation.dialogRequestId    |    string    |    No    |    连续操作对话ID                                                            |
|    strategy                                    |    string    |    No    |    策略名                                                                        |