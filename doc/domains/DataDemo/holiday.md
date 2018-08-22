[TOC]

### 领域名称

时间节日

### 意图列表

| Intent             | Description    |
| ------------------ | -------------- |
| search_festival    | 查节日         |
| search_week        | 查星期         |
| search_solar2lunar | 查公历转农历   |
| search_dateDiff    | 查天数         |
| search_holiday     | 查节日放假安排 |
| search_date        | 查日期         |
| search_time        | 查时间         |

### 数据示例

##### search_festival无模版

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：今天是什么节日
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "今天是世界语创立日。"
        }
    ]
}
```

##### search_week 无模板

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：今天星期几
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "今天是星期四。"
        }
    ]
}
```

##### search_solar2lunar 无模板

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：今天是农历几号
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "今天是农历戊戌年六月十四。"
        }
    ]
}
```

##### search_dateDiff 无模板

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：中秋还有几天
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "现在距离今年中秋9月24日还有60天。"
        }
    ]
}
```

##### search_holiday 无模板

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：中秋放假安排
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "2018年中秋节，从9月22日到9月24日一共放假3天。"
        }
    ]
}
```

##### search_date 无模板

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：今天是几号
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "今天是7月26日，星期四。"
        }
    ]
}
```

##### search_time 无模板

```json
/*
 * translate 该意图仅有回复语 无 Json 数据
 * 语料：现在几点了
 * BOT：410音响
*/ 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "现在是北京时间晚上7点8分。"
        }
    ]
}
```

