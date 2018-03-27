# 电台
### fm.*
#### 问法
播放最新一期罗辑思维
我想听成都交通广播
#### JSON
```json
{
    "eDisplayFormat": 3, //终端展现类型
    "eRetCode": 0,   //返回码
    "eSubService": 2,    //服务类型，2:fm
    "exstr": "",     //扩展字段
    "fmData": {      //在线电台的卡片列表
        "vActionList": [
            {
                "eActionType": 3,  //  0:只展示sText字段。(其他形式中，sText字段也是要展示的) 1:只播放有url的那首，展示这节目的卡片 2: 只展示播放列表，以节目为单位展示 3: 展示专辑列表，需要把返回的节目列表按专辑排重 4:播放有url的那个节目，并且展示播放列表 5:播放有url的那个节目，列表中的都隐藏，只有点击后才展示出来，并且需要去掉正在播放的那个
                "vFmDataList": [
                    {
                        "eShowType": 0,             //0：专辑，1：广播
                        "lUpdateTime": 0,   
                        "sAlbum": "电音狂潮 绝对震撼你的耳朵",  //专辑名字
                        "sAlbumId": "rd002dUZop1eHQ0S",     //专辑id
                        "sAnchor": "Dj嗨小冷",         //主播名
                        "sArea": "",                //地区
                        "sCoverUrl": "http://imgcache.qq.com/fm/photo/album/rmid_album_720/0/S/002dUZop1eHQ0S.jpg?time=1447313988", //图片url
                        "sShowId": "rd002cXH931FF9tO",  //节目id
                        "sShowName": "意大利极品男腔", //节目名字
                        "sSource": "qq",        //节目来源
                        "sUrl": "http://ws.stream.fm.qq.com/vfm.tc.qq.com/R124002cXH931FF9tO.m4a?fromtag=36&guid=1482745683&vkey=D4F8A932596B3A2E928C81B43A534C48B138346568ECD5B3D7765E52AFFE467E5A1A30DCB1989561B29C63834C83353E913553026574F6E3", //播放URl
                        "vLive": []
                    }
                ]
            }
        ]
    },
    "localDataItem": {  //本地广播
        "strAm": "",    //调频
        "strFm": "",    //调幅
        "strProgramName": "",//节目名
        "strRadioName": ""  //电台名
    },
    "sSpeak": "推荐你听听这些节目",
    "sText": "推荐你听听这些节目"
}
```