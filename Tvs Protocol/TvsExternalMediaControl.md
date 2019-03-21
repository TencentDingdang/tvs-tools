### 外部媒体控制播放指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "Play",
            "messageId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

### 外部媒体控制暂停指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "Pause",
            "messageId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

### 外部媒体控制上一个指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "Previous",
            "messageId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

### 外部媒体控制下一个指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "Next",
            "messageId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

### 外部媒体控制下载指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "Download",
            "messageId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|