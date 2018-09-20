[TOC]

### 领域名称

视频

### 意图列表

| Intent              | Description                         |
| ------------------  | ----------------------------------- |
| search_cartoon      | 看动画                              |
| search_film         | 看电影                              |
| search_tvseries     | 看电视剧                            |
| search_show         | 看综艺                              |
| search_short_video  | 看小视频                            |
| ------------------  | ----------------------------------- |
| open_xxx            | 打开腾讯视频、打开小企鹅            |
| next_page           | 下一页                              |
| prev_page           | 上一页                              |
| play_located        | 指定位置播放                        |
| fullscreen          | 全屏                                |
| low_definition      | 低画质播放                          |
| high_definition     | 高画质播放                          |
| back                | 返回                                |
| next                | 下一个                              |
| prev                | 上一个                              |
| replay              | 重播                                |
| play_by_episode     | 播第几集                            |
| double_speed        | 倍速播放                            |
| back_tvhomepage     | 返回主页                            |
| fullscreen          | 全屏                                |
| index_v2            | 第几个                              |
| close               | 退出                                |
| search_video_by_person | 搜索                             |
| resume              | 继续播放                            |
| fast_forward        | 快进                                |
| fast_reverse        | 快退                                |
| fast_backward       | 快退                                |

### 数据示例 for 410

##### play search_cartoon 等意图，打开小企鹅

```json
/*
 * play play_album 等意图，音频类模版
 * 语料：来点音乐
 * BOT：410音箱 (2b82efec-a77c-46cd-a2c2-8df9bbd1d1c3)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "小板凳搬好，一起来看小猪佩奇咯。",
	"strSpeakTipsText": "小板凳搬好，一起来看小猪佩奇咯。"
}
// ======================= 小企鹅 Json 数据 =======================
{
    "baseInfo":{
        "skillName":"小企鹅乐园"                      //技能名称
    },
    "controlInfo":{
        "textSpeak":"false",                          //默认不播报
        "type":"URI"                                  //uri卡片类型
    },
    "globalInfo":{
        "selfData":{
            "action":"android.intent.action.VIEW",    //action
            "actionParam":{                           //action参数

            },
            "isApp":"true",                           //是本地app
            "operType":"activity",                    //avtivity方式
            "packageName":"com.tencent.qqlivekid"     //包名
        }
    },
    "uriInfo":{
        "ui":{                                        //控制指令
            "url":"qqlivekid://v.qq.com/JumpAction?cht=5&ext=%7B%22cid%22:%22uqt7am9f9dmvoss%22%7D&jump_source=QROBOT"
        }
    }
}

// ======================= 腾讯视频 Json 数据 =======================
{
    "baseInfo":{
        "skillName":"腾讯视频"
    },
    "controlInfo":{
        "textSpeak":"false",
        "type":"URI"
    },
    "globalInfo":{
        "selfData":{
            "action":"com.ktcp.aiagent.voice.trigger",
            "actionParam":{

            },
            "isApp":"true",
            "operType":"broadcast",
            "packageName":"com.ktcp.aiagent"
        }
    },
    "uriInfo":{
        "ui":{
            "url":""
        }
    }
}
```
##### search_film 视频模版 for QB智能助手

```json
/*
 * search_film search_cartoon search_tvseries search_show 视频模版
 * 语料：我要看谍影重重
 * BOT：QB智能助手 (69156881-10bb-40dd-92e0-db5329b044dc)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "找到了以下在线电影",
	"strSpeakTipsText": "找到了以下在线电影"
}
// ======================= Json 数据 =======================
{
    "baseInfo":{
        "skillName":"叮当视频"                        //技能名称
    },
    "controlInfo":{
        "textSpeak":"false",                          //默认不播报
        "type":"VIDEO"                                //视频卡片类型
    },
	
    "listItems":[
        {
            "htmlView":"",
            "image":{                                 // 剧照图片
                "sources":[ 
                    {
                        "url":"http://cdn.read.html5.qq.com/image?src=video_hot&q=5&h=411&w=312&r=0&imageUrl=http%3A%2F%2Fi%2Egtimg%2Ecn%2Fqqlive%2Fimg%2Fjpgcache%2Ffiles%2Fqqvideo%2Fl%2Flvxqk7s7yynbdba%5Fl%2Ejpg"
                    }
                ]
            },
            "mediaId":"3769497",                      // 媒体ID
            "selfData":{
                "actor":[                             // 演员列表
                    "朱丽娅·斯蒂尔斯",
                    "汤米·李·琼斯",
                    "艾丽西亚·维坎德",
                    "马特·达蒙"
                ],
                "area":"美国",                        // 地区
                "curSetNum":"3_1",                    // 当前剧集
                "director":[                          // 导演列表
                    "保罗·格林格拉斯"
                ],
                "nickName":"",                        // 别名
                "score":"0.0",                        // 评分
                "sourceIcon":"",                      // 图标
                "sourceName":"",                      // 来源
                "subType":"0-其他",                   // 子类型
                "tag":[                               // 标签

                ],
                "toTalSetNum":"3_1",                  // 总剧集
                "type":"电影",                        // 类型
                "videoType":1,                        // 视频类型
                "viewCount":"2",                      // 
                "year":"2016"                         // 发布年
            },
            "textContent":"",
            "title":"谍影重重5",                      // 名称
            "video":{
                "metadata":{
                    "totalMilliseconds":0             // 时间
                },
                "sources":[
                    {
                        "size":"",
                        "url":"http://v.html5.qq.com/?ch=001411#p=detail&vId=3769497&vType=1" //播放链接
                    }
                ]
            }
        },
        {
            "htmlView":"",
            "image":{
                "sources":[
                    {
                        "url":"http://cdn.read.html5.qq.com/image?src=video_hot&q=5&h=411&w=312&r=0&imageUrl=http%3A%2F%2F3img%2Emgtv%2Ecom%2Fpreview%2Finternettv%2Fsp%5Fimages%2Fott%2F2016%2Fdianying%2F8846%2F20160702220244252%2Dnew%2Ejpg"
                    }
                ]
            },
            "mediaId":"1111925",
            "selfData":{
                "actor":[
                    "克里夫·欧文",
                    "弗兰卡·波坦特",
                    "朱丽娅·斯蒂尔斯",
                    "马特·达蒙"
                ],
                "area":"美国",
                "curSetNum":"14_1,25_1",
                "director":[
                    "道格·李曼",
                    "道格·里曼"
                ],
                "nickName":"",
                "score":"8.4",
                "sourceIcon":"",
                "sourceName":"",
                "subType":"|冒险|动作|悬疑|惊悚",
                "tag":[

                ],
                "toTalSetNum":"14_1,25_1",
                "type":"电影",
                "videoType":1,
                "viewCount":"1",
                "year":"2002"
            },
            "textContent":"",
            "title":"谍影重重英语BD",
            "video":{
                "metadata":{
                    "totalMilliseconds":0
                },
                "sources":[
                    {
                        "size":"",
                        "url":"http://v.html5.qq.com/?ch=001411#p=detail&vId=1111925&vType=1"
                    }
                ]
            }
        }
    ]
}
```
