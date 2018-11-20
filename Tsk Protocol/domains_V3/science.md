[TOC]

### 领域名称
science

### 意图列表
| Domain    | Intent             | Description                         |
| ----------| ------------------ | ----------------------------------- |
| science   | calculator         | 科学计算                             |
| science   | unit_convert       | 单位转换                             |
| science   | unit_search        | 单位查询                             |
| science   | unit_convert_howto | 单位转换帮助                          |

### 数据示例
#### 纯文本模版
| Domain    | Intent             | Description                         |
| ----------| ------------------ | ----------------------------------- |
| science   | calculator         | 科学计算                             |
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
	"strTipsText": "",
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
        "textSpeak": "false", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "selfData": {
                "iRet": 0, 
                "sFormula": "1+1", 
                "sResult": "2"
            }, 
            "textContent": "1加1等于2", 
            "title": "1+1=2"
        }
    ]
}
```
| Domain    | Intent             | Description                         |
| ----------| ------------------ | ----------------------------------- |
| science   | unit_convert       | 单位转换                             |
```json
/*
 * 纯文本模版
 * @domain: science
 * @intent: unit_convert
 * 语料：80厘米等于多少米
 * BOT：格力空调 (8d3b6076-3bb4-4c26-89c3-011447996044)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": "80厘米等于0.8米"
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
        "textSpeak": "false", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "80厘米等于0.8米", 
            "title": ""
        }
    ]
}
```
| Domain    | Intent             | Description                         |
| ----------| ------------------ | ----------------------------------- |
| science   | unit_search        | 单位查询                             |
```json
/*
 * 纯文本模版
 * @domain: science
 * @intent: unit_search
 * 语料：光年是什么单位
 * BOT：格力空调 (8d3b6076-3bb4-4c26-89c3-011447996044)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": "光年是长度的单位"
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
        "textSpeak": "false", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "光年是长度的单位", 
            "title": ""
        }
    ]
}
```
| Domain    | Intent             | Description                         |
| ----------| ------------------ | ----------------------------------- |
| science   | unit_convert_howto | 单位转换帮助                          |
```json
/*
 * 纯文本模版
 * @domain: science
 * @intent: unit_convert_howto
 * 语料：帮我计算一下单位
 * BOT：格力空调 (8d3b6076-3bb4-4c26-89c3-011447996044)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": "我支持长度、时间、面积等单位换算，你想换算什么单位呢？"
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
        "textSpeak": "false", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "我支持长度、时间、面积等单位换算，你想换算什么单位呢？", 
            "title": ""
        }
    ]
}
```