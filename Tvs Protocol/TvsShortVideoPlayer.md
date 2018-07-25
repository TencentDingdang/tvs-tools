### 播放指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsShortVideoPlayer",
			"name": "Play",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
            "videoItem": {
                "videoItemId": "{{STRING}}",
                "stream": {
                	"url": "{{STRING}}",
                    "offsetInMilliseconds": {{LONG}},
                    "expiryTime": "{{STRING}}",
                    "progressReport": {
                    	"progressReportDelayInMilliseconds": {{LONG}},
                        "progressReportIntervalInMilliseconds": {{LONG}}
                   	},
                    "token": "{{STRING}}"
                }
            }
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

|	Parameter																							|	Type		|	必选	|	描述								|
|	:----------------------------------------------------------------------------------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	videoItem																							|	object	|	Yes	|	视频对象						|
|	videoItem.videoItemId																			|	string	|	Yes	|	视频对象ID					|
|	videoItem.stream																				|	object	|	Yes	|	视频对象流					|
|	videoItem.stream.url																			|	object	|	Yes	|	视频对象URL					|
|	videoItem.stream.offsetInMilliseconds													|	long		|	Yes	|	视频对象播放开始位置	|
|	videoItem.stream.token																		|	string	|	Yes	|	视频对象token				|
|	videoItem.stream.expiryTime																|	string	|	No	|	视频对象过期时间			|
|	videoItem.stream.progressReport															|	object	|	No	|	进度上报						|
|	videoItem.stream.progressReport.progressReportDelayInMilliseconds		|	string	|	No	|	进度上报延迟时间点		|
|	videoItem.stream.progressReport	.progressReportIntervalInMilliseconds	|	string	|	No	|	进度上报间隔					|

###播放开始事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackStarted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###播放快结束事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackNearlyFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###进度上报延迟到达事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "ProgressReportDelayElapsed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###进度上报间隔到达事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "ProgressReportIntervalElapsed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###播放卡顿开始事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackStutterStarted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###播放卡顿结束事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackStutterFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}},
            "stutterDurationInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter								|	Type		|	必选	|	描述								|
|	:---------------------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token									|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds				|	long		|	Yes	|	偏移量							|
|	stutterDurationInMilliseconds	|	long		|	Yes	|	卡顿时长						|

###播放结束事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###播放失败事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "currentPlaybackState": {
                "token": "{{STRING}}",
                "offsetInMilliseconds": {{LONG}},
                "playerActivity": "{{STRING}}"
            },
            "error": {
                "type": "{{STRING}}",
                "message": "{{STRING}}"
            }
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter													|	Type		|	必选	|	描述									|
|	:-----------------------------------------------------------	|	:--------	|	:-----	|	:--------------------------------		|
|	token														|	string	|	Yes	|	播放失败的视频对象token	|
|	currentPlaybackState									|	object	|	Yes	|	当前播放状态						|
|	currentPlaybackState.token						|	string	|	Yes	|	当前播放器token				|
|	currentPlaybackState.offsetInMilliseconds	|	long		|	Yes	|	偏移量								|
|	currentPlaybackState.playerActivity				|	string	|	Yes	|	当前播放器状态					|
|	error															|	object	|	Yes	|	错误									|
|	error.type													|	string	|	Yes	|	错误类型							|
|	error.message											|	string	|	Yes	|	错误消息							|

###停止播放指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "Stop",
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

###播放已停止事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackStopped",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:----------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###播放已暂停事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackPaused",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:----------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###播放已恢复事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "PlaybackResumed ",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:----------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	offsetInMilliseconds	|	long		|	Yes	|	偏移量							|

###视频流元数据解析成功事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsShortVideoPlayer",
            "name": "StreamMetadataExtracted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "metadata": {
                "{{STRING}}": "{{STRING}}",
                "{{STRING}}": {{BOOLEAN}},
                "{{STRING}}": "{{STRING NUMBER}}"
            }
        }
    }
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:----------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	token						|	string	|	Yes	|	视频对象token				|
|	metadata					|	object	|	Yes	|	视频流元信息					|