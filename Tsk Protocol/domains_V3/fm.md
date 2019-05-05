[TOC]

### 领域名称

电台

### 意图列表

| Intent                 | Description                  |
| ---------------------- | ---------------------------- |
| play                   | 查询电台                      |
| search_album          | 搜索专辑                      |
| play_radio             | 查询广播                   |
|search_radio             | 搜索广播                   |

### 数据示例

##### 全意图 图文模版

```json
/*
 * 全意图 音频模版
 * 语料：我要听凯叔的故事
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "没问题，来听听这些内容吧。",
	"strSpeakTipsText": "没问题，来听听这些内容吧。"
}
// ======================= Json 数据 =======================
 {
        "jsonData": {
            "baseInfo": {
                "skillIcon": "", 
                "skillName": ""
            }, 
            "controlInfo": {
                "audioConsole": "false", 
                "textSpeak": "false", 
                "type": "AUDIO"
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
                "seeMore": "", 
                "selfData": {
                    "displayFormat": 1, 
                    "subService": 2
                }
            }, 
            "listItems": [
                {
                    "audio": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 430
                        }, 
                        "stream": {
                            "url": "http://ws.stream.fm.qq.com/R196003rmCXB20cppu.m4a?fromtag=36&guid=1532712056&vkey=392E5D684C4C269D33D1BA173C3504EC06142EAF2ACEC2CB4C071998215915353CD1BA9B67A34ABCD385A372B3476AC116F2A44695C49A4C"
                        }
                    }, 
                    "htmlView": "", 
                    "image": {
                        "contentDescription": "", 
                        "sources": [
                            {
                                "heightPixels": 0, 
                                "size": "", 
                                "url": "http://imgcache.qq.com/fm/photo/album/rmid_album_360/L/9/003ppF4W3h4FL9.jpg?time=1506449701", 
                                "widthPixels": 0
                            }
                        ]
                    }, 
                    "mediaId": "1_rd003rmCXB20cppu", 
                    "selfData": {
                        "iAccurateMatch": 1, 
                        "iLine": 1, 
                        "iOffSet": 0, 
                        "iPlayCount": 0, 
                        "iShowNum": 19, 
                        "lUpdateTime": 0, 
                        "sAlbum": "凯叔讲故事", 
                        "sAlbumId": "1_rd003ppF4W3h4FL9", 
                        "sAnchor": "企鹅FM童话频道", 
                        "sArea": "", 
                        "sShowName": "第一次提问", 
                        "sSource": "企鹅FM", 
                        "vLive": [ ]
                    }, 
                    "textContent": "凯叔讲故事", 
                    "title": "第一次提问", 
                    "video": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 0
                        }, 
                        "sources": [ ]
                    }
                }, 
                {
                    "audio": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 610
                        }, 
                        "stream": {
                            "url": "http://ws.stream.fm.qq.com/R196003pOEZl1hlDpu.m4a?fromtag=36&guid=1532712056&vkey=0E76A331652A2E19F506D8783C62D5B48F258B42A1AF8E4ED0888238A87D06C5F8FF1C36C0DFCF8328772061F8438D5AED2464DFD2E1126C"
                        }
                    }, 
                    "htmlView": "", 
                    "image": {
                        "contentDescription": "", 
                        "sources": [
                            {
                                "heightPixels": 0, 
                                "size": "", 
                                "url": "http://imgcache.qq.com/fm/photo/album/rmid_album_360/L/9/003ppF4W3h4FL9.jpg?time=1506449701", 
                                "widthPixels": 0
                            }
                        ]
                    }, 
                    "mediaId": "1_rd003pOEZl1hlDpu", 
                    "selfData": {
                        "iAccurateMatch": 1, 
                        "iLine": 8, 
                        "iOffSet": 0, 
                        "iPlayCount": 0, 
                        "iShowNum": 19, 
                        "lUpdateTime": 0, 
                        "sAlbum": "凯叔讲故事", 
                        "sAlbumId": "1_rd003ppF4W3h4FL9", 
                        "sAnchor": "企鹅FM童话频道", 
                        "sArea": "", 
                        "sShowName": "好安静的蟋蟀", 
                        "sSource": "企鹅FM", 
                        "vLive": [ ]
                    }, 
                    "textContent": "凯叔讲故事", 
                    "title": "好安静的蟋蟀", 
                    "video": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 0
                        }, 
                        "sources": [ ]
                    }
                }, 
                {
                    "audio": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 1022
                        }, 
                        "stream": {
                            "url": "http://ws.stream.fm.qq.com/R196001xD6PE23BQeR.m4a?fromtag=36&guid=1532712056&vkey=B290B898094658BF40C21583142F4D7AB0EC9634F41B65178CAC0E101566386B4505B2DE6E6E6891CFCDA5B44EB15FA138D1CD5D33152A87"
                        }
                    }, 
                    "htmlView": "", 
                    "image": {
                        "contentDescription": "", 
                        "sources": [
                            {
                                "heightPixels": 0, 
                                "size": "", 
                                "url": "http://imgcache.qq.com/fm/photo/album/rmid_album_360/L/9/003ppF4W3h4FL9.jpg?time=1506449701", 
                                "widthPixels": 0
                            }
                        ]
                    }, 
                    "mediaId": "1_rd001xD6PE23BQeR", 
                    "selfData": {
                        "iAccurateMatch": 1, 
                        "iLine": 10, 
                        "iOffSet": 0, 
                        "iPlayCount": 0, 
                        "iShowNum": 19, 
                        "lUpdateTime": 0, 
                        "sAlbum": "凯叔讲故事", 
                        "sAlbumId": "1_rd003ppF4W3h4FL9", 
                        "sAnchor": "企鹅FM童话频道", 
                        "sArea": "", 
                        "sShowName": "自行车蚊子埃贡", 
                        "sSource": "企鹅FM", 
                        "vLive": [ ]
                    }, 
                    "textContent": "凯叔讲故事", 
                    "title": "自行车蚊子埃贡", 
                    "video": {
                        "metadata": {
                            "offsetInMilliseconds": 0, 
                            "totalMilliseconds": 0
                        }, 
                        "sources": [ ]
                    }
                }
            ]
        }
```

