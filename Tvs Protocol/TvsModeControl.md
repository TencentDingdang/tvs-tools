### 情景模式上下文
```json
{
	"header": {
		"namespace": "TvsProfileInformation",
		"name": "ProfileState"
	},
	"payload": {
		"mainMode": "{{STRING}}",
		"extraMode": "{{STRING}}"
	}
}
```

***Payload Paramters***

|	Parameter						|	Type		|	必选		|	描述					|
|	:---------------------------		|	:--------	|	:-----		|	:-------------------	|
|	mainMode						|	string	|	No		|	当前模式:<br>LEARNING,学习模式	<br>CHLIDREN,儿童模式<br>FAMILY,家庭模式<br>NORMAL,普通模式|
|	extraMode						|	string	|	No		|	当前模式:<br>CHILDREN_LOCK,儿童锁定模式|

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

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId    |    string    |    Yes    |    对话ID                            |

***Payload Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    srcMode            |    string    |    Yes    |    来源模式:<br>NORMAL,普通模式<br>LEARNING,学习模式    |
|    dstMode            |    string    |    Yes    |    目的模式:<br>NORMAL,普通模式<br>LEARNING,学习模式    |

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

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    srcMode            |    string    |    Yes    |    来源模式:<br>NORMAL,普通模式<br>LEARNING,学习模式    |
|    dstMode            |    string    |    Yes    |    目的模式:<br>NORMAL,普通模式<br>LEARNING,学习模式    |

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

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    srcMode            |    string    |    Yes    |    来源模式:<br>NORMAL,普通模式<br>LEARNING,学习模式    |
|    dstMode            |    string    |    Yes    |    目的模式:<br>NORMAL,普通模式<br>LEARNING,学习模式    |
