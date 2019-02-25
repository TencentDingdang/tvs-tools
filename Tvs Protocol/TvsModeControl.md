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
	"directive": {
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
	"directive": {
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
	"directive": {
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
	"directive": {
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