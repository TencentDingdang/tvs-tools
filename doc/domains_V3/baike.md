[TOC]

### 领域名称

百科服务

### 意图列表

| Intent       | Description |
| ------------ | ----------- |
| search_baike | 百科        |
| search_more  | 更多百科    |

### 数据示例

##### search_baike、search_more纯文本模版

```json
/*
 * search_person 纯文本模版
 * 语料：张三是谁
 * BOT：410音响 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": "http://baike.sogou.com/v101204096.htm"
    }, 
    "listItems": [
        {
            "htmlView": "", 
            "image": {
                "contentDescription": "", 
                "sources": [ ]
            }, 
            "mediaId": "101204096", 
            "selfData": "", 
            "textContent": "东北地区用张三指代狼    张三，中国人最耳熟能详的名字。张三可能真有其人，但更多时候与 李四、 王五一起指代不特定的某个人，揶揄或者概括常用。例如古代说书人常说：那张三的李四的都来了。也常被用在文学影视作品中。因此名平常普通，近来也被用来指代一个普通人群体，即“ 张三族”。", 
            "title": "张三"
        }
    ]
    }
}
```

#####search_baike、search_more图文模版

```json
/*
 * search_today 纯文本模版
 * 语料：刘德华是谁
 * BOT：410音响 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "GRAPHIC"
    }, 
    "globalInfo": {
        "seeMore": "http://baike.sogou.com/v4962641.htm"
    }, 
    "listItems": [
        {
            "htmlView": "", 
            "image": {
                "contentDescription": "刘德华", 
                "sources": [
                    {
                        "heightPixels": 0, 
                        "size": "", 
                        "url": "https://pic.baike.soso.com/ugc/baikepic2/11447/cut-20171027101245-1817512049_jpg_292_365_11299.jpg/300", 
                        "widthPixels": 0
                    }
                ]
            }, 
            "mediaId": "4962641", 
            "selfData": "", 
            "textContent": "刘德华（Andy ），1961年9月27日出生于中国香港，演员、歌手、作词人、制片人。1981年出演电影处女作《彩云曲》。1983年主演的武侠剧《神雕侠侣》在香港获得62点的收视纪录。1985年发行首张个人专辑《只知道此刻爱你》。1990年凭借专辑《可不可以》在歌坛获得关注。1991年创办天幕电影公司。1992年，凭借传记片《五亿探长雷洛传》获得第11届香港电影金像奖最佳男主角提名。1994年创立刘德华慈善基金会。2004年凭借警匪片《无间道3：终极无间》获得第41届台湾金马奖最佳男主角奖。2011年主演剧情片《桃姐》，并凭借该片先后获得台湾金马奖最佳男主角奖、香港电影金像奖最佳男主角奖；同年担任第49届台湾电影金马奖评审团主席。2000年被《吉尼斯世界纪录大全》评为“获奖最多的香港男歌手”。2004年第六次获得十大劲歌金曲最受欢迎男歌星奖。2008年被委任为香港非官守太平绅士。2016年参与填词的歌曲《原谅我》正式发行。2017年，出演电影《追龙》。2018年2月，凭借《拆弹专家》获第37届香港电影金像奖最佳男主角提名。", 
            "title": "刘德华"
        }
    ]
}
```

