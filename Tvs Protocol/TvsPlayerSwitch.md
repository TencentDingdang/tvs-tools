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
			"srcOffsetInMillseconds": {{LONG}},
            "dstToken": "{{STRING}}",
			"dstType": "{{STRING}}",
			"dstId": "{{STRING}}",
			"dstOffsetInMillseconds": {{LONG}}
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|

***Payload Paramters***

|	Parameter						|	Type		|	必选	|	描述						|
|	:-------------------------------	|	:--------	|	:-----	|	:------------------------	|
|	srcToken						|	string	|	Yes	|	来源播放器Token	|
|	srcType							|	string	|	Yes	|	来源播放器类型:<br>AudioPlayer<br>OtherPlayer<br>ShortVideoPlayer		|
|	srcId								|	string	|	No	|	来源播放器Id			|
|	srcOffsetInMillseconds	|	long		|	No	|	来源播放器偏移量	|
|	dstToken						|	string	|	Yes	|	目的播放器Token	|
|	dstType							|	string	|	Yes	|	目的播放器类型:<br>AudioPlayer<br>OtherPlayer<br>ShortVideoPlayer		|
|	dstId								|	string	|	No	|	目的播放器Id			|
|	dstOffsetInMillseconds	|	long		|	No	|	目的播放器偏移量	|

