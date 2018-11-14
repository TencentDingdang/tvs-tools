### 取消事件
```json
{
    "event": {
        "header": {
            "namespace": "ExceptionReporter",
            "name": "Cancel",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "dialogRequestId": "{{STRING}}"
		}
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	dialogRequestId			|	string	|	Yes	|	对话ID				|

### 期待语音超时事件
```json
{
    "event": {
        "header": {
            "namespace": "ExceptionReporter",
            "name": "ExpectSpeechTimeOut",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "dialogRequestId": "{{STRING}}"
		}
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	dialogRequestId			|	string	|	Yes	|	对话ID				|