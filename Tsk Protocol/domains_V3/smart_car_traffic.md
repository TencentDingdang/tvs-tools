 [TOC]

### 领域名称
路况

### 意图列表

| Intent | Description                         |语料|
| ------ | ----------------------------------- |----------------------------------- |
| query_route_traffic   | 腾讯大厦到海岸城堵不堵 |


### 数据示例
腾讯大厦到海岸城堵不堵
##### smart_car_traffic

```json
/*
 * query_route_traffic
 * 语料：腾讯大厦到海岸城堵不堵
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
                "textContent":"从腾讯大厦到海岸城现在一路通畅。开车从南海大道经过滨海南海立交桥到达目的地，大概需要12分钟"				// 内容，默认呈现和播报
              }
              //....
            ]
        }
```