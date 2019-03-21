### 播放命令事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlaybackController",
            "name": "PlayCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```
***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

### 暂停命令事件
```json
{
    "context": [...],
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlaybackController",
            "name": "PauseCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |