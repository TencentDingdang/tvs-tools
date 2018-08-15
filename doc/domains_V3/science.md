[TOC]

### 领域名称
1. science

### 意图列表

| Domain    | Intent            | Description                         |
| ----------| ----------------- | ----------------------------------- |
| science   | calculator        | 科学计算                             |
| science   | unit_convert      | 单位转换                             |

### 数据示例
##### 纯文本模版

```json
/*
 * 纯文本模版
 * @domain: science
 * @intent: calculator
 * 语料：1+1等于几
 * BOT：格力空调 (8d3b6076-3bb4-4c26-89c3-011447996044)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "1+1=2",
	"strSpeakTipsText": "1加1等于2"
}
// ======================= Json 数据 =======================
{
    "baseInfo": {
        "skillIcon": "", 
        "skillName": "science"
    }, 
    "controlInfo": {
        "audioConsole": "false", 
        "orientation": "portrait", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "selfData": {
                "iRet": 0, 
                "sFormula": "1+1=2", 
                "sResult": "2"
            }, 
            "textContent": "1加1等于2", 
            "title": "1+1=2"
        }
    ]
}

/*
 * 纯文本模版
 * @domain: science
 * @intent: unit_convert
 * 语料：80厘米等于多少米
 * BOT：格力空调 (8d3b6076-3bb4-4c26-89c3-011447996044)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "80厘米等于0.8米",
	"strSpeakTipsText": "80厘米等于0.8米"
}
```