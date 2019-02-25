### 上报指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsCustomControl",
			"name": "Report",
            "messageId": "{{STRING}}"
		},
		"payload": {
            "token": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter						|	Type		|	必选	|	描述						|
|	:-------------------------------	|	:--------	|	:-----	|	:------------------------	|
|	token							|	string	|	Yes	|	token					|

### 上报开始事件
```json
{
	"context": [...],
	"event": {
		"header": {
			"namespace": "TvsCustomControl",
			"name": "Started",
            "messageId": "{{STRING}}"
		},
		"payload": {
            "token": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter						|	Type		|	必选	|	描述						|
|	:-------------------------------	|	:--------	|	:-----	|	:------------------------	|
|	token							|	string	|	Yes	|	token					|

### 上报结束事件
```json
{
	"context": [...],
	"event": {
		"header": {
			"namespace": "TvsCustomControl",
			"name": "Finished",
            "messageId": "{{STRING}}"
		},
		"payload": {
            "token": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter						|	Type		|	必选	|	描述						|
|	:-------------------------------	|	:--------	|	:-----	|	:------------------------	|
|	token							|	string	|	Yes	|	token					|