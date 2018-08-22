[TOC]

### 领域名称

成语

### 意图列表

| Intent                  | Description  |
| ----------------------- | ------------ |
| search_chengyu          | 查询成语含义       |
| search_chengyu_from     | 查询成语出处       |
| search_chengyu_same     | 查询成语的同义词/近义词 |
| search_chengyu_opposite | 查询成语的反义词     |
| search_chengyu_sentence | 查询成语如何造句     |
| search_chengyu_story    | 查询成语背后的故事    |
| search_chengyu_pos      | 查询成语的词性      |
| search_chengyu_spell    | 查询成语的拼音      |

### 数据示例

##### 纯文本模版

| Intent                  | Description  |
| ----------------------- | ------------ |
| search_chengyu          | 查询成语含义       |
| search_chengyu_story    | 查询成语背后的故事    |

```json
/*
 * 纯文本模版 (1)
 * 语料：意气风发什么意思
 * BOT：腾讯叮当App (ad415e3e-643c-489a-88ca-3fda41f976c1)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "找到了以下相关内容：",
	"strSpeakTipsText": "找到了以下相关内容："
}
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"textSpeak": "true", 
		"type": "TEXT"
	}, 
	"listItems": [
		{
			"htmlView": "http://hanyu.baidu.com/s?wd=意气风发&ptype=zici", 
			"mediaId": "c4fb48bd9d75325c8a391a27e53b7881", 
			"selfData": {
			    "interpretation": "意气：意志和气概；风发：像风吹一样迅猛。形容精神振奋，气概豪迈。", 
			    "pinyin": "[yì qì fēng fā]"
			}, 
			"textContent": "意气：意志和气概；风发：像风吹一样迅猛。形容精神振奋，气概豪迈。", 
			"title": "意气风发"
		}
	]
}
```

##### 纯文本模版 (2)

| Intent                  | Description  |
| ----------------------- | ------------ |
| search_chengyu_from     | 查询成语出处       |
| search_chengyu_same     | 查询成语的同义词/近义词 |
| search_chengyu_opposite | 查询成语的反义词     |
| search_chengyu_sentence | 查询成语如何造句    |
| search_chengyu_pos      | 查询成语的词性      |
| search_chengyu_spell    | 查询成语的拼音      |

```json
/*
 * 纯文本模版
 * 语料：掩耳盗铃反义词
 * BOT：TCL_MS838A (4297b1f0859111e882ea654a97ef9d8a)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": ""
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "true", 
        "orientation": "portrait", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "htmlView": "", 
            "mediaId": "", 
            "selfData": {
                "interpretation": "", 
                "pinyin": ""
            }, 
            "textContent": "开诚布公", 
            "title": ""
        }
    ]
}
```
