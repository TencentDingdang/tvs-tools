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
            "text": "{{STRING}}",
			"timbre": "{{STRING}}",
			"volume": {{LONG}},
			"speed": {{LONG}},
			"pitch": {{LONG}}
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
|	timbre						|	string	|	No	|	音色<br>ZHOULONGFEI<br>CHENANQI<br>YEZI<br>YEWAN<br>DAJI<br>LIBAI<br>NAZHA<br>MUZHA<br>WY	|
|	volume						|	long		|	No	|	音量(0~100,默认100)	|
|	speed						|	long		|	No	|	语速(0~100,默认50)	|
|	pitch							|	long		|	No	|	声调(0~100,默认50)	|

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
            "type": "{{STRING}}",
            "message": "{{STRING}}"
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