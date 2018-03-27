# 音乐
### music.*
#### 问法
我想听刘德华的歌
#### JSON
```json
{
    "eDisplayFormat": 1,//终端展示形式
    "eRetCode": 0,//返回码
    "eSubService": 1,//music子服务 音乐服务返回都是1
    "exstr": "",//回带终端请求时上报的预留字段
    "sSpeak": "为你找到刘德华的这些歌",//语音语句
    "sText": "为你找到刘德华的这些歌",//显示语句
    "stMedia": {//音乐相关数据
        "vActionList": [
            {//当前播放
                "eActionType": 3,//执行的动作 3播放;4 播放列表；对于播放类意图会有两个list一个是当前播放，一个是列表
                "vMediaDataList": [
                    {
                        "sAlbum": "Unforgettable 中国巡回演唱会2011",//专辑
                        "sAlbumPic": "http://y.gtimg.cn/music/photo_new/T002R120x120M000000b79wf3pGa96.jpg",//专辑封面图片的url
                        "sAlbumPubTime": "",//专辑发行时间
                        "sH5Url": "http://i.y.qq.com/v8/playsong.html?songid=1136752",//音乐的H5页面
                        "sMedia": "忘情水",//歌曲名称
                        "sMediaId": "1136752",//歌曲id
                        "sMediaRichname": "",//音乐richname（带有live标识） 终端不需关注
                        "sPerson": "刘德华",//歌手名称
                        "sSource": "QQ音乐",//媒体来源
                        "sUrl": "http://isure.stream.qqmusic.qq.com/C600003bBcS60NhwdR.m4a?vkey=153A7090C6D18CD7201290ADB9323DD4B7AEC097F05CCA0E0A51805A7CA2801829DE7EF0D199903BB49E02A9AE604D8E2CFD4B6D89FD9079&guid=1234727204&fromtag=50&uin=1152921504732322084"//播放地址
                    }
                ]
            },
            {//当前播放列表
                "eActionType": 4,//执行的动作 4播放列表
                "vMediaDataList": [
                    {
                        "sAlbum": "Unforgettable 中国巡回演唱会2011",
                        "sAlbumPic": "http://y.gtimg.cn/music/photo_new/T002R120x120M000000b79wf3pGa96.jpg",
                        "sAlbumPubTime": "",
                        "sH5Url": "http://i.y.qq.com/v8/playsong.html?songid=1136752",
                        "sMedia": "忘情水",
                        "sMediaId": "1136752",
                        "sMediaRichname": "",
                        "sPerson": "刘德华",
                        "sSource": "QQ音乐",
                        "sUrl": "http://isure.stream.qqmusic.qq.com/C600003bBcS60NhwdR.m4a?vkey=153A7090C6D18CD7201290ADB9323DD4B7AEC097F05CCA0E0A51805A7CA2801829DE7EF0D199903BB49E02A9AE604D8E2CFD4B6D89FD9079&guid=1234727204&fromtag=50&uin=1152921504732322084"
                    },
                    {
                        "sAlbum": "Unforgettable 中国巡回演唱会2011",
                        "sAlbumPic": "http://y.gtimg.cn/music/photo_new/T002R120x120M000000b79wf3pGa96.jpg",
                        "sAlbumPubTime": "",
                        "sH5Url": "http://i.y.qq.com/v8/playsong.html?songid=1136761",
                        "sMedia": "凭什么",
                        "sMediaId": "1136761",
                        "sMediaRichname": "",
                        "sPerson": "刘德华",
                        "sSource": "QQ音乐",
                        "sUrl": "http://isure.stream.qqmusic.qq.com/C600001oC8vq2jowhf.m4a?vkey=34819D39A907A9A1E1ABE275D640E3087A942D1420E888C2EC375804075B7FEC280F24B0408B45012B9DF48496964D4E27B6FC751F5BD511&guid=1234727204&fromtag=50&uin=1152921504732322084"
                    }
                ]
            }
        ]
    },
    //strJsonToSemantic 为给语义的数据终端不需要关注
    "strJsonToSemantic": "{\"params\":[{\"entity_type\":\"sys.music.singer\",\"name\":\"singer\",\"values\":[\"刘德华\"]},{\"entity_type\":\"sys.music.song\",\"name\":\"song\",\"values\":[\"忘情水\"]},{\"entity_type\":\"sys.music.album\",\"name\":\"album\",\"values\":[\"Unforgettable 中国巡回演唱会2011\"]}]}\n",
    "ePlayMode":0,//播放方式 0由终端控制，1随机，2顺序，3单曲循环，4循环播放，5单曲模式
    "iContainCode":1,//用于音乐服务上层的统计，终端不用关注
    "vecNotifyInfo":"",//返回给音乐服务上层的json结构，终端不用关注
    "eAIRetCode":0,//返回的错误码 0是正确，-100调用外部接口错误，-3调用dcache错误,-2调用mdb错误，-1,默认错误,抛出异常时使用
                   //1无数据返回,2无登录态,3参数校验失败,4功能不支持,100自定义业务返回.
}
```