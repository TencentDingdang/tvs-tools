# 腾讯云小微基础API接入指南



[TOC]

# 目录

- [1 简介](#1-简介)
- [2 术语](#2-术语)
- [3 接口规则](#3-接口规则)
  - [3.1 接入前置条件](#31-接入前置条件)
  - [3.2 协议支持](#32-协议支持)
  - [3.3 HTTP Header要求](#33-HTTP Header要求)
  - [3.4 签名方法](#32-签名方法)
  
- [4 API接口能力](#5-API接口能力)
- [5 API列表](#5-api列表)
  - [5.1 语义请求](#51-语义请求)
  - [5.2 语音识别](#52-语音识别)
  - [5.3 语音合成](#53-语音合成)
  - [5.4 终端状态上报](#54-终端状态上报)
  - [5.5 特殊能力访问](#55-特殊能力访问)
  - [5.6 票据授权](#56-票据授权)
  - [5.7 刷票](#57-刷票)
- [6 Q&A](#6-Q&A)
- [7 附录 ](#7-附录)

# 1 简介

本文档主要针对基础API开发者，描述基础API语音识别、语义理解/技能、语音合成等相关接口内容。

# 2 术语

本文涉及以下术语，具体释义见http://xxxxxxxxx

- 语音合成

- 流式语音合成

- 非流式语音合成

- 语音识别

- 流式语音识别

- 非流式语音识别

- 技能服务

- 语义理解

- 明确语义

  

# 3 接口规则

## 3.1 接入前置条件

### 3.1.1 小微开放平台申请应用并<font color="red">发布</font>



见<https://dingdang.qq.com/doc.html?dir=/doc/tvs/introduce/process.html>

### 3.1.2 接入腾讯云小微账号系统（可选）



如果厂商要接入音乐技能，必须接入腾讯云小微账号系统，见<https://github.com/TencentDingdang/dmsdk/tree/master/doc>

## 3.2 协议支持

厂商调用基础API必须遵循以下规则：

|          |                                                              |
| -------- | ------------------------------------------------------------ |
| 传输方式 | 为保证交易安全性，采用<font color="red">**HTTPS**</font>传输                          |
| 请求方式 | 采用<font color="red">**POST**</font>方法请求                                         |
| 数据格式 | 请求和返回数据都为<font color="red">**JSON**</font>格式                               |
| 字符编码 | 统一采用<font color="red">**UTF-8**</font>字符编码                                    |
| 签名算法 | HMAC-SHA256                                                  |
| 签名要求 | API后台的各个接口都会校验签名，接入方需要将签名信息放到Http Header中。详细方法请参考3.2 签名方法 |


## 3.3  HTTP Header要求

基础API对于HTTP请求的请求头字段有如下要求：

| Header Name   | 是否必须 | 说明                                                         |
| ------------- | -------- | ------------------------------------------------------------ |
| Authorization | 必须     | 该请求头将用于访问权限的验证。请求不带该字段或者签名验证错误的，将会被拒绝访问。`Authorization`包含了签名算法类型、时间戳、签名信息等，比如`CredentialKey`、`Signature`等。关于签名的具体方法，请查阅[签名方法](#34-签名方法)。 |
| Content-Type  | 可选     | 指定`Content-Type: application/json; charset=UTF-8`。        |


## 3.4 签名方法

基础API要求所有的请求都要经过签名，以证明请求是经过授权的。请求通过Hash算法进行加密计算，得到一个请求对应的签名字符串，并将该签名字符串带到`Authorization`请求头中。基础API会对该签名进行校验，对于未带上正确签名的请求将视为未授权的请求并拒绝访问。

基础API支持使用[TVS-HMAC-SHA256-BASIC](#611-TVS-HMAC-SHA256-BASIC签名方法)进行消息签名。TVS-HMAC-SHA256-BASIC签名过程如下：

### 3.4.1 第一步: 拼接请求数据和时间戳得到`SigningContent`
请求数据指的是HTTP Body数据，时间戳取当前的UTC时间，并以ISO8601格式为标准（'YYYYMMDD'T'HHMMSS'Z）。假设当前时间戳为20170701T235959Z，以某个请求为例，得到的`SigningContent`为：
```text
{
    "query": "今天的天气怎样",
    "device":{
    	"serial_num":"1f6befd9f24f332babec26d1106088ce"
    } 
    "qua": "QV=3&PL=ADR&PR=your_product_name&VE=GA&VN=0.1.0.1000&PP=com.your_product.packagename&DE=TV&CHID=app_channel_id"
}20170701T235959Z
```

### 3.4.2 第二步: 计算签名，记为`Signature`

基础API要求使用开放平台分配的`AccessToken`作为签名的密钥，`AccessToken`建议存放在请求方的服务器中，不应该以任何形式暴露给终端。签名使用的算法是`HMAC-SHA256`：
```
Signature = HMAC_SHA256(SigningContent, AccessToken);
```

需要注意的是，在执行hmac时用的是sha256哈希之后的16进制数据，而不是二进制数据，`Signature`同样是hmac之后的16进制数据。

以下为签名算法的伪代码：
```
SigningContent = "This is signing-content";
AccessToken = "AccessToken";
Signature = HMAC_SHA256(SigningContent, AccessToken);
print Signature;

// 结果输出
97d9a01ea1e5e76753128e2f5696fc8b59aff75c25ba243703e6992b00699daf
```
调试签名算法的正确性可以参考：http://tool.oschina.net/encrypt?type=2， 签名结果与该网页计算结果一致即可。

### 3.4.3 第三步: 拼接`Authorization`串，在Header中带上签名信息

计算得到请求内容的签名之后，需要在HTTP Header的`Authorization`中带上签名信息。`Authorization`的结构如下伪代码所示：

```http
Authorization: TVS-HMAC-SHA256-BASIC CredentialKey=[AppKey], Datetime=[Timestamp], Signature=[Signature]
```

以下Demo展示了一个完整的`Authorization`：
```http
Authorization: TVS-HMAC-SHA256-BASIC CredentialKey = 39ba87a1-2we3-4345-8d26-e632646e54b1, Datetime=20170720T193559Z, Signature=d8612ab1ff0301e1016d817c02350a2b76ea62e0
```


签名示例见：samples/signature.py

# 4 API接口能力

| 接口名称      | 能力                                |
| --------- | --------------------------------- |
| 语义理解/技能服务接口 | 提供文本转语义结构，并返回技能服务数据的能力。           |
| 语音识别接口    | 提供流式/非流式语音识别能力。                   |
| 语音合成接口    | 提供语音合成的能力。                        |
| 终端状态上报接口  | 上报终端状态，有助于后台提供更精准的语义服务结果          |
| 特殊能力访问接口  | 为终端提供访问非AI的其他能力，如换取资源URL、访问智能家居 |
| 票据授权接口 | 给手机端传过来的client_id授权，返回授权串`authorization`与刷票串`tvsRefreshToken`。 |
| 刷票接口 | 使用`tvsRefreshToken`刷票，返回最新授权串`authorization`与刷票串`tvsRefreshToken`。 |

其中核心的语音识别、语义理解、语音合成三个接口在典型的语音交互系统中使用方法如下图所示：
![三个接口使用方法](img/api_case.png)

# 5 API列表

## 5.1 语义请求接口

### 5.1.1 接口描述
​     该接口为语义理解、技能服务接口，语义理解能够分析出文本中的领域、意图、语义结构。技能服务可以根据语义理解结果返回相应的服务数据。例如“我想听周杰伦的歌”，语义理解的领域为song，意图为play，歌手名为周杰伦。服务接口根据语义理解结果，返回周杰伦的歌单。

### 5.1.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/v1/richanswerV2`

请求示例

```json
{
    "header": {
    	"device": {
            "network": "4G",
            "serial_num":"{{STRING}}"
        },
        "qua": "【设备QUA】",
        "user": {
            "user_id": "{{STRING}}",
            "account":{
                "id": "{{STRING}}",
                "appid": "{{STRING}}",
                "type": "{{STRING}}",
                "token": "{{STRING}}"   
            },
            "authorization": "{{STRING}}"
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8"

    },
    "payload": {
        "query": "我想听刘德华的歌",
        "semantic": {
            "domain": "{{STRING}}",
            "intent": "{{STRING}}",
            "slots": [
                {
                    "name": "{{STRING}}",
                    "type": "{{STRING}}",
                    "slot_struct": LONG,
                    "values": [
                        {
                            "origin_text": "{{STRING}}",
                            "text": "{{STRING}}"
                        },
                        {
                            "origin_text": "{{STRING}}",
                            "text": "{{STRING}}"
                        }
                    ]
                }
            ],
        },
        "semantic_extra": {
            "cmd": "{{STRING}}"
        },
        "extra_data":[          
            {
                "type":"IMAGE",
                "data_base64":"{{STRING}}"
            },
            {
                "type":"AUDIO",
                "data_base64":"{{STRING}}"
            },
            {
                "type":"VIDEO",
                "data_base64":"{{STRING}}"
            }
        ]
    }
}
```

| 参数名                      |   类型   | 是否必选 | 描述                                                         |
| --------------------------- | :------: | :------: | ------------------------------------------------------------ |
| `header`                    |    -     |    是    | 请求头                                                       |
| `header.device`                   |    -     |  是   |   设备信息          |
| `header.device.network`           | `string` |  否   | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`                        |
| `header.device.serial_num`        | `string` |  是   | 设备<font color="red">唯一序列号</font>。请保证每个设备唯一，以免影响用户体验。 |
| `header.qua`                      | `string` |  是   | 应用信息，详细说明见[附录-QUA字段说明](#71-QUA字段说明)   |
| `header.user`               |    -     |    否    | 用户信息                                                     |
| `header.user.authorization` | `string` |    No    | 授权信息(使用account相关接口得到的authorization)。本字段填写后，`header.device.serial_num`与`header.user`都不需要填写。|
| `header.user.user_id`       | `string` |    -     | 用户ID，，详细说明见[附录-USERID](#73-USERID)                   |
| `header.user.account`       | `object` |    -     | 用户账户信息                                                 |
| `header.user.account.id`    | `string` |    -     | 用户账户ID，填openid                                         |
| `header.user.account.token` | `string` |    -     | 用户账户accesstoken                                          |
| `header.user.account.type`  | `string` |    -     | 用户账户类型,支持`WX`/`QQOPEN`                               |
| `header.user.account.appid` | `string` |    -     | 用户账户的appid                                              |
| `header.lbs`                |    -     |    否    | 用户位置信息                                                 |
| `header.lbs.longitude`      | `double` |    -     | 经度                                                         |
| `header.lbs.latitude`       | `double` |    -     | 纬度                                                         |
| `header.ip`                 | `string` |    否    | 终端IP。如果是云端对接，需要填写。如果是终端直接调用，不需要填写。 |
| `payload`                   |    -     |    是    | 请求内容                                                     |
| `payload.query`             | `string` |    是    | 用户query                                                    |
| `payload.semantic`          |    -     |    否    | 明确语义信息，若带上，则请求不经过NLP。一般不需要带，某些特殊能力需要。
| `payload.semantic.domain`   | `string` |    否    | 领域信息                                                     |
| `payload.semantic.intent`   | `string` |    否    | 意图信息                                                     |
| `payload.semantic.slots`    |    -     |    否    | 语义参数信息（语义槽位）                                          |
| `payload.semantic_extra`    |    -     |    否    | 附加语义信息                                                 |
| `payload.semantic_extra.cmd`         | `string` |  否   | 语义命令字<br>`SEMANTIC_CMD_FORCE_SESSION_COMPLETE`:强制语义结束当前的session(清除多轮)<br>`SEMANTIC_CMD_FORCE_CLEAR_SESSION`:强制清除session<br>`SEMANTIC_CMD_FORCE_CLEAR_PREV_SESSION`:清除上一个session数据<br>`SEMANTIC_CMD_NOT_SAVE_CURRENT_SESSION`:当次请求不保存session数据               <br>

| `payload.extra_data`              |    -     |  否   | 额外数据信息，特殊能力才需要                                   |
| `payload.extra_data{type}`        |    -     |  否   | 额外数据类型：<br>`IMAGE`：图片；<br>`AUDIO`：语音；<br>`VIDEO`：视频； |
| `payload.extra_data{data_base64}` | `string` |  否   | 额外数据`Base64`编码                           |


### 5.1.3 返回参数

```json
{
    "header": {
        "semantic": {
            "code": 0,
            "msg": "",
            "domain": "{{STRING}}",
            "intent": "{{STRING}}",
            "session_complete": true,
            "slots":[
                {
                    "name":"location",
                    "value":"深圳"
                }
            ]
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
| `header.semantic.slots` | `array`  | 语义槽列表，见[文档](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/slots.md)     |
| `header.semantic.slots.name`       | `string`   | 语义槽位名称     |
| `header.semantic.slots.value`      | `string`   | 语义槽位值     |
| `header.session`                   | -        | 会话                                       |
| `header.session.session_id`        | `string` | 会话ID                                     |
| `payload`                          | -        | 消息体                                      |
| `payload.response_text`            | `string` | 显示正文内容                                   |
| `payload.data`                     | -        | 领域数据                                     |
| `payload.data.json`                | -        | 领域结构化Json数据，数据格式详见https://github.com/TencentDingdang/tvs-tools/blob/master/doc/%E6%9C%8D%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%8D%8F%E8%AE%AE%E8%A7%84%E8%8C%83_V3.md |
| `payload.data.json_template`       | -        | **废弃**。  |

 

示例代码见：samples/richanswerv2.py，samples/richanswerv2_ext.py

## 5.2 语音识别

### 5.2.1 接口描述

该接口提供(非)流式语音识别的能力。语音识别按是否采用云端VAD分为两种情况：

| 类型    | 说明                                       |
| ----- | ---------------------------------------- |
| 云端VAD | 当payload.open_vad=true时，语音识别引擎将会自动识别用户说话结束。自动返回最终识别结果。适用于音箱收音等非手动控制结束的场景 |
| 本地VAD | 当payload.open_vad=false时，语音识别引擎不会自动识别用户说话结束。需要终端主动设置结束标识(voice_finished=true)，语音识别引擎才会返回最终识别结果。适用于**按下说话,抬起结束**的收音场景，如遥控器。 |

### 5.2.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/asr`

```json
{
    "header": {
        "device": {
            "network": "4G",
            "serial_num":"{{STRING}}"
        },
        "qua": "【QUA】",
        "user": {
            "user_id": ""
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8"
    },
    "payload": {
        "voice_meta": {
            "compress": "PCM",
            "sample_rate": "8K",
            "channel": 1,
            "language": "{{STRING}}",
            "offset":0
        },
        "open_vad": true,
        "session_id": "{{STRING}}",
        "index": 0,
        "voice_finished": false,
        "voice_base64": "{{STRING}}"
    }
}
```

| 参数名                              |    类型    | 是否必选 | 描述                                       |
| -------------------------------- | :------: | :--: | ---------------------------------------- |
| `header`                         |    -     |  是   | 请求头                                      |
| `header.device`                   |    -     |  是   |   设备信息          |
| `header.device.network`           | `string` |  否   | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`                        |
| `header.device.serial_num`        | `string` |  是   | 设备<font color="red">唯一序列号</font>。请保证每个设备唯一，以免影响用户体验。 |
| `header.qua`                     | `string` |  是   | 设备及应用信息，详细说明见[附录-QUA字段说明](#71-QUA字段说明)   |
| `header.user`                    |    -     |  否   | 用户信息                                     |
| `header.user.user_id`            | `string` |  -   | 用户ID，，详细说明见[附录-USERID](#73-USERID)          |
| `header.lbs`                     |    -     |  否   | 用户位置信息                                   |
| `header.lbs.longitude`           | `double` |  -   | 经度                                       |
| `header.lbs.latitude`            | `double` |  -   | 纬度                                       |
| `header.ip`                      | `string` |  否  | 终端IP。如果是云端对接，需要填写。如果是终端直接调用，不需要填写。 |
| `payload`                        |    -     |  是   | 请求内容                                     |
| `payload.voice_meta`             |    -     |  是   | 语音配置信息                                   |
| `payload.voice_meta.compress`    | `string` |  是   | 压缩类型：`PCM`/`WAV`/`SPEEX`/`AMR`/`OPUS`/`MP3` |
| `payload.voice_meta.sample_rate` | `string` |  是   | 采样率：`8K`/`16K`                           |
| `payload.voice_meta.channel`     |  `int`   |  是   | 音频通道数：`1`/`2`                            |
| `payload.voice_meta.language`    | `string` |  否   | 语言类型(默认汉语)<br>ENGLISH:英语                 |
| `payload.voice_meta.offset`      |  `int`   |  否   | 语音片偏移量                                   |
| `payload.open_vad`               |  `bool`  |  是   | 是否打开VAD                                  |
| `payload.session_id`             | `string` |  否   | 流式识别过程中必填                                |
| `payload.index`                  |  `int`   |  是   | 语音片偏移量(英文时为语音包序号)                        |
| `payload.voice_finished`         |  `bool`  |  是   | 语音是否结束                                   |
| `payload.voice_base64`           | `string` |  是   | 语音数据的`Base64`编码                          |


### 5.2.3 返回参数

```json
{
    "header": {
        "session": {
            "session_id": "{{STRING}}"
        }
    },
    "payload": {
        "ret":0,
        "final_result": false,
        "result": "深圳市今天天气"
    }
}
```

| 参数名                      | 类型     | 描述                                     |
| --------------------------- | -------- | ---------------------------------------- |
| `header`                    | -        | 消息头                                   |
| `header.session`            | -        | 会话                                     |
| `header.session.session_id` | `string` | 会话ID                                   |
| `payload`                   | -        | 消息体                                   |
| `payload.final_result`      | `bool`   | 是否最终结果                             |
| `payload.result`            | `string` | 语音识别结果                             |
| `payload.ret`               | `int`    | 返回状态，如果是0表示正常返回，非0为错误 |
示例代码见1:  samples/asr.py

 

## 5.3 语音合成
### 5.3.1 接口描述
(非)流式文本转换为语音。

| 类型     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 流式合成 | 当payload.single_request=false时，TTS引擎将会分多次返回语音合成结果，最终结果是多次数据的拼接。优点是终端可以迅速收到TTS部分回包，进行TTS播放，体验较好。缺点是终端代码逻辑复杂。建议使用这种方式。 |
| 一次合成 | 当payload.single_request=true时，TTS引擎将语音合成结果一次性返回。 优点是终端代码逻辑简单，缺点是合成速度较慢 |


### 5.3.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/tts`

```json
{
    "header": {
        "device": {
            "network": "4G",
            "serial_num":"{{STRING}}"
        },
        "qua": "【QUA】",
        "user": {
            "user_id": ""
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8"
    },
    "payload": {
        "speech_meta": {
            "compress": "MP3",
            "person": "LIBAI",
            "volume": 50,
            "speed": 50,
            "pitch": 50
        },
        "session_id": "{{STRING}}",
        "index": 0,
        "single_request": false,
        "content": {
            "text": "{{STRING}}"
        }
    }
}
```

| 参数名                         |   类型   | 是否必选 | 描述                                                         |
| ------------------------------ | :------: | :------: | ------------------------------------------------------------ |
| `header`                       |    -     |    是    | 请求头                                                       |
| `header.device`                |    -     |    是    | 设备信息                                                     |
| `header.device.network`        | `string` |    否    | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`                        |
| `header.device.serial_num`     | `string` |    是    | 设备<font color="red">唯一序列号</font>。请保证每个设备唯一，以免影响用户体验。 |
| `header.qua`                   | `string` |    是    | 设备及应用信息，详细说明见[附录-QUA字段说明](#71-QUA字段说明) |
| `header.user`                  |    -     |    否    | 用户信息                                                     |
| `header.user.user_id`          | `string` |    -     | 用户ID，，详细说明见[附录-USERID](#73-USERID)                   |
| `header.lbs`                   |    -     |    否    | 用户位置信息                                                 |
| `header.lbs.longitude`         | `double` |    -     | 经度                                                         |
| `header.lbs.latitude`          | `double` |    -     | 纬度                                                         |
| `header.ip`                    | `string` |    否    | 终端IP。如果是云端对接，需要填写。如果是终端直接调用，不需要填写。 |
| `payload`                      |    -     |    是    | 请求内容                                                     |
| `payload.speech_meta`          |    -     |    是    | 语音配置信息                                                 |
| `payload.speech_meta.compress` | `string` |    是    | 压缩类型：`WAV`/`MP3`/`AMR`                                  |
| `payload.speech_meta.person`   | `string` |    否    | 发音人：`ZHOULONGFEI`/`CHENANQI`/`YEZI`/`YEWAN`/`DAJI`/`LIBAI`/`NAZHA`/`MUZHA`/`WY` |
| `payload.speech_meta.volume`   |  `int`   |    否    | 音量：0~100（默认50）                                        |
| `payload.speech_meta.speed`    |  `int`   |    否    | 语速：0~100（默认50）                                        |
| `payload.speech_meta.pitch`    |  `int`   |    否    | 声调：0~100（默认50）                                        |
| `payload.session_id`           | `string` |    否    | 流式TTS过程中必填                                            |
| `payload.index`                |  `int`   |    是    | 请求的语音片序号                                             |
| `payload.single_request`       |  `bool`  |    是    | 是否一次合成：<br>`true`：一次合成；<br>`false`：流式合成；  |
| `payload.content`              |    -     |    是    | TTS内容                                                      |
| `payload.content.text`         | `string` |    是    | 转语音的文本内容                                             |


### 5.3.3 返回参数

```json
{
    "header": {
        "session": {
            "session_id": "{{STRING}}"
        }
    },
    "payload": {
        "speech_finished": false,
        "speech_base64": "{{STRING}}"
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

示例代码见1:  samples/tts.py

## 5.4 终端状态上报
### 5.4.1 接口描述
   为了给用户提供更多个性化的内容，保证更优的体验。终端可以通过上报接口向腾讯后台上报终端的媒体播放等状态。对于依赖终端
### 5.4.2 请求参数
__URL__：`POST https://aiwx.html5.qq.com/api/v1/report`

```json
{
    "header": {
        "device": {
            "network": "4G",
            "serial_num":"{{STRING}}"
        },
        "qua": "【QUA】",
        "user": {
            "account_type": 0,
            "account_app_id": "",
            "user_id": ""
        },
        "ip": "8.8.8.8"
    },
    "payload": {
        "type": "state_report", // state_report：状态上报，上报当前媒体播放/展示状态；
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
| `header.device`                   |    -     |  是   |   设备信息          |
| `header.device.network`           | `string` |  否   | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`                        |
| `header.device.serial_num`        | `string` |  是   | 设备<font color="red">唯一序列号</font>。请保证每个设备唯一，以免影响用户体验。 |
| `header.qua`                 | `string` | 是    |                                          |
| `header.user`                | -        | 否    |                                          |
| `header.user.account_type`   | `int`    | 否    | `-1`：未登录<br>`2`：QQ Open登陆<br>`3`：微信登陆    |
| `header.user.account_app_id` | `string` | 否    | 登陆平台的APPID                               |
| `header.user.user_id`        | `string` | 否    | QQ或微信的OpenID                             |
| `header.ip`                  | `string` | 是    | 终端IP。如果是云端对接，需要填写。如果是终端直接调用，不需要填写。 |
| `payload`                    | -        | 是    | 上报消息体。消息分为几种类型：<br>`state_report`：上报媒体播放/展示状态；<br>`device_report`：上报设备开关机等状态； |

#### 5.3.2.1 state_report

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


### 5.4.3 返回数据

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

## 5.5 特殊能力访问
### 5.5.1 接口描述
   特殊能力访问接口提供终端访问后端各个服务特定接口的能力。本接口根据`payload.domain`和`payload.intent`提供不同的能力。见https://github.com/TencentDingdang/tvs-tools/blob/master/doc/uniAccess%E6%8E%A5%E5%8F%A3%E8%83%BD%E5%8A%9B.md
### 5.5.2 请求参数
__URL__：`POST https://aiwx.html5.qq.com/api/v1/uniAccess`

```json
{
    "header": {
        "device": {
            "network": "4G",
            "serial_num":"{{STRING}}"
        },
        "qua": "【QUA】",
        "user": {
            "user_id": "",
            "account":{
                "id":"{{STRING}}",
                "appid":"{{STRING}}",
                "type":"{{STRING}}",
                "token": "{{STRING}}"   
            },
            "authorization": "{{STRING}}"
        },
        "lbs": {
            "longitude": 132.56481,
            "latitude": 22.36549
        },
        "ip": "8.8.8.8"
    },
    "payload": {
        "domain": "{{STRING}}",
        "intent": "{{STRING}}",
        "jsonBlobInfo": "{{STRING}}"
    }
}
```

***Header Parameters***

| 参数名                      | 类型     | 是否必选 | 描述                                                         |
| --------------------------- | -------- | -------- | ------------------------------------------------------------ |
| ` header `                  | `object` | Yes      | -                                                            |
| `header.device`                   |    -     |  Yes   |   设备信息          |
| `header.device.network`           | `string` |  No   | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`                        |
| `header.device.serial_num`        | `string` |  Yes  | 设备<font color="red">唯一序列号</font>。请保证每个设备唯一，以免影响用户体验。 |
| `header.qua`                | `string` | Yes    | 设备及应用信息，详细说明见[附录-QUA字段说明](#71-QUA字段说明) |
| `header.user`               | -        | No       | 用户信息                                                     |
| `header.user.authorization` | `string` | No       | 授权信息(使用account相关接口得到的authorization)。本字段填写后，`header.device.serial_num`与`header.user`都不需要填写。 |
| `header.user.user_id`       | `string` | No       | 用户ID，详细说明见[附录-USERID](#73-USERID)                   |
| `header.user.account`       | `object` | No       | 用户账户信息                                                 |
| `header.user.account.id`    | `string` | No       | 用户账户ID，填openid                                         |
| `header.user.account.token` | `string` | No       | 用户账户accesstoken                                          |
| `header.user.account.type`  | `string` | No       | 用户账户类型,支持`WX`/`QQOPEN`                               |
| `header.user.account.appid` | `string` | No       | 用户账户的appid                                              |
| `header.ip`                 | `string` | No       | 终端IP。如果是云端对接，需要填写。如果是终端直接调用，不需要填写。           |
| `header.device`             | `object` | No       | 终端其他信息                                                 |
| `header.device.network`     | `string` | No       | 终端网络类型                                                 |
| `header.device.serialNum`   | `string` | 否       | 设备唯一序列号                                               |

***Payload Parameters***

| 参数名                    | 类型       | 是否必选 | 描述                                       |
| ---------------------- | -------- | ---- | ---------------------------------------- |
| `payload`              | `object` | Yes  | 负载                                       |
| `payload.domain`       | `string` | Yes  | 领域                                       |
| `payload.intent`       | `string` | Yes  | 意图                                       |
| `payload.jsonBlobInfo` | `string` | Yes  | 数据，根据`payload.domain`和`payload.intent`的不同，有不同的数据格式。 |

### 5.5.3 返回参数
```json
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

示例代码见：samples/uniAccess.py



## 5.6 票据授权

### 5.6.1 接口描述

提供终端ClientId票据授权接口。

调用时机： 设备侧第一次拿到手机端传过来的clientid，需要调用本接口换取对应的`tvsRefreshToken`和`authorization`，`tvsRefreshToken`用于刷票接口（7.8节）。`authorization`内部有账号与设备信息，调用7.1-7.6接口时，把`authorization`填入`header.user.authorization`。如果填入`header.user.authorization`，那么`header.guid`,`header.user`其他字段都不需要填写。

### 5.6.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/v1/account/authorize`

```json
{
    "header": {
        "qua": "{{STRING}}",
        "ip": "8.8.8.8",
        "device": {
            "network": "4G"
        }
    },
    "payload": {
    	"clientId":"{{STRING}}"
    }
}
```



| 参数名                              |    类型    | 是否必选 | 描述                                       |
| -------------------------------- | :------: | :--: | ---------------------------------------- |
| `header`                         |    -     |  是   | 请求头       |
| `header.qua`                     | `string` |  是   | 设备及应用信息，详细说明见[附录-QUA字段说明](#71-QUA字段说明)   |
| `header.ip`                      | `string` |  否   | 终端IP，仅限云端使用。终端直接调用不需要填。 |
| `header.device`                  |    -     |  否   |                 |
| `header.device.network`          | `string` |  否   | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`                        |
| `payload`                        |    -     |  是   | 请求内容                                     |
| `payload.clientId` |    -     |  是   | DMSDK ClientId |


### 5.6.3 返回参数
```json
{
    "header": {
        "retCode": 0,
        "errMsg": "{{STRING}}"
    },
    "payload": {
        "tvsRefreshToken": "{{STRING}}"，
        "authorization": "{{STRING}}"，
        "expiredTimeInSeconds":{{INT}}
    }
}
```

***Header Parameters***

| 参数名           | 类型     | 是否必选 | 描述                                                        |
| ---------------- | -------- | -------- | ----------------------------------------------------------- |
| `header`         | `object` | Yes      | 头部                                                        |
| `header.retCode` | `long`   | Yes      | 返回码。如果错误码不等于0且大于-1000000，可以认为票据无效。 |
| `header.errMsg`  | `string` | Yes      | 错误消息                                                    |

***Payload Parameters***

| 参数名                    | 类型       | 是否必选 | 描述   |
| ---------------------- | -------- | ---- | ---- |
| `payload`              | `object` | Yes  | 负载   |
| `payload.tvsRefreshToken` | `string` | Yes  | tvsRefreshToken，刷票用 |
| `payload.authorization` | `string` | Yes  | 账户信息。用在其他请求的`header.user.authorization`中。 |
| `payload.expiredTimeInSeconds` | `int` | Yes  | 票据过期时间 (秒)。到达过期时间，需要调用7.8刷票接口重新刷票。 |


## 5.7 刷票
### 5.7.1 接口描述

提供终端刷票接口。

### 5.7.2 请求参数

__URL__：`POST https://aiwx.html5.qq.com/api/v1/account/refresh`

```json
{
    "header": {
        "qua": "{{STRING}}",
        "ip": "8.8.8.8",
        "device": {
            "network": "4G"
        }
    },
    "payload": {
        "tvsRefreshToken": "{{STRING}}"
    }
}
```



| 参数名                              |    类型    | 是否必选 | 描述                                       |
| -------------------------------- | :------: | :--: | ---------------------------------------- |
| `header`                         |    -     |  是   | 请求头       |
| `header.qua`                     | `string` |  是   | 设备及应用信息，详细说明见[附录-QUA字段说明](#71-QUA字段说明)   |
| `header.ip`                      | `string` |  否   | 终端IP，仅限云端使用。终端直接调用不需要填。                 |
| `header.device`                  |    -     |  否   |                 |
| `header.device.network`          | `string` |  否   | 网络类型：`5G`/`4G`/`3G`/`2G`/`Wi-Fi`              |
| `payload`                        |    -     |  是   | 请求内容                                     |
| `payload.tvsRefreshToken` |    -     |  是   | TVS刷票Token     |


### 5.7.3 返回参数
```json
{
    "header": {
        "retCode": 0,
        "errMsg": "{{STRING}}"
    },
    "payload": {
        "tvsRefreshToken": "{{STRING}}"，
        "authorization": "{{STRING}}"，
        "expiredTimeInSeconds":{{INT}}
    }
}
```

***Header Parameters***

| 参数名           | 类型     | 是否必选 | 描述                                                        |
| ---------------- | -------- | -------- | ----------------------------------------------------------- |
| `header`         | `object` | Yes      | 头部                                                        |
| `header.retCode` | `long`   | Yes      | 返回码。如果错误码不等于0且大于-1000000，可以认为票据无效。 |
| `header.errMsg`  | `string` | Yes      | 错误消息                                                    |

***Payload Parameters***

| 参数名                    | 类型       | 是否必选 | 描述   |
| ---------------------- | -------- | ---- | ---- |
| `payload`              | `object` | Yes  | 负载   |
| `payload.tvsRefreshToken` | `string` | Yes  | 最新tvsRefreshToken，下次刷票使用。 |
| `payload.authorization` | `string` | Yes  | 最新账户信息。每次请求7.1-7.6的接口，都需要用最新账户信息。 |
| `payload.expiredTimeInSeconds` | `int` | Yes  | 过期时间 (秒)。到达过期时间，需要重新刷票。 |


# 6 Q&A
## 6.1 使用了TVS API，想同时使用基础API，账户、设备信息怎么填。

将TVS API的`tvsToken`填到`header.user.authorization`中即可。其他字段无需填写。

## 6.2 报SSL证书校验错误

check以下几项

- 调用方系统时间是否调对，SSL证书有有效时间范围
- 调用方的SSL库是否支持`server_name`扩展。

## 6.3 返回403、401等4XX错误码

打印下返回的http response body，上面有错误原因。

如果是签名错误，check以下几项：

- 签名算法是否正确。
- Http content-length是否正确。
- 签名Appkey，Accesstoken是否有拼写错误

如果是签名过期的错误，check以下几项：

- 时间戳是否UTC时间或者北京时间。

- 调用方系统时间是否与真实时间差5分钟以上，如果差距大，请调好时间。

如果报Appkey未配置，check以下几项：

 	- appkey拼写是否正确。
 	- 开放平台是否已经发布应用，如果已经发布，等待10分钟后再试。

## 6.4 返回的领域/意图/回复语等不对

正常的会话返回的领域意图与上下文严重相关。

遇到这种问题，请将发生的时间点，设备唯一序列号、Query、预期的落域/回复语、实际的返回数据反馈给对接的产品经理。

## 6.5 流式语音无法正常识别怎么定位

check一下几项：

- 将发送给腾讯后台的语音保存起来，人工听一下音频质量。音频质量差，自然不好识别。
- 同一次流式的语音识别，是否都用的同一个sessionid
- `index`参数填写是否正确。
- 发包过程是否有丢包


## 6.6 语音识别速度慢

check一下几项：

- 网络质量。
- 是否使用了并行发包形式去请求腾讯后台。

## 6.7 如何取消语义多轮

使用语义请求接口，赋值`payload.semantic_extra.cmd`为`SEMANTIC_CMD_FORCE_SESSION_COMPLETE`即可。

## 6.8 基于基础API，如何使用腾讯的图像识别能力

见[https://github.com/TencentDingdang/tvs-tools/blob/master/doc/%E8%85%BE%E8%AE%AF%E5%8F%AE%E5%BD%93%E5%9B%BE%E5%83%8F%E8%AF%86%E5%88%AB%E6%B5%81%E7%A8%8B%E6%96%87%E6%A1%A3.md](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/腾讯叮当图像识别流程文档.md)



# 7 附录
## 7.1 QUA字段说明

  QUA是用于标识客户端信息的key-value对，key-value之间以`&`连接，服务端可根据QUA信息给出响应的适配内容。

   **终端每次请求腾讯后台时，都需要在请求结构体中带上QUA信息。**

   QUA 的key-value说明如下：

| Key  | 是否必填  | 数据类型   | Value               | 含义     | 备注                                       |
| ---- | ----- | ------ | ------------------- | ------ | ---------------------------------------- |
| QV   | **是** | Number | 3                   | QUA版本号 | ** 默认填3，不能更改。**标识QUA的版本。                 |
| VN   | **是** | String | 主版本.子版本.修正版本.Build  | 终端版本号  | **格式必须为四段。且新版本的版本号必须比旧版本大（按字母排序）。**<br>例如：1.0.1.1000。 |
| PP   | **是** | String | com.company.product | 终端软件包名 | 例如：com.tencent.ai.tvs。                   |
| VE   | 否     | String | P,GA,RC,B1...B9     | 终端版本名  | P: 预览版<br>GA: 正式版<br>RC: 发布候选<br>BN: BetaN<br> |
| CHID | 否     | Number | 10020               | 渠道号    | 用于区分不同的渠道，如：线上渠道，线下渠道。                   |


   **示例**: QV=3&VE=GA&VN=1.0.1000&PP=com.tencent.ai.tvs&CHID=10020


## 7.2 GUID获取

   如果设备上使用了AISDK，可以从AISDK获取GUID，否则，设备端需要自己生成GUID。

按照如下方式生成：

1. 把厂商的appkey、accessToken和设备唯一序列号三个字符串拼接，以“:”作为分割符，拼接形式为`appkey:accessToken:设备唯一序列号`

2. 取拼接串的md5值小写形式。md5值即为GUID。

   

## 7.3 USERID

请将用户openid填入。

## 7.4 TVS-HMAC-SHA256-BASIC签名示例

### 7.4.1 Python版(依赖requests)

```python
# -*- coding: UTF-8 -*-
import datetime, hashlib, hmac
import requests # Command to install: `pip install requests`

# 开放平台提供的Appkey/AccessToken
AppKey = 'AppKey' # Replace with your appKey
accessToken = 'AccessToken' # Replace with your accessToken

# ***** Task 1: 拼接请求数据和时间戳 *****

## 获取请求数据(也就是HTTP请求的Body)
postData = '{"header": {"guid": "{{STRING}}","qua": "{{STRING}}","user": {"user_id": "{{STRING}}"},"lbs": {"longitude": 1.1111,"latitude": 2.2222},"ip": "8.8.8.8"},"payload": {"query": "你叫什么名字"}}'
## 获得ISO8601时间戳
credentialDate = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

## 拼接数据
signingContent = postData + credentialDate

# ***** Task 2: 获取Signature签名 *****
signature = hmac.new(accessToken, signingContent, hashlib.sha256).hexdigest()

# ***** Task 3: 在HTTP请求头中带上签名信息
authorizationHeader = 'TVS-HMAC-SHA256-BASIC' + ' ' + 'CredentialKey=' + AppKey + ', ' + 'Datetime=' + credentialDate + ', ' + 'Signature=' + signature

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

### 7.4.2 Java版

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
        String appKey = "appKey";
        String accessToken = "accessToken";

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
            signature = sign(signingContent, accessToken);
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }

        // ***** Task 3: 在HTTP请求头中带上签名信息
        String authorizationHeader = "TVS-HMAC-SHA256-BASIC" + " " + "CredentialKey=" + appKey + ", " + "Datetime=" + credentialDate + ", " + "Signature=" + signature;

        System.out.println("Authorization:" + authorizationHeader);
    }
}
```

## 7.5 错误码

| HTTP Status Code | 错误类型    |
| ---------------- | ------- |
| 401              | 未授权     |
|                  | 签名已过期   |
| 403              | 时间格式有误  |
|                  | 签名验证未通过 |
|                  | Bot不存在  |
| 404              | 资源不存在   |
| 405              | 请求方法不允许 |

## 7.6 更新日志

| 日期         | 更新内容                         |
| ---------- | ---------------------------- |
| 2017/12/06 | 1.添加终端上报接口；<br>2.添加评测注意事项说明； |
| 2017/12/25 | 1.添加终端开关机上报接口；               |
| 2019/05/15 | 整体修改               |
