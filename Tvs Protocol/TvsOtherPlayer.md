### 控制第三方播放器指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsOtherPlayer",
			"name": "Control",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
            "playerId": "{{STRING}}",
			"token": "{{STRING}}",
			"controlInfo" : "{{STRING}}"
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
|	playerId						|	string	|	Yes	|	标识					|
|	token						|	string	|	Yes	|	token				|
|	controlInfo					|	string	|	Yes	|	控制信息			|