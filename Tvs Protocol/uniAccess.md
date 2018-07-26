## 统一接入接口
### ##接口描述

*统一接入接口*

### ##接口URL

https://aiwx.html5.qq.com/api/v1/uniAccess

### ##	请求方法

*POST*

### ##请求参数

```
json
{
    "header": {
        "user": {
            "authorization": "{{STRING}}"
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8",
        "device": {
            "network": "4G"
        },
		"profile":{
			"isChildModeEnabled" : {{BOOLEAN}},
			"isPhoneModeEnabled" : {{BOOLEAN}}
		}
    },
    "payload": {
      	"domain": "{{STRING}}",
		"intent": "{{STRING}}",
        "jsonBlobInfo": "{{STRING}}"
    }
}
```

***Header Parameters***

| 参数名                          					| 类型		| 是否必选 | 描述                                  		|
| :--------------------------------------------------	| :------------	| :------------	| :--------------------------------------------	|
| header                     						| object		| Yes			| -                                   			|
| header.user                						| object		| Yes			| 用户信息                               	|
| header.user.authorization  					| string		| Yes			| 用户访问认证信息						|
| header.ip                  						| string 		| No 			| 终端IP										|
| header.device                  					| object 		| No 			| 终端其他信息							|
| header.device.network           			| string 		| No 			| 终端网络类型							|
| header.profile           							| object 		| No 			| 情景模式									|
| header.profile.isChildModeEnabled		| boolean	| No 			| 是否儿童模式							|
| header.profile.isPhoneModeEnabled	| boolean	| No 			| 是否电话模式							|

***Payload Parameters***

| 参数名                          			| 类型		| 是否必选 | 描述                                  		|
| :------------------------------------------	| :------------	| :------------	| :--------------------------------------------	|
| payload                    				| object		| Yes			| 负载			 							|
| payload.domain                 		| string   	| Yes			| 领域			 							|
| payload.intent                 			| string    	| Yes			| 意图			 							|
| payload.jsonBlobInfo             	| string		| Yes			| 数据			 							|

### ##返回参数
```
json
{
	"header": {
   		"retCode": 0,
   		"errMsg": "{{STRING}}"
	},
	"payload": {
        "jsonBlobInfo": "{{STRING}}"
	}
}
```

***Header Parameters***

| 参数名                          			| 类型		| 是否必选 | 描述                                  		|
| :------------------------------------------	| :------------	| :------------	| :--------------------------------------------	|
| header                     				| object		| Yes			| 头部                                   		|
| header.retCode                			| long    	 	| Yes			| 返回码                               		|
| header.errMsg  						| string    	| Yes			| 错误消息									|

***Payload Parameters***

| 参数名                          			| 类型		| 是否必选 | 描述                                  		|
| :------------------------------------------	| :------------	| :------------	| :--------------------------------------------	|
| payload                    				| object		| Yes			| 负载			 							|
| payload.jsonBlobInfo             	| string		| Yes			| 数据			 							|