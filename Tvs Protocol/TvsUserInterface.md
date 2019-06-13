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
            "baseInfo": {
                "domain": "{{STRING}}",
                "intent": "{{STRING}}"
            },
            "jsonUI": {
                "compress": "{{STRING}}",
                "data": "{{STRING}}",
                "tipsText": "{{STRING}}"
            },
            "jsonSemantic": {
                "compress": "{{STRING}}",
                "data": "{{STRING}}"
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
|    baseInfo                            |    string    |    Yes    |    基本信息                                                                                |
|    baseInfo.domain                    |    string    |    Yes    |    领域                                                                                        |
|    baseInfo.intent                    |    string    |    Yes    |    意图                                                                                        |
|    jsonUI                                |    string    |    Yes    |    UI信息                                                                                    |
|    jsonUI.compress                |    string    |    Yes    |    压缩格式<br>none:无压缩<br>gzip:GZIP压缩                            |
|    jsonUI.data                        |    string    |    Yes    | UI数据，各领域UI协议见[https://github.com/TencentDingdang/tvs-tools/tree/master/Tsk%20Protocol/domains_V3](https://github.com/TencentDingdang/tvs-tools/tree/master/Tsk Protocol/domains_V3) |
|    jsonUI.tipsText                    |    string    |    Yes    |    回复语呈现文本                                                                        |
|    jsonSemantic.compress        |    string    |    Yes    |    压缩格式<br>none:无压缩<br>gzip:GZIP压缩                            |
|    jsonSemantic.data                |    string    |    Yes    |    语义数据                                                                                |

### 选择事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsUserInterface",
            "name": "Selected",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "domain": "{{STRING}}",
            "intent": "{{STRING}}",
            "dataId": "{{STRING}}"
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
|    domain                |    string    |    Yes    |    领域                                |
|    intent                |    string    |    Yes    |    意图                                |
|    dataId                |    string    |    Yes    |    数据ID                            |


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
                "isFinal": {{BOOLEAN}},
                "userInfo": {
                    "userId": "{{STRING}}",
                    "gender": {{LONG}},
                    "age": {{LONG}}
                },
                "asrClassifierInfo": [
                    {
                        "classifier": "{{STRING}}",
                        "items": [
                            {
                                "label": {{LONG}},
                                "probability": {{FLOAT}}
                            },
                            {
                                "label": {{LONG}},
                                "probability": {{FLOAT}}
                            },
                        ]
                    },
                    {
                        "classifier": "{{STRING}}",
                        "items": [
                            {
                                "label": {{LONG}},
                                "probability": {{FLOAT}}
                            },
                            {
                                "label": {{LONG}},
                                "probability": {{FLOAT}}
                            },
                        ]
                    }
                ]
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
|    data.userInfo.userId                                    |    string    |    No    |    用户ID                            |
|    data.userInfo.gender                                    |    long        |    No    |    用户性别                        |
|    data.userInfo.age                                        |    long        |    No    |    用户年龄                        |
|    data.asrClassifierInfo                                    |    array        |    No    |    ASR分类器信息                |
|    data.asrClassifierInfo[].classifier                    |    string    |    No    |    ASR分类器名称                |
|    data.asrClassifierInfo[].items                        |    array        |    No    |    ASR分类器                    |
|    data.asrClassifierInfo[].items[].label                |    long        |    No    |    ASR分类器标签                |
|    data.asrClassifierInfo[].items[].probability        |    float        |    No    |    ASR分类器概率                |

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


### 播放模式指令
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
