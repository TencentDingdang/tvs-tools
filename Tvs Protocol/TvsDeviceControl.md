### 设置亮度指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "SetBrightness",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
            "brightness": {{LONG}}
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	brightness					|	long		|	Yes	|	亮度值[0~100]	|

### 调整亮度指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "AdjustBrightness",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
            "brightness": {{LONG}}
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述							|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------	|
|	brightness					|	long		|	Yes	|	亮度值[-100~+100]		|

### 亮度改变事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "BrightnessChanged",
            "messageId": "{{STRING}}"
		},
		"payload": {
            "brightness": {{LONG}}
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述						|
|	:---------------------------	|	:--------	|	:-----	|	:-------------------------	|
|	brightness					|	long		|	Yes	|	亮度值[0~100]		|

### 关闭摄像头指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "CloseCamera",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

### 打开摄像头指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "OpenCamera",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

### 摄像头改变事件
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "CameraChanged",
            "messageId": "{{STRING}}"
		},
		"payload": {
			"state": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	state							|	string	|	Yes	|	摄像头状态:<br>Open:打开<br>Closed:关闭			|

### 关闭麦克风指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "CloseMicrophone",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

### 打开麦克风指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "OpenMicrophone",
            "messageId": "{{STRING}}"
		},
		"payload": {
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|

### 麦克风改变事件
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "MicrophoneChanged",
            "messageId": "{{STRING}}"
		},
		"payload": {
			"state": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	state							|	string	|	Yes	|	麦克风状态:<br>Open:打开<br>Closed:关闭			|

### 关闭监视器指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "CloseMonitor",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {

		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	controlInfo					|	string	|	Yes	|	控制信息			|

### 打开监视器指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "OpenMonitor",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

### 监视器改变事件
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "MonitorChanged",
            "messageId": "{{STRING}}"
		},
		"payload": {
			"state": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	state							|	string	|	Yes	|	监视器状态:<br>Open:打开<br>Closed:关闭			|

### 关闭蓝牙指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "CloseBluetooth",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {

		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	controlInfo					|	string	|	Yes	|	控制信息			|
### 打开蓝牙指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "OpenBluetooth",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

### 蓝牙改变事件
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "BluetoothChanged",
            "messageId": "{{STRING}}"
		},
		"payload": {
			"state": "{{STRING}}"
		}
	}
}	
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	state							|	string	|	Yes	|	监视器状态:<br>Open:打开<br>Closed:关闭			|

### 关闭Wifi指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "CloseWifi",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {

		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	controlInfo					|	string	|	Yes	|	控制信息			|


### 改变页面指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "ChangePage",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"type": "{{STRING}}",
			"pageInfo": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	type							|	string	|	Yes	|	类型:<br>Back:返回<br>Exit:退出<br>BackToHome:返回首屏<br>OpenThis:打开当前对象<br>OpenPage:打开页面			|
|	pageInfo					|	string	|	Yes	|	页面信息			|

### 改变壁纸指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "ChangeWallPaper",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"wallPaperInfo": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	wallPaperInfo				|	string	|	Yes	|	壁纸信息			|

### 重启指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "Reboot",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"type": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述					|
|	:---------------------------	|	:--------	|	:-----	|	:--------------------	|
|	type							|	string	|	Yes	|	类型<br>INFORMATION:提示<br>EXECUTE:执行<br>CANCEL:取消			|

### 设置睡眠指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "SetSleep",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"token": "{{STRING}}",
			"beginDate": "{{STRING}}",
			"endDate": "{{STRING}}",
			"beginTime": "{{STRING}}",
			"endTime": "{{STRING}}",
			"type": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	token						|	string	|	Yes	|	token									|
|	beginDate					|	string	|	Yes	|	开始日期(UTC:20180810)		|
|	endDate					|	string	|	Yes	|	结束日期(UTC:20180830)		|
|	beginTime					|	string	|	Yes	|	开始时间(UTC:231010)			|
|	endTime					|	string	|	Yes	|	结束时间(UTC:071010)			|
|	type							|	string	|	Yes	|	类型<br>Once,一次<br>Daily,每天<br>Weekly,每周<br>Monthly,每月	|

### 设置睡眠成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "SetSleepSucceeded",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"token": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	token						|	string	|	Yes	|	token									|

### 设置睡眠失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "SetSleepFailed",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"token": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	token						|	string	|	Yes	|	token									|

### 取消睡眠指令
```json
{
	"directive": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "DeleteSleep",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"token": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	token						|	string	|	Yes	|	token									|

### 取消睡眠成功事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "DeleteSleepSucceeded",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"token": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	token						|	string	|	Yes	|	token									|

### 取消睡眠失败事件
```json
{
	"event": {
		"header": {
			"namespace": "TvsDeviceControl",
			"name": "DeleteSleepFailed",
            "messageId": "{{STRING}}",
			"dialogRequestId": "{{STRING}}"
		},
		"payload": {
			"token": "{{STRING}}"
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述							|
|	:-------------------	|	:--------	|	:-----	|	:-----------------------------	|
|	messageId			|	string	|	Yes	|	消息ID						|
|	dialogRequestId	|	string	|	No	|	对话ID						|

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	token						|	string	|	Yes	|	token									|