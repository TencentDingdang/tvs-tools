### 进入儿童模式指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "EnterChildMode",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
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
|	dialogRequestId	|	string	|	Yes	|	对话ID							|

### 进入儿童模式成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "EnterChildModeSucceeded",
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

### 进入儿童模式失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "EnterChildModeFailed",
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


### 退出儿童模式指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "LeaveChildMode",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
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
|	dialogRequestId	|	string	|	No	|	对话ID							|

### 退出儿童模式成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "LeaveChildModeSucceeded",
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

### 退出儿童模式失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "LeaveChildModeFailed",
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

### 模式切换指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "SwitchMode",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"srcMode": "{{STRING}}",
			"dstMode": "{{STRING}}"
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

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	srcMode			|	string	|	Yes	|	来源模式:<br>NORMAL,普通模式<br>LEARNING,学习模式	|
|	dstMode			|	string	|	Yes	|	目的模式:<br>NORMAL,普通模式<br>LEARNING,学习模式	|

### 模式切换成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "SwitchModeSucceeded",
            "messageId": "{{STRING}}"
		},
		"payload": {
			"srcMode": "{{STRING}}",
			"dstMode": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	srcMode			|	string	|	Yes	|	来源模式:<br>NORMAL,普通模式<br>LEARNING,学习模式	|
|	dstMode			|	string	|	Yes	|	目的模式:<br>NORMAL,普通模式<br>LEARNING,学习模式	|

### 模式切换失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsModeControl",
			"name": "SwitchModeFailed",
            "messageId": "{{STRING}}"
		},
		"payload": {
			"srcMode": "{{STRING}}",
			"dstMode": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	srcMode			|	string	|	Yes	|	来源模式:<br>NORMAL,普通模式<br>LEARNING,学习模式	|
|	dstMode			|	string	|	Yes	|	目的模式:<br>NORMAL,普通模式<br>LEARNING,学习模式	|
