### UI上下文
```json
{
	"header": {
		"namespace": "TvsUserInterface",
		"name": "ShowState"
	},
	"payload": {
		"isEnabled": {{BOOLEAN}},
		"version": "{{STRING}}"
	}
}
```

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	isEnabled					|	boolean	|	Yes	|	是否开启UI					|

### UI数据指令
```json
{
    "directive": {
        "header": {
            "namespace":"TvsUserInterface",
            "name":"Show",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "retCode": 0,
            "errMsg": "{{STRING}}",
            "session" : "{{STRING}}",
            "jsonUI": {
                "compress": "{{STRING}}",
                "data": "{{STRING}}",
                "tipsText": "{{STRING}}"
            }
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId    |    string    |    No    |    对应语音识别事件的ID    |

***Payload Paramters***

|    Parameter                            |    Type        |    必选    |    描述                                                                                        |
|    :------------------------------------    |    :--------    |    :-----    |    :----------------------------------------------------------------------------------------    |
|    retCode                                |    string    |    Yes    |    返回码                                                                                    |
|    errMsg                                |    string    |    Yes    |    错误消息                                                                                |
|    session                                |    string    |    No    |    SESSION信息                                                                        |
|    jsonUI                                |    string    |    Yes    |    UI信息                                                                                    |
|    jsonUI.compress                |    string    |    Yes    |    压缩格式<br>none:无压缩(默认)<br>gzip:GZIP压缩                            |
|    jsonUI.data                        |    string    |    Yes    | UI数据，协议见[TSK协议](https://github.com/TencentDingdang/tvs-tools/tree/master/Tsk%20Protocol) |
|    jsonUI.tipsText                    |    string    |    Yes    |    回复语呈现文本                                                                        |

### 实时ASR结果指令
    说明：该指令从下行通道发送

```json
{
    "directive": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "ASRShow",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "data": {
                "text": "{{STRING}}",
                "isFinal": {{BOOLEAN}}
			}
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId    |    string    |    No    |    对应语音识别事件的ID    |

***Payload Paramters***

|    Parameter                                                    |    Type        |    必选    |    描述                                |
|    :------------------------------------------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    data                                                            |    string    |    Yes    |    数据                                |
|    data.isFinal                                                |    bool        |    Yes    |    是否最终结果                    |
|    data.text                                                    |    string    |    Yes    |    文本                                |

### AudioPlayer进度改变事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "AudioPlayerProgressChanged",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "playerActivity": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    token                        |    string    |    Yes    |    AudioPlayer token            |
|    playerActivity                |    string    |    Yes    |    AudioPlayer状态            |
|    offsetInMilliseconds    |    long        |    Yes    |    偏移量                            |

### TvsShortVideoPlayer进度改变事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "TvsShortVideoPlayerProgressChanged",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "playerActivity": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    TvsShortVideoPlayer token        |
|    playerActivity                |    string    |    Yes    |    TvsShortVideoPlayer状态        |
|    offsetInMilliseconds    |    long        |    Yes    |    偏移量                                    |

### 收藏展示指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "CollectShow",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "id": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    id                                |    string    |    Yes    |    数据ID                            |

### 取消收藏展示指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "UncollectShow",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "id": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    id                                |    string    |    Yes    |    数据ID                            |

### 播放模式显示指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "PlayModeShow",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "mode": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    mode                        |    string    |    Yes    |    模式:<br>SingleMode:单曲<br>SingleCycleMode:单曲循环<br>ListMode:列表<br>ListCycleMode:列表循环<br>RandomMode:随机    |

### 音乐播放器进入MV模式事件
    说明：用户点击界面按钮上报

```json
{
    "context" : [...],
    "event": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "EnterMvCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```
***Header Parameters***

|    Parameter                            |    Type        |    必选    |    描述                            |
|    :------------------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    messageId                            |    string    |    Yes    |    消息ID                        |

### 音乐播放器离开MV模式事件
    说明：用户点击界面按钮上报

```json
{
    "context" : [...],
    "event": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "LeaveMvCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```
***Header Parameters***

|    Parameter                            |    Type        |    必选    |    描述                            |
|    :------------------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    messageId                            |    string    |    Yes    |    消息ID                        |

### 触发动作事件
```json
{
    "context" : [...],
    "event": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "ActionTriggered",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "actionDomain": "{{STRING}}",
            "actionType": "{{STRING}}",
            "actionParam": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter               	|    Type   	|    必选	|    描述                            	|
|    :---------------------------  	|    :-------- 	|    :-----	|    :--------------------------------	|
|    actionDomain          	|    string  	|    Yes	|    动作作用域					|
|    actionType          		|    string  	|    Yes	|    动作类型						|
|    actionParam          	|    string  	|    Yes	|    动作参数						|
