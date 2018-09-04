# `v1/uniAccess`文档



[TOC]
`v1/uniAccess`接口根据`payload.domain`和`payload.intent`提供不同的能力。`payload.jsonBlobInfo`为附加参数，一般为json结构的**string**形式。下面介绍`v1/uniAccess`所提供的能力，并说明各个能力下`payload.domain`、`payload.intent`、`payload.jsonBlobInfo`应怎么填写。如果不特殊说明，为了美观起见，`payload.jsonBlobInfo`参数本文将只给出json形式，实际请求的时候开发者必须将**json转换为string**填到`payload.jsonBlobInfo`。

# 1. 媒体ID换URL
## 1.1 参数


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
## 1.2 返回jsonBlobInfo 参数

```json
{
	"vectResourceList": [{
		"lExpiresInSec": 43200,
		"lRefrainEnd": 0,
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


## 1.3 payload示例

### 1.3.1 请求payload数据
```json
{
	"domain": "resource",
	"intent": "get",
	"jsonBlobInfo": "{\"vectResourceID\":[{\"strID\":\"music.play$9058085\"}]}"

}
```

### 1.3.2 返回payload数据

```json
{
		"jsonBlobInfo": "{ \"vectResourceList\": [ { \"lExpiresInSec\": 43200, \"lRefrainEnd\": 0, \"lRefrainStart\": 0, \"strCategory\": \"\",\"strResourceCoverURL\": \"http:\\/\\/y.gtimg.cn\\/music\\/photo_new\\/T002R500x500M000004CsAwT2P0qg9.jpg\", \"strResourceID\": \"music.play$9058085\", \"strResourceTitle\": \"妲己 - 葛雨晴\", \"strResourceURL\": \"http:\\/\\/isure.stream.qqmusic.qq.com\\/C400003eQCey2ZWFwu.m4a?guid=2000001810&vkey=A0E042094C3D15131B3143F111E9AD042D504434E0F33C50DAE42D9E2756153B733D3DBEB1000860DD53486DE20BC6A5151A949CBC67C530&uin=&fromtag=50\", \"vTags\": [  ] } ] }"
	}
```



