[TOC]

### 领域名称

帮助与引导

### 意图列表

| Intent | Description |
| ------ | ----------- |
| cando  | 会做什么、列举上线服务 |

### 数据示例
##### cando 文本模版
```json
/*
 * cando 该意图仅有回复语
 * 语料：讲个笑话
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ---------------------- 回复语 -----------------------
{
   "strTipsText": "",
   "strSpeakTipsText": "我能做很多事情，比如播新闻，查天气，查股票。"
}
// ---------------------- json 数据 -----------------------
{
    "controlInfo": {
        "audioConsole": "true", 
        "orientation": "portrait", 
        "textSpeak": "false", 
        "titleSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "我可是腾讯叮当，你的智能助手，播视频、查新闻、视频通话，都是我的强项。"
        }
    ]
}
```

