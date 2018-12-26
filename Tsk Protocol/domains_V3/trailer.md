[TOC]

### 领域名称

电视节目单

### 意图列表

| Intent           | Description                         |
| ---------------- | ----------------------------------- |
| search_tvlist    | 湖南卫视有什么电视节目              |
| search_time      | 快乐大本营什么时候播                |
| search_channel   | 快乐大本营什么时候播                |
| remind_program   | 快乐大本营什么时候播                |
| switch_channel   | 快乐大本营什么时候播                |

### 数据示例

##### search_tvlist search_time search_channel 图文类模版

```json
/*
 * search_tvlist search_time search_channel 图文类模版
 * 语料：湖南卫视有什么电视节目
 * BOT：QB智能助手 (69156881-10bb-40dd-92e0-db5329b044dc)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "下面是湖南卫视今天的电视节目:",
	"strSpeakTipsText": "15:39 偶像独播剧场:因为爱情有晴天(30)
16:18 嘿!好样的
17:56 新闻大求真
18:30 湖南新闻联播
18:56 卫视气象站
19:00 转播中央台新闻联播
19:34 生机无限
20:06 金鹰独播剧场:温暖的弦(43)
21:07 金鹰独播剧场:温暖的弦(44)
22:00 嘿!好样的
23:30 我想和你唱"
}
// ======================= Json 数据 =======================
{
    "baseInfo":{
        "skillName":"tvmao"
    },
    "controlInfo":{
        "textSpeak":"false",
        "type":"GRAPHIC"
    },
    "globalInfo":{
        "seeMore":"http://m.tvmao.com/program/HUNANTV-HUNANTV1-w4.html"
    },
    "listItems":[
        {
            "image":{
                "sources":[
                    {
                        "url":"http://softfile.3g.qq.com/myapp/soft_imtt/tvprogram/267bcb6711b15993a9a3af72123527bc.jpg"
                    }
                ]
            },
            "selfData":{
                "ChLogo":"http://softfile.3g.qq.com/myapp/soft_imtt/tvprogram/7fda3f934f038c523a4b2ec3d87bf1b1.png",
                "TVName":"偶像独播剧场:因为爱情有晴天(30)",
                "channel":"湖南卫视",
                "channelType":0,
                "date":"2018-05-24",
                "endTime":"2018-05-24 16:18",
                "episode":30,
                "hot":16,
                "isPlaying":1,
                "playType":0,
                "thumb":"http://softfile.3g.qq.com/myapp/soft_imtt/tvprogram/267bcb6711b15993a9a3af72123527bc.jpg",
                "time":"15:39",
                "weekPrint":"周四"
            },
            "textContent":"2018-05-24 15:39",
            "title":"湖南卫视 偶像独播剧场:因为爱情有晴天(30)"
        }
    ]
}
```

##### search_tvlist search_time search_channel 纯文本模版

```json
/*
 * search_tvlist search_time search_channel 纯文本模版
 * 语料：电视节目
 * BOT：QB智能助手 (69156881-10bb-40dd-92e0-db5329b044dc)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "你需要说出某个频道，可以跟我说“湖南卫视今天的节目单”",
	"strSpeakTipsText": "你需要说出某个频道，可以跟我说“湖南卫视今天的节目单”"
}
// ======================= Json 数据 =======================
{
	"baseInfo": {
		"skillName": "tvmao"
	},
	"controlInfo": {
		"textSpeak": "false",
		"type": "TEXT"
	},
	"globalInfo": {
		"seeMore": ""
	},
	"listItems": [{
		"image": {
			"sources": []
		},
		"selfData": "",
		"textContent": "",
		"title": "你需要说出某个频道，可以跟我说“湖南卫视今天的节目单”"
	}]
}
```
