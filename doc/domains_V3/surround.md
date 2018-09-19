[TOC]

### 领域名称

查周边

### 意图列表

| Intent                      | Description  |
| --------------------------- | ------------ |
| search		              | 查周边       |

### 数据示例


```json
/*
 * 无模版
 * 语料：附近的银行
 * BOT：410音箱 (2b82efec-a77c-46cd-a2c2-8df9bbd1d1c3)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "为你找到了以下银行", 
    "strSpeakTipsText": "为你找到了以下银行", 
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "false", 
        "textSpeak": "false", 
        "type": "TEXT", 
    }, 
   "globalInfo": {
                "backgroundAudio": {
                    "metadata": {
                        "offsetInMilliseconds": 0, 
                        "totalMilliseconds": 0
                    }, 
                    "stream": {
                        "url": ""
                    }
                }, 
                "backgroundImage": {
                    "contentDescription": "", 
                    "sources": [ ]
                }, 
                "seeMore": "http://apis.map.qq.com/tools/poimarker?type=1&keyword=银行¢er=22.540491104,113.934898376&radius=5000&init_view=2&key=3C3BZ-CJDKR-VCWWH-WPXST-GZTYJ-NBFJG&referer=dobby"
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
                    "htmlView": "http://apis.map.qq.com/uri/v1/marker?marker=coord:22.540279388,113.935417175;title:中国工商银行(深圳高新园中区支行);addr:广东省深圳市南山区深南大道9988号大族科技中心大厦1层;uid:6770461266819681217&referer=dobby", 
                    "image": {
                        "contentDescription": "", 
                        "sources": [ ]
                    }, 
                    "mediaId": "", 
                    "selfData": {
                        "iDistance": 58, 
                        "sCategory": "银行金融:银行", 
                        "sTel": ""
                    }, 
                    "textContent": "广东省深圳市南山区深南大道9988号大族科技中心大厦1层", 
                    "title": "中国工商银行(深圳高新园中区支行)", 
                    "video": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 0
                        }, 
                        "sources": [ ]
                    }
                }, 
    ]
}
```

