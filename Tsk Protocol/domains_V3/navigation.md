[TOC]

### 领域名称
路况

### 意图列表

| Intent | Description                         |语料|
| ------ | ----------------------------------- |----------------------------------- |
| ask_distance_time   | 腾讯大厦到海岸城要多久 |


### 数据示例
腾讯大厦到海岸城要多久
##### navigation

```json
/*
 * ask_distance_time
 * 语料：腾讯大厦到海岸城要多久
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
                "seeMore": "",    //查看更多url
            }, 
            "listItems": [
              {
                "textContent":"腾讯大厦离海岸城4.4公里，开车大概需要11分钟",					// 内容，默认呈现和播报
              }
              //....
            ]
        }
```