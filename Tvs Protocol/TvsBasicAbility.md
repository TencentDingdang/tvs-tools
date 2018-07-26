### TTS事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsBasicAbility",
			"name": "TextToSpeech",
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

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|
|	dialogRequestId	|	string	|	Yes	|	对话ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	text							|	string	|	Yes	|	需要TTS的文本	|


### 自定义消息指令
```json

{
    "directive": {
        "header": {
            "namespace": "TvsBasicAbility",
            "name": "CustomMessage",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "type":"{{STRING}}",
            "message":"{{STRING}}"
        }
    }
}   

```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|
|	dialogRequestId	|	string	|	No	|	对话ID							|


***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述													|
|	:---------------------------	|	:--------	|	:-----	|	:-----------------------------------------------------	|
|	type							|	string	|	No	|	标识消息类型，自定义						|
|	message					|	string	| 	No	|	消息内容，内容自定义，格式自行约定	|