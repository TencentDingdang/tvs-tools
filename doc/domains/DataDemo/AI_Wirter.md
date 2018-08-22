[TOC]

### 领域名称

AI写作

### 意图列表

| Intent                  | Description  |
| ----------------------- | ------------ |
| create          | 根据藏头词作诗       |

### 数据示例

##### 全意图 音频模版

```json
/*
 * 音频模版
 * 语料：计算器藏头诗
 * BOT：QB智能助手 (69156881-10bb-40dd-92e0-db5329b044dc)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": ""
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "true", 
        "orientation": "portrait", 
        "textSpeak": "false", 
        "type": "AUDIO", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "audio": {
                "metadata": {
                    "offsetInMilliseconds": 0, 
                    "totalMilliseconds": 0
                }, 
                "stream": {
                    "url": "http://inner.mig.test.cdn.qq.com:8080/dingdang/poem_new/201807/05/10/20180705T103650_0424238335.mp3"
                }
            }, 
            "selfData": {
                "strAudioUrl": "http://inner.mig.test.cdn.qq.com:8080/dingdang/poem_new/201807/05/10/20180705T103650_0424238335.mp3", 
                "strShareIconUrl": "http://res.imtt.qq.com/hotwords/icon/qqbrowser.jpg", 
                "strShareSubtitle": "", 
                "strShareTitle": "QQ浏览器帮我作了一首诗，快来发现其中的秘密！", 
                "strShareUrl": "http://smartbox.cs0309.html5.qq.com/poetry?key=60d12e74bd992608463b4b00b6c74e5f", 
                "strText": "计钧何德为螺青，
算面迎春已一叹。
器到尘埃今未得，
一身横上谁能看。"
            }, 
            "textContent": "计钧何德为螺青，
算面迎春已一叹。
器到尘埃今未得，
一身横上谁能看。"
        }
    ]
}
```
