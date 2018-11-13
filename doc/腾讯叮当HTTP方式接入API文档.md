# 腾讯叮当HTTP接入API V1.15



[TOC]

## 1 简介

本文档主要针对API开发者，描述腾讯叮当云端API语音识别、语义理解、TTS接口服务的相关技术内容。如果您对文档内容有任何疑问，可以通过以下方式联系我们：

- 发送邮件至allenwwang##tencent.com;kangrong##tencent.com;。 替换##为@。

  ​

## 2 API接口能力

| 接口名称      | 能力                       |
| --------- | ------------------------ |
| 语义理解+服务接口 | 提供文本转语义结构，并返回服务数据的能力。    |
| 语音识别接口    | 提供流式/非流式语音识别能力。          |
| TTS接口     | 提供语音合成的能力。               |
| 终端状态上报接口  | 上报终端状态，有助于后台提供更精准的语义服务结果 |


## 3 协议支持

​	接口为HTTP形式，建议使用HTTPS保持长连接，以减少访问耗时、提升用户体验。


## 4 请求格式

POST方式调用。并在Http协议头中，设置`Content-Type`为`application/json; charset=UTF-8`。

**注意**：要求使用JSON格式的结构体来描述一个请求的具体内容。发送时默认需要对body整体进行UTF-8编码



## 5 返回格式

JSON格式，返回内容为UTF-8编码



## 6 HTTP Header要求

腾讯叮当API对于HTTP请求的请求头字段有如下要求：

| Header Name   | 是否必须 | 说明                                       |
| ------------- | ---- | ---------------------------------------- |
| Authorization | 必须   | 该请求头将用于访问权限的验证。请求不带该字段或者签名验证错误的，将会被拒绝访问。`Authorization`包含了签名算法类型、时间戳、签名信息等，比如`CredentialKey`、`Signature`等。关于签名的具体方法，请查阅[签名方法](#_1)。 |
| Content-Type  | 可选   | 当请求方法为`PATCH`、`PUT`或`POST`时，指定`Content-Type: application/json; charset=UTF-8`。 |


### 6.1 签名方法

腾讯叮当API要求所有的请求都要经过签名，以证明请求是经过授权的。请求通过Hash算法进行加密计算，得到一个请求对应的签名字符串，并将该签名字符串带到`Authorization`请求头中。腾讯叮当API会对该签名进行校验，对于未带上正确签名的请求将视为未授权的请求并拒绝访问。

腾讯叮当API支持使用[TVS-HMAC-SHA256-BASIC](#TVS-HMAC-SHA256-BASIC签名方法)进行消息签名。

#### 6.1.1 TVS-HMAC-SHA256-BASIC签名方法

#### 6.1.2 Task 1: 拼接请求数据和时间戳得到`SigningContent`
请求数据指的是HTTP Body数据，时间戳取当前的UTC时间，并以ISO8601格式为标准（'YYYYMMDD'T'HHMMSS'Z）。假设当前时间戳为20170701T235959Z，以示例1的请求为例，得到的`SigningContent`为：
```text
{
    "query": "今天的天气怎样",
    "guid": "1f6befd9f24f332babec26d1106088ce",
    "qua": "QV=3&PL=ADR&PR=your_product_name&VE=GA&VN=0.1.0.1000&PP=com.your_product.packagename&DE=TV&CHID=app_channel_id",
    ...
}20170701T235959Z
```

#### 6.1.3 Task 2: 获取`Signature`签名
腾讯叮当API要求使用平台分配的`BotSecret`作为签名的密钥，`BotSecret`应该存放在请求方的服务器中，不应该以任何形式暴露给终端。签名使用的算法是`HMAC-SHA256`：
```
Signature = HMAC_SHA256(SigningContent, BotSecret);
```

需要注意的是，在执行hmac时用的是sha256哈希之后的16进制数据，而不是二进制数据，`Signature`同样是hmac之后的16进制数据。

以下为签名算法的伪代码：
```
SigningContent = "This is signing-content";
BotSeret = "bot_secret";
Signature = HMAC_SHA256(SigningContent, BotSecret);
print Signature;

/// output
cc7d8a8210bace445f7f67c862fac6ad33e99feda0f16a45fe6bbcda295388f4
```
文档后面给出了具体的签名的具体实现Demo和请求方式，详见[TVS-HMAC-SHA256-BASIC签名示例](#tvs-hmac-sha256-basic_1)

#### 6.1.4 Task 3: 在请求中带上签名信息
计算得到请求内容的签名之后，需要在HTTP Header的`Authorization`中带上签名信息。`Authorization`的结构如下伪代码所示：

```http
Authorization: [Algorithm] CredentialKey=[BotKey], Datetime=[Timestamp], Signature=[Signature]
```

以下Demo展示了一个完整的`Authorization`：
```http
Authorization: TVS-HMAC-SHA256-BASIC CredentialKey = 39ba87a1-2we3-4345-8d26-e632646e54b1, Datetime=20170720T193559Z, Signature=d8612ab1ff0301e1016d817c02350a2b76ea62e0
```



## 7 API接口文档

### 7.1 语义请求接口

#### 7.1.1 接口描述
​	该接口为语义理解、服务接口，语义理解能够分析出文本中的领域、意图、语义结构。服务接口可以根据语义理解结果返回相应的服务数据。例如“我想听周杰伦的歌”，语义理解的领域为song，意图为play，歌手名为周杰伦。服务接口根据语义理解结果，返回周杰伦的歌单。

该接口按request_type的不同提供三种功能：

| payload.request_type | 说明                                       |
| -------------------- | ---------------------------------------- |
| SEMANTIC_SERVICE     | 默认，返回语义、服务结果                             |
| SEMANTIC_ONLY        | 仅返回语义理解结果。                               |
| SERVICE_ONLY         | 仅返回服务结果，但是需要payload.session.session_id填上语义理解的sessionId。 |


#### 7.1.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/v1/richanswer`

body请求示例

```json
{
    "header": {
        "guid": "【设备唯一标识】",
        "qua": "【设备QUA】",
        "user": {
            "user_id": "",
	    "account":{
	    	"id":"{{STRING}}",
                "appid":"{{STRING}}",
                "type":"{{STRING}}",
                "token":"{{STRING}}"	
	    }
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8",
        "device": {
            "network": "4G",
            "serial_num":"{{STRING}}"
        }
    },
    "payload": {
        "session": {
            "session_id": "..."
        },
        "query": "我想听刘德华的歌",
        "request_type": "SEMANTIC_SERVICE",
        "semantic":{
			"domain":"...",
			"intent":"...",
			"param":[
				{
					"type":"...",
					"key":"...",
					"value":"..."
				},
				{
					"type":"...",
					"key":"...",
					"value":"..."
				}
		    ]
		},
		"extra_data":[			
			{
				"type":"IMAGE",
				"data_base64":"..."
			},
			{
				"type":"AUDIO",
				"data_base64":"..."
			},
			{
				"type":"VIDEO",
				"data_base64":"..."
			}
		]
    }
}
```

| 参数名                               |    类型    | 是否必选 | 描述                                       |
| --------------------------------- | :------: | :--: | ---------------------------------------- |
| `header`                          |    -     |  是   | 请求头                                      |
| `header.guid`                     | `string` |  是   | 设备唯一标志码。详细说明见[附录-GUID获取](#GUID获取)        |
| `header.qua`                      | `string` |  是   | 设备及应用信息，详细说明见[附录-QUA字段说明](#QUA字段说明)      |
| `header.user`                     |    -     |  否   | 用户信息                                     |
| `header.user.user_id`             | `string` |  -   | 用户ID，，详细说明见[附录-USERID](#USERID)          |
| `header.user.account`             | `object` |  -   | 用户账户信息                                   |
| `header.user.account.id`          | `string` |  -   | 用户账户ID，填openid                           |
| `header.user.account.token`       | `string` |  -   | 用户账户accesstoken                          |
| `header.user.account.type`        | `string` |  -   | 用户账户类型,支持`WX`/`QQOPEN`                   |
| `header.user.account.appid`       | `string` |  -   | 用户账户的appid                               |
| `header.lbs`                      |    -     |  否   | 用户位置信息                                   |
| `header.lbs.longitude`            | `double` |  -   | 经度                                       |
| `header.lbs.latitude`             | `double` |  -   | 纬度                                       |
| `header.ip`                       | `string` |  是   | 终端IP                                     |
| `header.device`                   |    -     |  否   |                                          |
| `header.device.network`           | `string` |  否   | 网络类型：`4G`/`3G`/`2G`/`Wi-Fi`              |
| `header.device.serial_num`        | `string` |  否   | 设备唯一序列号                                  |
| `payload`                         |    -     |  是   | 请求内容                                     |
| `payload.query`                   | `string` |  是   | 用户query                                  |
| `payload.request_type`            | `string` |  否   | 请求类型：<br>`SEMANTIC_SERVICE`：默认，返回语义、服务结果；<br>`SEMANTIC_ONLY`：只需要语义结果<br>`SERVICE_ONLY`：只需要服务结果，需带上`session_id`； |
| `payload.semantic`                |    -     |  否   | 语义信息，若带上，则请求不经过NLP                       |
| `payload.semantic.domain`         | `string` |  否   | 领域信息                                     |
| `payload.semantic.intent`         | `string` |  否   | 意图信息                                     |
| `payload.semantic.param`          |    -     |  否   | 语义参数信息                                   |
| `payload.semantic.param{type}`    | `string` |  否   | 语义参数类型                                   |
| `payload.semantic.param{key}`     | `string` |  否   | 语义参数名字                                   |
| `payload.semantic.param{value}`   | `string` |  否   | 语义参数值                                    |
| `payload.extra_data`              |    -     |  否   | 额外数据信息                                   |
| `payload.extra_data{type}`        |    -     |  否   | 额外数据类型：<br>`IMAGE`：图片；<br>`AUDIO`：语音；<br>`VIDEO`：视频； |
| `payload.extra_data{data_base64}` | `string` |  否   | 额外数据`Base64`编码                           |


#### 7.1.3 返回参数

```json
{
    "header": {
        "semantic": {
			"code":0,
			"msg":"",
            "domain": "...",
            "intent": "...",
            "session_complete": true
        }
    },
    "payload": {
        "response_text": "深圳市今天天气.....",
        "data": {
            "json": {
                ...
            },
            "json_template":{
                ...
			}
        }
    }
}
```

| 参数名                                | 类型       | 描述                                       |
| ---------------------------------- | -------- | ---------------------------------------- |
| `header`                           | -        | 消息头                                      |
| `header.semantic`                  | -        | 语义信息                                     |
| `header.semantic.code`             | `string` | 语义错误码(0,正常;非0,异常;)                       |
| `header.semantic.msg`              | `string` | 语义错误消息                                   |
| `header.semantic.domain`           | `string` | 领域                                       |
| `header.semantic.intent`           | `string` | 意图                                       |
| `header.semantic.session_complete` | `bool`   | 会话是否结束                                   |
| `header.session`                   | -        | 会话                                       |
| `header.session.session_id`        | `string` | 会话ID                                     |
| `payload`                          | -        | 消息体                                      |
| `payload.response_text`            | `string` | 显示正文内容                                   |
| `payload.data`                     | -        | 领域数据                                     |
| `payload.data.json`                | -        | 领域结构化Json数据，数据格式详见https://github.com/TencentDingdang/tvs-tools/tree/master/doc/domains， 对于采用V3协议的端，见https://github.com/TencentDingdang/tvs-tools/tree/master/Tsk%20Protocol |
| `payload.data.json_template`       | -        | 领域模版Json数据，数据格式详见"腾讯叮当模板文档"              |

示例代码见1:	../evaluate/script/richanswerV1.py(不带附加数据)
示例代码见2:	../evaluate/script/richanswer_extV1.py(带附加数据)



### 7.2. 语音识别接口

#### 7.2.1 接口描述

该接口提供(非)流式语音识别的能力。语音识别按是否采用云端VAD分为两种情况：

| 类型    | 说明                                       |
| ----- | ---------------------------------------- |
| 云端VAD | 当payload.open_vad=true时，语音识别引擎将会自动识别用户说话结束。自动返回最终识别结果。适用于音箱收音等非手动控制结束的场景 |
| 本地VAD | 当payload.open_vad=false时，语音识别引擎不会自动识别用户说话结束。需要终端主动设置结束标识(voice_finished=true)，语音识别引擎才会返回最终识别结果。适用于**按下说话,抬起结束**的收音场景，如遥控器。 |

#### 7.2.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/asr`

```json
{
    "header": {
        "guid": "9f533c717354fd6b2b95ee5111ba88cb",
        "qua": "QV=3&PL=ADR&PR=your_product_name&VE=GA&VN=0.1.0.1000&PP=com.your_product.packagename&DE=TV&CHID=app_channel_id",
        "user": {
            "user_id": ""
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8",
        "device": {
            "network": "4G"
        }
    },
    "payload": {
        "voice_meta": {
            "compress": "PCM",
            "sample_rate": "8K",
            "channel": 1,
			"language": ENGLISH,
			"offset":0
        },
      	"open_vad": true,
        "session_id": "...",
        "index": 0,
        "voice_finished": false,
        "voice_base64": "..."
    }
}
```

| 参数名                              |    类型    | 是否必选 | 描述                                       |
| -------------------------------- | :------: | :--: | ---------------------------------------- |
| `header`                         |    -     |  是   | 请求头                                      |
| `header.guid`                    | `string` |  是   | 设备唯一标志码。详细说明见[附录-GUID获取](#GUID获取)        |
| `header.qua`                     | `string` |  是   | 设备及应用信息，详细说明见[附录-QUA字段说明](#QUA字段说明)      |
| `header.user`                    |    -     |  否   | 用户信息                                     |
| `header.user.user_id`            | `string` |  -   | 用户ID，，详细说明见[附录-USERID](#USERID)          |
| `header.lbs`                     |    -     |  否   | 用户位置信息                                   |
| `header.lbs.longitude`           | `double` |  -   | 经度                                       |
| `header.lbs.latitude`            | `double` |  -   | 纬度                                       |
| `header.ip`                      | `string` |  是   | 终端IP                                     |
| `header.device`                  |    -     |  否   |                                          |
| `header.device.network`          | `string` |  否   | 网络类型：`4G`/`3G`/`2G`/`Wi-Fi`              |
| `payload`                        |    -     |  是   | 请求内容                                     |
| `payload.voice_meta`             |    -     |  是   | 语音配置信息                                   |
| `payload.voice_meta.compress`    | `string` |  是   | 压缩类型：`PCM`/`WAV`/`SPEEX`/`AMR`/`OPUS`/`MP3` |
| `payload.voice_meta.sample_rate` | `string` |  是   | 采样率：`8K`/`16K`                           |
| `payload.voice_meta.channel`     |  `int`   |  是   | 音频通道数：`1`/`2`                            |
| `payload.voice_meta.language`     |  `string`   |  否   | 语言类型(默认汉语)<br>ENGLISH:英语                            |
| `payload.voice_meta.offset`     |  `int`   |  否   | 语音片偏移量                            |
| `payload.open_vad`               |  `bool`  |  是   | 是否打开VAD                                  |
| `payload.session_id`             | `string` |  否   | 流式识别过程中必填                                |
| `payload.index`                  |  `int`   |  是   | 语音片偏移量(英文时为语音包序号)                                   |
| `payload.voice_finished`         |  `bool`  |  是   | 语音是否结束                                   |
| `payload.voice_base64`           | `string` |  是   | 语音数据的`Base64`编码                          |


#### 7.2.3 返回参数

```json
{
    "header": {
        "session": {
            "session_id": "..."
        }
    },
    "payload": {
        "final_result": false,
        "result": "深圳市今天天气"
    }
}
```

| 参数名                         | 类型       | 描述     |
| --------------------------- | -------- | ------ |
| `header`                    | -        | 消息头    |
| `header.session`            | -        | 会话     |
| `header.session.session_id` | `string` | 会话ID   |
| `payload`                   | -        | 消息体    |
| `payload.final_result`      | `bool`   | 是否最终结果 |
| `payload.result`            | `string` | 语音识别结果 |


### 7.3 语音合成接口
#### 7.3.1 接口描述
(非)流式文本转换为语音。

| 类型   | 说明                                       |
| ---- | ---------------------------------------- |
| 流式合成 | 当payload.single_request=false时，TTS引擎将会分多次返回语音合成结果，最终结果是多次数据的拼接。优点是终端可以迅速收到TTS部分回包，进行TTS播放，体验较好。缺点是终端代码逻辑复杂。 |
| 一次合成 | 当payload.single_request=true时，TTS引擎将语音合成结果一次性返回。 优点是终端代码逻辑简单，缺点是合成速度较慢 |


#### 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/tts`

```json
{
    "header": {
        "guid": "9f533c717354fd6b2b95ee5111ba88cb",
        "qua": "QV=3&PL=ADR&PR=your_product_name&VE=GA&VN=0.1.0.1000&PP=com.your_product.packagename&DE=TV&CHID=app_channel_id",
        "user": {
            "user_id": ""
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8",
        "device": {
            "network": "4G"
        }
    },
    "payload": {
        "speech_meta": {
            "compress": "MP3",
            "person": "LIBAI",
            "volume": 50,
            "speed": 50,
            "pitch": 50
        },
        "session_id": "...",
        "index": 0,
        "single_request": false,
        "content": {
            "text": "..."
        }
    }
}
```

| 参数名                            |    类型    | 是否必选 | 描述                                       |
| ------------------------------ | :------: | :--: | ---------------------------------------- |
| `header`                       |    -     |  是   | 请求头                                      |
| `header.guid`                  | `string` |  是   | 设备唯一标志码。详细说明见[附录-GUID获取](#GUID获取)        |
| `header.qua`                   | `string` |  是   | 设备及应用信息，详细说明见[附录-QUA字段说明](#QUA字段说明)      |
| `header.user`                  |    -     |  否   | 用户信息                                     |
| `header.user.user_id`          | `string` |  -   | 用户ID，，详细说明见[附录-USERID](#USERID)          |
| `header.lbs`                   |    -     |  否   | 用户位置信息                                   |
| `header.lbs.longitude`         | `double` |  -   | 经度                                       |
| `header.lbs.latitude`          | `double` |  -   | 纬度                                       |
| `header.ip`                    | `string` |  是   | 终端IP                                     |
| `header.device`                |    -     |  否   |                                          |
| `header.device.network`        | `string` |  否   | 网络类型：`4G`/`3G`/`2G`/`Wi-Fi`              |
| `payload`                      |    -     |  是   | 请求内容                                     |
| `payload.speech_meta`          |    -     |  是   | 语音配置信息                                   |
| `payload.speech_meta.compress` | `string` |  是   | 压缩类型：`WAV`/`MP3`/`AMR`                   |
| `payload.speech_meta.person`   | `string` |  否   | 发音人：`ZHOULONGFEI`/`CHENANQI`/`YEZI`/`YEWAN`/`DAJI`/`LIBAI`/`NAZHA`/`MUZHA`/`WY` |
| `payload.speech_meta.volume`   |  `int`   |  否   | 音量：0~100（默认50）                           |
| `payload.speech_meta.speed`    |  `int`   |  否   | 语速：0~100（默认50）                           |
| `payload.speech_meta.pitch`    |  `int`   |  否   | 声调：0~100（默认50）                           |
| `payload.session_id`           | `string` |  否   | 流式TTS过程中必填                               |
| `payload.index`                |  `int`   |  是   | 请求的语音片序号                                 |
| `payload.single_request`       |  `bool`  |  是   | 是否一次合成：<br>`true`：一次合成；<br>`false`：流式合成； |
| `payload.content`              |    -     |  是   | TTS内容                                    |
| `payload.content.text`         | `string` |  是   | 转语音的文本内容                                 |


#### 7.3.2 返回参数

```json
{
    "header": {
        "session": {
            "session_id": "..."
        }
    },
    "payload": {
        "speech_finished": false,
        "speech_base64": "..."
    }
}
```

| 参数名                         | 类型       | 描述          |
| --------------------------- | -------- | ----------- |
| `header`                    | -        | 消息头         |
| `header.session`            | -        | 会话          |
| `header.session.session_id` | `string` | 会话ID        |
| `payload`                   | -        | 消息体         |
| `payload.speech_finished`   | `bool`   | 是否结束        |
| `payload.speech_base64`     | `string` | 语音的Base64数据 |

### 7.4 终端上报接口
#### 7.4.1 接口描述
​	为了给用户提供更多个性化的内容，保证更优的体验。终端可以通过上报接口向腾讯叮当上报终端的阅读、播放等状态。
#### 7.4.2 请求参数
__URL__：`POST https://aiwx.html5.qq.com/api/v1/report`

```json
{
    "header": {
        "guid": "9f533c717354fd6b2b95ee5111ba88cb",
        "qua": "QV=3&PL=ADR&PR=your_product_name&VE=GA&VN=0.1.0.1000&PP=com.your_product.packagename&DE=TV&CHID=app_channel_id",
        "user": {
            "account_type": 0,
            "account_app_id": "",
            "user_id": ""
        },
        "ip": "8.8.8.8"
    },
    "payload": {
      	"type": "state_report", // device_report: 设备上报，上报设备的开关机状态等；state_report：状态上报，上报当前媒体播放/展示状态；
        "semantic": {
            "domain": "",
            "intent": ""
        },
        "state": {
            "resource_id": "",
            "offset": 0,
            "play_state": 0,
        },
        "detail": {
            "data_source": "",
            "exposure_reason": "",
            "state_reason": ""
        }
    }
}
```

| 参数名                          | 类型       | 是否必选 | 描述                                       |
| ---------------------------- | -------- | ---- | ---------------------------------------- |
| `header`                     | -        | 是    | 消息头                                      |
| `header.guid`                | `string` | 是    |                                          |
| `header.qua`                 | `string` | 是    |                                          |
| `header.user`                | -        | 否    |                                          |
| `header.user.account_type`   | `int`    | 否    | `-1`：未登录<br>`2`：QQ Open登陆<br>`3`：微信登陆    |
| `header.user.account_app_id` | `string` | 否    | 登陆平台的APPID                               |
| `header.user.user_id`        | `string` | 否    | QQ或微信的OpenID                             |
| `header.ip`                  | `string` | 是    | 终端IP（厂商后台代为上报需填该字段）                      |
| `payload`                    | -        | 是    | 上报消息体。消息分为几种类型：<br>`state_report`：上报媒体播放/展示状态；<br>`device_report`：上报设备开关机等状态； |

##### 7.4.2.1 state_report

| 参数名                      | 类型       | 是否必选 | 描述                                       |
| ------------------------ | -------- | ---- | ---------------------------------------- |
| `type`                   | `string` | 是    | 填"state_report"                          |
| `semantic`               | -        | 是    | 语义信息                                     |
| `semantic.domain`        | `string` | 是    | 领域                                       |
| `semantic.intent`        | `string` | 是    | 意图                                       |
| `state`                  | -        | 是    | 状态信息                                     |
| `state.resource_id`      | `string` | 是    | 资源ID                                     |
| `state.offset`           | `int`    | 是    | 资源播放进度Offset，单位为秒                        |
| `state.play_state`       | `int`    | 是    | 播放状态：<br>`1`:播放中；<br>`2`:播放暂停；<br>`3`:播放中断；<br>`4`:播放开始；<br>`5`:播放结束； |
| `detail`                 | -        | 否    | 上报详情                                     |
| `detail.data_source`     | `string` | 否    | 内容来源                                     |
| `detail.exposure_reason` | `string` | 否    | 曝光原因                                     |
| `detail.state_reason`    | `string` | 否    | 进入状态原因                                   |

##### 7.4.2.2 device_report

| 参数名            | 类型       | 描述                              |
| -------------- | -------- | ------------------------------- |
| `type`         | `string` | 填"device_report"                |
| `device`       | -        | 设备状态信息                          |
| `device.state` | `string` | `power_on` 开机<br>`power_off` 关机 |

#### 7.4.3 返回数据

```json
{
    "code": 0,
    "message": ""
}
```

| 参数名       | 类型       | 描述                          |
| --------- | -------- | --------------------------- |
| `code`    | `int`    | 错误码：<br>`0`: 正常；<br>`其他`:异常 |
| `message` | `string` | 错误消息                        |

### 7.5 统一接入接口
#### 7.5.1 接口描述
​	统一接入接口提供终端访问后端各个服务特定接口的能力。本接口根据`payload.domain`和`payload.intent`提供不同的能力。见https://github.com/TencentDingdang/tvs-tools/blob/master/doc/uniAccess%E6%8E%A5%E5%8F%A3%E8%83%BD%E5%8A%9B.md
#### 7.5.2 请求参数
__URL__：`POST https://aiwx.html5.qq.com/api/v1/uniAccess`

```
json
{
    "header": {
        "guid": "【设备唯一标识】",
        "qua": "【设备QUA】",
        "user": {
            "user_id": "",
	        "account":{
	    	    "id":"{{STRING}}",
                "appid":"{{STRING}}",
                "type":"{{STRING}}",
                "token":"{{STRING}}"	
	    }
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8",
        "device": {
            "network": "4G"
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

| 参数名                         | 类型       | 是否必选 | 描述                                  |
| --------------------------- | -------- | ---- | ----------------------------------- |
| ` header `                  | `object` | Yes  | -                                   |
| `header.guid`               | `string` | 是    | 设备唯一标志码。详细说明见[附录-GUID获取](#GUID获取)   |
| `header.qua`                | `string` | 是    | 设备及应用信息，详细说明见[附录-QUA字段说明](#QUA字段说明) |
| `header.user`               | -        | No   | 用户信息                                |
| `header.user.user_id`       | `string` | No   | 用户ID，，详细说明见[附录-USERID](#USERID)     |
| `header.user.account`       | `object` | No   | 用户账户信息                              |
| `header.user.account.id`    | `string` | No   | 用户账户ID，填openid                      |
| `header.user.account.token` | `string` | No   | 用户账户accesstoken                     |
| `header.user.account.type`  | `string` | No   | 用户账户类型,支持`WX`/`QQOPEN`              |
| `header.user.account.appid` | `string` | No   | 用户账户的appid                          |
| `header.ip`                 | `string` | No   | 终端IP                                |
| `header.device`             | `object` | No   | 终端其他信息                              |
| `header.device.network`     | `string` | No   | 终端网络类型                              |


***Payload Parameters***

| 参数名                    | 类型       | 是否必选 | 描述                                       |
| ---------------------- | -------- | ---- | ---------------------------------------- |
| `payload`              | `object` | Yes  | 负载                                       |
| `payload.domain`       | `string` | Yes  | 领域                                       |
| `payload.intent`       | `string` | Yes  | 意图                                       |
| `payload.jsonBlobInfo` | `string` | Yes  | 数据，根据`payload.domain`和`payload.intent`的不同，有不同的数据格式。 |

#### 7.5.3 返回参数
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

| 参数名              | 类型       | 是否必选 | 描述   |
| ---------------- | -------- | ---- | ---- |
| `header`         | `object` | Yes  | 头部   |
| `header.retCode` | `long`   | Yes  | 返回码  |
| `header.errMsg`  | `string` | Yes  | 错误消息 |

***Payload Parameters***

| 参数名                    | 类型       | 是否必选 | 描述   |
| ---------------------- | -------- | ---- | ---- |
| `payload`              | `object` | Yes  | 负载   |
| `payload.jsonBlobInfo` | `string` | Yes  | 数据   |



## 8 腾讯叮当能力评测注意事项

终端接入腾讯叮当时，若有评测需求需向相应的产品接口人申请，告知测试理由、测试QPS及持续时间，评测时有以下需要注意的事项：

1. 评测开始及过程中与接口人保持联系；
2. 测试QPS需以1小时为单位逐渐增加；
3. 测试时GUID及UserID需设置为`auto_test`；

## 9 附录
### 9.1 QUA字段说明
​	QUA是用于标识客户端信息的key-value对，key-value之间以`&`连接，服务端可根据QUA信息给出响应的适配内容。

​	QUA 的key-value说明如下：

| Key  | Value                | 含义     | 备注                                       |
| ---- | -------------------- | ------ | ---------------------------------------- |
| QV   | 3                    | QUA版本号 |                                          |
| PR   | *                    | 终端产品名  | 英文、数字、下划线组成                              |
| PL   | ADR,IOS,LINUX        | 终端平台标识 | 安卓平台填ADR，iOS平台填IOS，Linux平台填LINUX         |
| VE   | P,GA,RC,B1...B9,LAB  | 终端版本名  | P:预览版<br>GA:正式版<br>RC:发布候选<br>BN:BetaN<br>LAB:实验室版 |
| VN   | 主版本.子版本.修正版本.Build   | 终端版本号  | 例如：1.0.1.1000                            |
| PP   | com.company.product  | 终端软件包名 |                                          |
| DE   | PHONE,TV,CAR,SPEAKER | 设备类型   | 手机填PHONE、电视填TV、车载设备填CAR，音箱填SPEAKER       |
| CHID | *                    | 渠道号    |                                          |

​	示例:QV=3&PR=Dingdang&PL=LINUX&VE=GA&VN=1.0.1000&PP=com.tencent.ai.tvs&DE=SPEAKER&CHID=10020

### 9.2 GUID获取

​	如果设备上使用了AISDK，可以从AISDK获取GUID，否则，设备端需要自己生成GUID。

按照如下方式生成：

1. 把厂商的appkey、appSceret和设备唯一序列号三个字符串拼接，以“:”作为分割符，拼接形式为`appkey:appSceret:设备唯一序列号`

2. 取拼接串的md5值小写形式。md5值即为GUID。

   ​

### 9.3 USERID

请将用户openid填入。

### 9.4 TVS-HMAC-SHA256-BASIC签名示例

#### 9.4.1 Python版(依赖requests)

```python
# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install requests`

# 腾讯叮当提供的Bot Key/Secret
botKey = 'bot_key' # Replace with your Bot Key
botSecret = 'bot_secret' # Replace with your Bot Secret

# ***** Task 1: 拼接请求数据和时间戳 *****

## 获取请求数据(也就是HTTP请求的Body)
postData = '{"header": {"guid": "...","qua": "...","user": {"user_id": ""},"lbs": {"longitude": 1.1111,"latitude": 2.2222},"ip": "8.8.8.8"},"payload": {"query": "你叫什么名字"}}'
## 获得ISO8601时间戳
credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

## 拼接数据
signingContent = postData + credentialDate

# ***** Task 2: 获取Signature签名 *****
signature = hmac.new(botSecret, signingContent, hashlib.sha256).hexdigest()

# ***** Task 3: 在HTTP请求头中带上签名信息
authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + botKey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature

headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorizationHeader}

# **** Send the request *****
requestUrl = 'https://aiwx.html5.qq.com/api/v1/richanswer'

print 'Begin request...'
print 'Request Url = ' + requestUrl

## 使用requests.session保持长连接
session = requests.session()
session.headers.update(headers)
print 'Request Headers =' + str(session.headers)

r = session.post(requestUrl, data = postData)

print 'Response...'
print 'HTTP Status Code:%d' % r.status_code
print r.text
```

#### 9.4.2 Java版

```java
//package com.qq.tvs.auth;

import java.nio.charset.Charset;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Hex;
import java.util.Date;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;

public class TVSBasicSigner
{
    private static final String ALGORITHM_HMACSHA256 = "HmacSHA256";
    private static final DateTimeFormatter TIME_FORMATER = DateTimeFormatter.ofPattern("yyyyMMdd'T'HHmmss'Z'");

    public static final String sign(String signingContent, String signingKey)
        throws NoSuchAlgorithmException, InvalidKeyException
    {
        byte[] data = signingContent.getBytes(Charset.forName("UTF-8"));
        byte[] key = signingKey.getBytes(Charset.forName("UTF-8"));

        Mac mac = Mac.getInstance(ALGORITHM_HMACSHA256);
        mac.init(new SecretKeySpec(key, ALGORITHM_HMACSHA256));
        return bytesToHexString(mac.doFinal(data));
    }

    protected static final String bytesToHexString(byte[] bArray) {  
        StringBuffer sb = new StringBuffer(bArray.length);  
        String sTemp;  
        for (int i = 0; i < bArray.length; i++) {  
            sTemp = Integer.toHexString(0xFF & bArray[i]);  
            if (sTemp.length() < 2)  
                sb.append(0);  
            sb.append(sTemp.toLowerCase());  
        }  
        return sb.toString();  
    }

    public static void main(String args[]) {
        String botKey = "bot_key";
        String botSecret = "bot_secret";

        // ***** Task 1: 拼接请求数据和时间戳 *****

        //// 获取请求数据(也就是HTTP请求的Body)
        String postData = "123";
        //// 获得ISO8601时间戳
        ZonedDateTime utc = ZonedDateTime.now(ZoneOffset.UTC);
        String credentialDate = utc.format(TIME_FORMATER);

        //// 拼接数据
        String signingContent = postData + credentialDate;

        // ***** Task 2: 获取Signature签名 *****
        String signature = null;
        try {
            signature = sign(signingContent, botSecret);
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }

        // ***** Task 3: 在HTTP请求头中带上签名信息
        String authorizationHeader = "TVS-HMAC-SHA256-BASIC" + " " + "CredentialKey=" + botKey + ", " + "Datetime=" + credentialDate + ", " + "Signature=" + signature;

        System.out.println("Authorization:" + authorizationHeader);
    }
}
```

### 9.5 错误码

| HTTP Status Code | 错误类型    |
| ---------------- | ------- |
| 401              | 未授权     |
|                  | 签名已过期   |
| 403              | 时间格式有误  |
|                  | 签名验证未通过 |
|                  | Bot不存在  |
| 404              | 资源不存在   |
| 405              | 请求方法不允许 |

### 9.6 更新日志

| 版本    | 日期         | 更新内容                         |
| ----- | ---------- | ---------------------------- |
| V1.14 | 2017/12/06 | 1.添加终端上报接口；<br>2.添加评测注意事项说明； |
| V1.15 | 2017/12/25 | 1.添加终端开关机上报接口；               |
