# `v1/uniAccess`文档



[TOC]

`v1/uniAccess`接口根据`payload.domain`和`payload.intent`提供不同的能力。`payload.jsonBlobInfo`为附加参数，一般为json结构的**string**形式。下面介绍`v1/uniAccess`所提供的能力，并说明各个能力下`payload.domain`、`payload.intent`、`payload.jsonBlobInfo`应怎么填写。如果不特殊说明，为了美观起见，`payload.jsonBlobInfo`参数本文将只给出json形式，实际请求的时候开发者必须将**json转换为string**填到`payload.jsonBlobInfo`。

# 1. 媒体ID换URL
## 1.1 说明

某些领域返回的媒体数据只有媒体ID（例如闹钟返回的闹铃信息）。如果想要播放该媒体，终端需要调用本接口换取媒体的URL才行。

## 1.2 参数


`payload.domain`: resource

`payload.intent`: get

`payload.jsonBlobInfo`:


```json
{
	"vectResourceID":[{
		"strID":"{{STRING}}"
	}]
}
```
***jsonBlobInfo Parameters***

| 参数名                    | 类型       | 是否必选 | 描述            |
| ---------------------- | -------- | ---- | ------------- |
| `vectResourceID`       | `list`   | Yes  | 需要换URL的媒体ID列表 |
| `vectResourceID.strID` | `string` | Yes  | 媒体ID          |

​	
## 1.3 返回jsonBlobInfo 参数

```json
{
	"vectResourceList": [{
		"lExpiresInSec": {{INT}},
		"lRefrainEnd": {{INT}},
		"lRefrainStart":{{INT}} ,
		"strResourceCoverURL": "{{STRING}}",
		"strResourceID": "{{STRING}}",
		"strResourceTitle": "{{STRING}}",
		"strResourceURL": "{{STRING}}",
		
	}]
}
```
***jsonBlobInfo Parameters***

| 参数名                                    | 类型       | 是否必选 | 描述                                   |
| -------------------------------------- | -------- | ---- | ------------------------------------ |
| `vectResourceList`                     | `list`   | Yes  | 结果列表                                 |
| `vectResourceList.strResourceURL`      | `string` | Yes  | 媒体URL                                |
| `vectResourceList.strResourceTitle`    | `string` | No   | 媒体标题                                 |
| `vectResourceList.strResourceID`       | `string` | Yes  | 媒体ID                                 |
| `vectResourceList.strResourceCoverURL` | `string` | No   | 媒体封面图                                |
| `vectResourceList.lRefrainStart`       | `int`    | No   | 开始时间偏移（ms），如果非0，那么需要媒体在这个偏移开始播放音频。   |
| `vectResourceList.lRefrainEnd`         | `int`    | No   | 结束时间偏移(ms)，如果非0，那么需要媒体需要在这个偏移结束播放音频。 |
| `vectResourceList.lExpiresInSec`       | `int`    | No   | 失效时间                                 |


## 1.4 payload示例

### 1.4.1 请求payload数据
```json
{
	"domain": "resource",
	"intent": "get",
	"jsonBlobInfo": "{\"vectResourceID\":[{\"strID\":\"music.play$9058085\"}]}"

}
```

### 1.4.2 返回payload数据

```json
{
		"jsonBlobInfo": "{ \"vectResourceList\": [ { \"lExpiresInSec\": 43200, \"lRefrainEnd\": 0, \"lRefrainStart\": 0, \"strCategory\": \"\",\"strResourceCoverURL\": \"http:\\/\\/y.gtimg.cn\\/music\\/photo_new\\/T002R500x500M000004CsAwT2P0qg9.jpg\", \"strResourceID\": \"music.play$9058085\", \"strResourceTitle\": \"妲己 - 葛雨晴\", \"strResourceURL\": \"http:\\/\\/isure.stream.qqmusic.qq.com\\/C400003eQCey2ZWFwu.m4a?guid=2000001810&vkey=A0E042094C3D15131B3143F111E9AD042D504434E0F33C50DAE42D9E2756153B733D3DBEB1000860DD53486DE20BC6A5151A949CBC67C530&uin=&fromtag=50\", \"vTags\": [  ] } ] }"
	}
```

# 2. 音乐硬件设备注册

## 2.1 说明

硬件设备需要先调用设备注册接口激活，才可正常访问音乐资源

## 2.2 参数


`payload.domain`: tskm_report

`payload.intent`: cloud_bind

`payload.jsonBlobInfo`:


```json
{
	"app_key":"{{STRING}}",
	"sn":"{{STRING}}"
}
```
***jsonBlobInfo Parameters***

| 参数名 | 类型 | 是否必选 | 描述            |
| ----- | -------- | ---- | ------------- |
| `app_key ` | `string` | Yes  | 开放平台分配的端标识 |
| `sn ` | `string` | Yes | 设备唯一序列号 |

## 2.3 返回jsonBlobInfo 参数

```json
{
  "eRet": {{INT}},
  "strMsg": "{{STRING}}"
}
```
***jsonBlobInfo Parameters***

| 参数名                                    | 类型       | 是否必选 | 描述                                   |
| -------------------------------------- | -------- | ---- | ------------------------------------ |
| `eRet` | `int` | YES | 0：成功 |
| `strMsg` | `int` | YES | 提示语 |


## 2.4 payload示例

### 2.4.1 请求payload数据
```json
{
	"domain": "tskm_report",
	"intent": "cloud_bind",
	"jsonBlobInfo": "{\"app_key\":\"{{STRING}}\",\"sn\":\"{{STRING}}\"}"

}
```

### 2.4.2 返回payload数据

```json
{
	"jsonBlobInfo": "{ \"eRet\": 1, \"strMsg\": \"QQMusic device has been registered\"}"
}
```

# 3. 设备闹钟数据同步

## 3.1 说明

硬件设备需要同步闹钟全量数据时，可以通过该接口拉取

## 3.2 参数


`payload.domain`: `alarm`

`payload.intent`: `sync_data`

`payload.jsonBlobInfo`:


```json
{}
```

## 3.3 返回jsonBlobInfo 参数

参见 https://github.com/TencentDingdang/tvs-tools/blob/master/Tsk%20Protocol/domains_V3/custom_made_domain/alarm.md

## 3.4 payload示例

### 3.4.1 请求payload数据
```json
{
	"domain": "alarm",
	"intent": "sync_data",
	"jsonBlobInfo": "{}"
}
```

### 3.4.2 返回payload数据

参见 https://github.com/TencentDingdang/tvs-tools/blob/master/Tsk%20Protocol/domains_V3/custom_made_domain/alarm.md


# 4. 设备闹钟数据同步

## 4.1 说明

硬件设备需要同步闹钟全量数据时，可以通过该接口拉取

## 4.2 参数


`payload.domain`: `reminder_v2`

`payload.intent`: `sync_data`

`payload.jsonBlobInfo`:


```json
{}
```

## 4.3 返回jsonBlobInfo 参数

参见 https://github.com/TencentDingdang/tvs-tools/blob/master/Tsk%20Protocol/domains_V3/custom_made_domain/reminder_v2.md

## 4.4 payload示例

### 4.4.1 请求payload数据
```json
{
	"domain": "reminder_v2",
	"intent": "sync_data",
	"jsonBlobInfo": "{}"
}
```

### 4.4.2 返回payload数据

参见 https://github.com/TencentDingdang/tvs-tools/blob/master/Tsk%20Protocol/domains_V3/custom_made_domain/reminder_v2.md



