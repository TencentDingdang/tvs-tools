### 播放器切换事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsPlayerSwitch",
            "name": "Switch",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "srcToken": "{{STRING}}",
            "srcType": "{{STRING}}",
            "srcId": "{{STRING}}",
            "srcPlayerActivity": "{{STRING}}",
            "srcOffsetInMilliseconds": {{LONG}},
            "dstToken": "{{STRING}}",
            "dstType": "{{STRING}}",
            "dstId": "{{STRING}}",
            "dstPlayerActivity": "{{STRING}}",
            "dstOffsetInMilliseconds": {{LONG}}
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                        |    Type        |    必选    |    描述                        |
|    :-------------------------------    |    :--------    |    :-----    |    :------------------------    |
|    srcToken                        |    string    |    Yes    |    来源播放器Token    |
|    srcType                            |    string    |    Yes    |    来源播放器类型:<br>AudioPlayer<br>OtherPlayer<br>ShortVideoPlayer        |
|    srcId                                |    string    |    No    |    来源播放器Id            |
|    srcPlayerActivity            |    string    |    Yes    |    来源播放器状态        |
|    srcOffsetInMilliseconds    |    long        |    No    |    来源播放器偏移量    |
|    dstToken                        |    string    |    Yes    |    目的播放器Token    |
|    dstType                            |    string    |    Yes    |    目的播放器类型:<br>AudioPlayer<br>OtherPlayer<br>ShortVideoPlayer        |
|    dstId                                |    string    |    No    |    目的播放器Id            |
|    dstPlayerActivity            |    string    |    Yes    |    目的播放器状态        |
|    dstOffsetInMilliseconds    |    long        |    No    |    目的播放器偏移量    |