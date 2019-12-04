### 上下文
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
		},
		"activeApplication": {
			"id": "{{STRING}}",
			"version": "{{STRING}}",
			"activity": "{{STRING}}"
		},
		"allApplications": [
			{
				"id": "{{STRING}}",
				"version": "{{STRING}}"
			},
			{
				"id": "{{STRING}}",
				"version": "{{STRING}}"
			}
		]
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
|   activeApplication              	|   object 	|    No 	|    活跃应用             			|
|   activeApplication.id            	|   string 	|    No   	|    应用ID                         	|
|   activeApplication.version    	|   string 	|    No   	|    应用版本                      	|
|   activeApplication.activity     |   string  	|    No 	|    应用状态		             	|
|   allApplications              		|   array  	|    No 	|    所有应用             			|
|   allApplications[].id         		|   string  	|    No 	|    应用ID	             			|
|   allApplications[].version  		|   string  	|    No 	|    应用版本             			|

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    brightness                    |    long        |    Yes    |    亮度值[0~100]    |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    brightness                    |    long        |    Yes    |    亮度值[-100~+100]        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                        |
|    :---------------------------    |    :--------    |    :-----    |    :-------------------------    |
|    brightness                    |    long        |    Yes    |    亮度值[0~100]        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    state                            |    string    |    Yes    |    摄像头状态:<br>Open:打开<br>Closed:关闭            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    state                            |    string    |    Yes    |    麦克风状态:<br>Open:打开<br>Closed:关闭            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    controlInfo                    |    string    |    Yes    |    控制信息            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    state                            |    string    |    Yes    |    监视器状态:<br>Open:打开<br>Closed:关闭            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    controlInfo                    |    string    |    Yes    |    控制信息            |
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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    state                            |    string    |    Yes    |    监视器状态:<br>Open:打开<br>Closed:关闭            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    controlInfo                    |    string    |    Yes    |    控制信息            |


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
            "type": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    type                            |    string    |    Yes    |    类型:<br>Back:返回<br>Exit:退出<br>BackToHome:返回首屏<br>OpenThis:打开当前对象           |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    wallPaperInfo                |    string    |    Yes    |    壁纸信息            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                    |
|    :---------------------------    |    :--------    |    :-----    |    :--------------------    |
|    type                            |    string    |    Yes    |    类型<br>INFORMATION:提示<br>EXECUTE:执行<br>CANCEL:取消            |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |
|    beginDate                    |    string    |    Yes    |    开始日期(UTC:20180810)        |
|    endDate                    |    string    |    Yes    |    结束日期(UTC:20180830)        |
|    beginTime                    |    string    |    Yes    |    开始时间(UTC:231010)            |
|    endTime                    |    string    |    Yes    |    结束时间(UTC:071010)            |
|    type                            |    string    |    Yes    |    类型<br>Once,一次<br>Daily,每天<br>Weekly,每周<br>Monthly,每月    |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 取消睡眠成功事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "DeleteSleepSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 取消睡眠失败事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "DeleteSleepFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 设置定时时间指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "SetFixedTime",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "timeInMilliseconds": LONG,
			"dataType": "{{STRING}}",
            "action": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    timeInMilliseconds        |    long        |    Yes    |    时长                |
|    dataType                        |    string    |    Yes    |    数据类型<br>ANY,任意类型;<br>CURRENT,当前类型;<br>CURRENT_MEDIA,当前媒体;<br>XXX,指定类型;               |
|    action                        |    string    |    Yes    |    动作<br>PAUSE,暂停                |
|    token                        |    string    |    Yes    |    token                                    |

### 设置定时时间成功事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "SetFixedTimeSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 设置定时时间失败事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "SetFixedTimeFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
			"error": {
				"type": "{{STRING}}",
				"message": "{{STRING}}"
			}
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter               		|    Type  	|    必选	|    描述                                 	|
|    :--------------------------------  	|    :-------- 	|    :-----	|    :---------------------------------------  	|
|    token                        	|    string 	|    Yes 	|    token                                  	|
|    error                        		|    object 	|    Yes 	|    error information                   	|
|    error.type                 		|    string 	|    Yes 	|    error type			                   	|
|    error.message          		|    string 	|    Yes 	|    error message                   	|

***Error Types***

|    Value		               		|    Description  							|
|    :--------------------------------  	|    :----------------------------------------- 	|
|    NO_MEDIA                  	|    no media 								|
|    MEDIA_NOT_PLAYING	|    media is not playing 				|
|    NOT_SUPPORTED   		|    not support						 	|
|    UNKNOWN_ERROR  	|    unknown error					 	|

### 清除定时时间指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ClearFixedTime",
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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 清除定时时间成功事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ClearFixedTimeSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
			"token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 清除定时时间失败事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ClearFixedTimeFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
			"token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 设置屏幕保护指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "SetScreenSaver",
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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 设置屏幕保护成功事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "SetScreenSaverSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 设置屏幕保护失败事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "SetScreenSaverFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 取消屏幕保护指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "DeleteScreenSaver",
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

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 取消屏幕保护成功事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "DeleteScreenSaverSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 取消屏幕保护失败事件
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "DeleteScreenSaverFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    token                        |    string    |    Yes    |    token                                    |

### 打开URI指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "OpenUri",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
			"type": "{{STRING}}",
			"uri": "{{STRING}}",
			"version": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                                        |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------------------    |
|    type                        |    string    |    Yes    |    类型:<br>URL,普通URL;<br>AndroidActivity,Android APP Activity;<br>AndroidBroadcast,Android APP Broadcast                                    |
|    uri                       	|    string    |    Yes  	|    URI                                    |
|    version                 	|    string    |    No    	|    版本信息                                    |

### 第三方APP播控(播放)
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationPlay",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
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
|    dialogRequestId    |    string    |    No    |    对话ID                        |

### 第三方APP播控(播放成功事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationPlaySucceeded",
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

### 第三方APP播控(播放失败事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationPlayFailed",
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

### 第三方APP播控(停止)
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationStop",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
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
|    dialogRequestId    |    string    |    No    |    对话ID                        |

### 第三方APP播控(停止成功事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationStopSucceeded",
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

### 第三方APP播控(停止失败事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationStopFailed",
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

### 第三方APP播控(下一个)
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationNext",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
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
|    dialogRequestId    |    string    |    No    |    对话ID                        |

### 第三方APP播控(下一个成功事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationNextSucceeded",
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

### 第三方APP播控(下一个失败事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationNextFailed",
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

### 第三方APP播控(上一个)
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationPrevious",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
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
|    dialogRequestId    |    string    |    No    |    对话ID                        |

### 第三方APP播控(上一个成功事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationPreviousSucceeded",
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

### 第三方APP播控(上一个失败事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationPreviousFailed",
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

### 第三方APP播控(改变播放模式)
```json
{
    "directive": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationChangePlaybackMode",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
			"mode": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |
|    dialogRequestId    |    string    |    No    |    对话ID                        |

***Payload Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    mode            |    string    |    Yes    |    播放模式<br>SingleMode:单曲<br>SingleCycleMode:单曲循环<br>ListMode:列表<br>ListCycleMode:列表循环<br>RandomMode:随机                        |

### 第三方APP播控(改变播放模式成功事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationChangePlaybackModeSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
			"mode": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    mode            |    string    |    Yes    |    播放模式<br>SingleMode:单曲<br>SingleCycleMode:单曲循环<br>ListMode:列表<br>ListCycleMode:列表循环<br>RandomMode:随机                        |

### 第三方APP播控(改变播放模式失败事件)
```json
{
    "event": {
        "header": {
            "namespace": "TvsDeviceControl",
            "name": "ApplicationChangePlaybackModeFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
			"mode": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                        |

***Payload Paramters***

|    Parameter            |    Type        |    必选    |    描述                            |
|    :-------------------    |    :--------    |    :-----    |    :-----------------------------    |
|    mode            |    string    |    Yes    |    播放模式<br>SingleMode:单曲<br>SingleCycleMode:单曲循环<br>ListMode:列表<br>ListCycleMode:列表循环<br>RandomMode:随机                        |