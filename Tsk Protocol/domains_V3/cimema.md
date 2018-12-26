[TOC]

### 领域名称

院线

### 意图列表

| Intent | Description                         |语料|
| ------ | ----------------------------------- |----------------------------------- |
| film_search   | 最近上映的电影 |最近热门的电影|
| cinema_search   | 附近的电影院 |腾讯大厦附近的电影院|




### 数据示例
最近上映的电影
附近的电影院
##### cinema

```json
/*
 * film_search
 * 语料：最近上映的电影
 * 
*/ 
 {
        "jsonData": {
            "controlInfo": {
                 "textSpeak": "false",                         //默认不播报 
                "type": "GRAPHIC",                            //图文卡片
                "version": "1.0.0"                            //版本
            }, 
            "globalInfo": {
                "seeMore": "https://m.ctrip.com/webapp/train/v2/index.html?page=list&dstation=北京&astation=深圳&ddate=2018-08-24&allianceid=317332&sid=896292",    //查看更多url
            }, 
            "listItems": [
               {
                "title":"无名之辈",								// 标题，默认呈现和播报
                "textContent":"陈建斌,任素汐,潘斌龙",					// 内容，默认呈现和播报
                "image":{
                     "sources":[
                        {
                        "url":"http://p0.meituan.net/100.100/movie/3e7696319c840d4890e947b926259d532809641.jpg",
                        "size":"SMALL",							// X_SMALL/SMALL/MEDIUM/LARGE/X_LARGE
                        "widthPixels": 720,
                        "heightPixels": 480
                        },
                    ]
                },
                "htmlView":"http://m.maoyan.com/movie/1208282?_v_=yes",
                }
                //...
            ]
        }
```

```json
/*
 * film_search
 * 语料：附近的电影院
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
                "seeMore": "http://m.maoyan.com/?type=cinema&_v_=yes&lat=22.54351329&lng=113.9296344",    //查看更多url
            }, 
            "listItems": [
              {
                "title":"中影德金影城(南山店)",								// 标题，默认呈现和播报
                "textContent":"0.17km",					// 内容，默认呈现和播报
                "htmlView":"http://m.maoyan.com/shows/16597?_v_=yes"
              }
              //....
            ]
        }
```
