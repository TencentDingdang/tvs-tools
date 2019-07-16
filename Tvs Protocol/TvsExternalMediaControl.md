### 外部媒体播放控制上下文
```json
{
	"header": {
		"namespace":"TvsExternalMediaControl",
		"name":"PlaybackState"
	},
	"payload": {
		"playerActivity": "{{STRING}}",
		"playerMode": "{{STRING}}",
		"offsetInMilliseconds": {{LONG}},
		"currentDataId": "{{STRING}}",
		"previousDataId": "{{STRING}}",
		"nextDataId": "{{STRING}}"
	}
}
```

***Payload Parameters***

|	Parameter							|	Type		|	必选	|	描述																|
|	:------------------------------------	|	:--------	|	:-----	|	:------------------------------------------------------------------	|
|	playerMode						|	string	|	Yes	|	当前模式<br>Audio:音频(默认)<br>Video:视频	|
|	playerActivity						|	string	|	Yes	|	播放器状态													|
|	offsetInMilliseconds			|	long		|	Yes	|	偏移量															|
|	currentDataId						|	string	|	No	|	当前数据ID													|
|	previousDataId					|	string	|	No	|	上一个数据ID													|
|	nextDataId							|	string	|	No	|	下一个数据ID													|

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

### 外部媒体控制播放成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "PlaySucceeded",
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

### 外部媒体控制播放失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "PlayFailed",
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

### 外部媒体控制停止指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "Stop",
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

### 外部媒体控制停止成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "StopSucceeded",
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

### 外部媒体控制停止失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "StopFailed",
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

### 外部媒体控制上一个成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "PreviousSucceeded",
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

### 外部媒体控制上一个失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "PreviousFailed",
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

### 外部媒体控制下一个成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "NextSucceeded",
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

### 外部媒体控制下一个失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsExternalMediaControl",
			"name": "NextFailed",
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