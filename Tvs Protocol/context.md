### 设备上下文
```json
{
    "header": {
        "namespace": "TvsDeviceControl",
        "name": "DeviceState"
    },
    "payload": {
		"monitor": {
			"state": "{{STRING}}",
        	"brightness": {{LONG}}
		},
		"camera": {
			"state": "{{STRING}}"
		},
        "microphone": {
			"state": "{{STRING}}"
		},
        "bluetooth": {
			"state": "{{STRING}}"
		},
		"battery": {
			"power": {{LONG}}
		}
    }
}
```
***Payload Parameters***

|	Parameter							|	Type		|	必选	|	描述								|
|	:------------------------------------	|	:--------	|	:-----	|	:---------------------------------	|
|	monitor								|	object	|	Yes	|	监视器							|
|	monitor.state						|	string	|	Yes	|	监视器状态					|
|	monitor.brightness				|	long		|	Yes	|	监视器亮度值[0~100]		|
|	camera								|	object	|	Yes	|	摄像头							|
|	camera.state						|	string	|	Yes	|	摄像头状态					|
|	microphone						|	object	|	Yes	|	麦克风							|
|	microphone.state				|	string	|	Yes	|	麦克风状态					|
|	bluetooth							|	object	|	Yes	|	蓝牙								|
|	bluetooth.state					|	string	|	Yes	|	蓝牙状态						|
|	battery								|	object	|	Yes	|	电池								|
|	battery.power						|	long		|	Yes	|	电池电量						|

### 第三方播放器上下文
```json
{
    "header": {
        "namespace": "TvsOtherPlayer",
        "name": "PlaybackState"
    },
    "payload": {
        "playerId": "{{STRING}}",
		"token": "{{STRING}}",
        "isTop": {{BOOLEAN}}
    }
}
```
***Payload Parameters***

|	Parameter							|	Type		|	必选	|	描述								|
|	:------------------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	playerId								|	string	|	Yes	|	标识								|
|	token								|	string	|	Yes	|	token							|
|	isTop									|	boolean	|	Yes	|	是否在顶层					|

### 短视频播放器上下文
```json
{
    "header": {
        "namespace": "TvsShortVideoPlayer",
        "name": "PlaybackState"
    },
    "payload": {
        "token": "{{STRING}}",
        "offsetInMilliseconds": {{LONG}},
        "playerActivity": "{{STRING}}",
        "isTop": {{BOOLEAN}}
    }
}
```
***Payload Parameters***

|	Parameter							|	Type		|	必选	|	描述							|
|	:------------------------------------	|	:--------	|	:-----	|	:---------------------------	|
|	playerActivity						|	string	|	Yes	|	播放器状态				|
|	token								|	string	|	Yes	|	token						|
|	offsetInMilliseconds			|	long		|	Yes	|	偏移量						|
|	isTop									|	boolean	|	Yes	|	是否在顶层				|

### 语音识别器上下文
```json
{
    "header": {
        "namespace": "SpeechRecognizer",
        "name": "RecognizerState"
    },
    "payload": {
		"wakeword": "{{STRING}}",
		"isNoWakeEnabled": {{BOOLEAN}}
    }
}
```

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	wakeword					|	string	|	Yes	|	唤醒词							|
|	isNoWakeEnabled		|	boolean	|	No	|	是否免唤醒开启				|

### 音频播放器上下文
```json
{
	"header": {
		"namespace":"AudioPlayer",
		"name":"PlaybackState"
	},
	"payload": {
		"token": "{{STRING}}",
		"playerActivity": "{{STRING}}",
		"tvsPlayerMode": "{{STRING}}",
		"offsetInMilliseconds": {{LONG}},
		"isTop": {{BOOLEAN}}
	}
}
```

***Payload Parameters***

|	Parameter							|	Type		|	必选	|	描述																|
|	:------------------------------------	|	:--------	|	:-----	|	:------------------------------------------------------------------	|
|	tvsPlayerMode					|	string	|	Yes	|	当前模式<br>Audio:音频(默认)<br>Video:视频	|
|	playerActivity						|	string	|	Yes	|	播放器状态													|
|	token								|	string	|	Yes	|	token															|
|	offsetInMilliseconds			|	long		|	Yes	|	偏移量															|
|	isTop									|	bool		|	Yes	|	是否在顶层													|

### UI上下文
```json
{
	"header": {
		"namespace": "TvsUserInterface",
		"name": "ShowState"
	},
	"payload": {
		"isEnabled": {{BOOLEAN}}
	}
}
```

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述								|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	isEnabled					|	boolean	|	Yes	|	是否开启UI					|

### 位置信息上下文
```json
{
	"header": {
		"namespace": "LocationInformation",
		"name": "LocationState"
	},
	"payload": {
		"latitude" : 30.0000,
		"longitude": 90.0000
	}
}
```

***Payload Paramters***

|	Parameter				|	Type		|	必选	|	描述				|
|	:-----------------------	|	:--------	|	:-----	|	:---------------	|
|	latitude					|	float		|	Yes	|	纬度				|
|	longitude				|	float		|	Yes	|	经度				|

### 情景模式上下文
```json
{
	"header": {
		"namespace": "TvsProfileInformation",
		"name": "ProfileState"
	},
	"payload": {
		"isChildModeEnabled": {{BOOLEAN}},
		"isLockModeEnabled": {{BOOLEAN}},
		"isPhoneModeEnabled": {{BOOLEAN}},
		"phoneState": "{{STRING}}"
	}
}
```

***Payload Paramters***

|	Parameter						|	Type		|	必选		|	描述					|
|	:---------------------------		|	:--------	|	:-----		|	:-------------------	|
|	isChildModeEnabled		|	boolean	|	No		|	是否儿童模式		|
|	isLockModeEnabled		|	boolean	|	No		|	是否锁定模式		|
|	isPhoneModeEnabled		|	boolean	|	No		|	是否电话模式		|
|	phoneState					|	string	|	No		|	电话状态:<br>CALL_COME<br>CALLING<br>CALL_IN	|

### 小程序控制上下文
```json
{
	"header": {
		"namespace": "AppletControl",
		"name": "AppletState"
	},
	"payload": {
		"id" : "{{STRING}}"
	}
}
```

***Payload Paramters***

|	Parameter				|	Type		|	必选	|	描述				|
|	:-----------------------	|	:--------	|	:-----	|	:---------------	|
|	id							|	string	|	Yes	|	小程序ID		|