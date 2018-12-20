[TOC]

### 领域名称

航班动态

### 意图列表

| Intent | Description                         |语料|
| ------ | ----------------------------------- |----------------------------------- |
| search_schedule   | MF1234什么时候起飞 |MF1234航班什么时候降落
| search_status   | MF1234航班晚点了吗 
| search_boarding  | MF1234的登机口
| search_checkin   | MF1234的值机口




### 数据示例
MF1234什么时候起飞
MF1234航班晚点了吗
MF1234的登机口
MF1234的值机口
##### flight

```json
/*
 * search_schedule
 * 语料：MF1234什么时候起飞
 * 
*/ 
 {
        "jsonData": {
            "controlInfo": {
                "textSpeak": "false",                         //默认不播报 
                "type": "TEXT",                            //图文卡片
                "version": "1.0.0"                            //版本
            }, 
            "globalInfo": {
                "seeMore": "http://www.variflight.com/h5/details?AE71649A58c77&token=9540f38ba5ddd0a912c6546beaebcfc1&fnum=MF1234&n_calendar=2018-11-30",    //查看更多url
            }, 
            "listItems": [
              {
                "textContent":"厦门航空MF1234航班计划于今天晚上10点40分从常州奔牛机场起飞",					// 内容，默认呈现和播报
              }
              //....
            ]
        }
```

```json
/*
 * search_status
 * 语料：MF1234航班晚点了吗
 * 
*/ 
 {
        "jsonData": {
            "controlInfo": {
                "textSpeak": "false",                         //默认不播报 
                "type": "TEXT",                            //图文卡片
                "version": "1.0.0"                            //版本
            }, 
            "globalInfo": {
                "seeMore": "http://www.variflight.com/h5/details?AE71649A58c77&token=9540f38ba5ddd0a912c6546beaebcfc1&fnum=MF1234&n_calendar=2018-11-30",    //查看更多url
            }, 
            "listItems": [
              {
                "textContent":"厦门航空MF1234号航班目前处于计划状态",					// 内容，默认呈现和播报
              }
              //....
            ]
        }
```

```json
/*
 * search_status
 * 语料：search_boarding
 * 
*/ 
 {
        "jsonData": {
            "controlInfo": {
                "textSpeak": "false",                         //默认不播报 
                "type": "TEXT",                            //图文卡片
                "version": "1.0.0"                            //版本
            }, 
            "globalInfo": {
                "seeMore": "http://www.variflight.com/h5/details?AE71649A58c77&token=9540f38ba5ddd0a912c6546beaebcfc1&fnum=MF1234&n_calendar=2018-11-30",    //查看更多url
            }, 
            "listItems": [
              {
                "textContent":"从常州飞往深圳的厦门航空MF1234号航班登机口信息尚未公布",					// 内容，默认呈现和播报
              }
              //....
            ]
        }
```

```json
/*
 * search_checkin
 * 语料：MF1234的值机口
 * 
*/ 
 {
        "jsonData": {
            "controlInfo": {
                "textSpeak": "false",                         //默认不播报 
                "type": "TEXT",                            //图文卡片
                "version": "1.0.0"                            //版本
            }, 
            "globalInfo": {
                "seeMore": "http://www.variflight.com/h5/details?AE71649A58c77&token=9540f38ba5ddd0a912c6546beaebcfc1&fnum=MF1234&n_calendar=2018-11-30",    //查看更多url
            }, 
            "listItems": [
              {
                "textContent":"从常州飞往深圳的厦门航空MF1234号航班在14-24柜台办理值机",					// 内容，默认呈现和播报
              }
              //....
            ]
        }
```