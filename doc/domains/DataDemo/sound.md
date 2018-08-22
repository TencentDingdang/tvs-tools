[TOC]

### 领域名称

声音百科

### 意图列表

| Intent | Description                         |
| ------ | ----------------------------------- |
| search_sound   | 声音查询                                |
| search_lastsound   | 持续声音查询 |

### 数据示例

##### search_sound、search_lastsound 音频类模版

```json
/*
 * search_sound search_lastsound 音频类模版
 * 语料：我要听狗的声音
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "这就给你播狗的声音",
	"strSpeakTipsText": "这就给你播狗的声音"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "true", 
        "orientation": "portrait", 
        "textSpeak": "true", 
        "type": "AUDIO", 
        "version": "1.0.0"
    }, 
    "globalInfo": {
        "selfData": {
            "eType": 1,                             // 0 表示仅播放一次 1 表示循环播放 2 表示播放指定时长
            "sDurationTime": "",                    // 当且仅当 eType 为 2 时生效，单位“秒”
            "sResText": "这就给你播狗的声音"        // 播放完声音后的TTS播报
        }
    }, 
    "listItems": [
        {
            "audio": {
                "metadata": {
                    "offsetInMilliseconds": 0, 
                    "totalMilliseconds": 0
                }, 
                "stream": {
                    "url": "http://softfile.3g.qq.com/myapp/soft_imtt/smartChildVoice/Animals/Dog.mp3"
                }
            }, 
            "mediaId": "313", 
            "title": "",
            "textContent": ""
        }
    ]
}
```

##### search_sound、search_lastsound 文本模版

```json
/*
 * search_sound search_lastsound 无模版
 * 语料：我要听外星人的声音 （当没有查询到资源时的模版）
 * BOT：格力空调 (8d3b6076-3bb4-4c26-89c3-011447996044)
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
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "globalInfo": {
        "selfData": {
            "eType": 0, 
            "sDurationTime": "", 
            "sResText": ""
        }
    }, 
    "listItems": [
        {
            "audio": {
                "metadata": {
                    "offsetInMilliseconds": 0, 
                    "totalMilliseconds": 0
                }, 
                "stream": {
                    "url": ""
                }
            }, 
            "mediaId": "", 
            "textContent": "唉呀，还没有“外星人”的声音。下次更新时，我会补全的。", 
            "title": ""
        }
    ]
}
```
