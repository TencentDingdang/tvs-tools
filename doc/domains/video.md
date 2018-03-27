# 视频
### video.*
#### 问法
有什么电视剧
#### JSON
```json
"jsonData": {
    //视频类型  1 长视频 ，2 短视频
    "iVideoClass": 1,
    //guid
    "sGuid": "", 
    //查看更多url
    "sMoreUrl": "http://smartbox.html5.qq.com/search?t=6&q=电视剧",
    //短视频数据 数组
    "vecShortVideoData": [
        {
            //账号类型 机构:0;个人:1;媒体:2;企业:3;政府:4;其他组织:5 机构是历史遗留类型，不再支持新增此类型
            "iAccounttype": 1,
            //播放时长，单位 s 
            "iDuratiuon": 44,
            //视频质量 1335024:清晰; 1335025:一般; 1335026:模糊 
            "iQuality": 1335026, 
            //昨日播放量(人工干预),有小数
            "iView": 16043233, 
            //媒体头像
            "sMediaIcon": "http://inews.gtimg.com/newsapp_ls/0/1231163395_200200/0", 
            //媒体名称
            "sMediaName": "新闻嘚吧嘚",
            //封面图“496x280” 
            "sPicture": "http://puui.qpic.cn/qqvideo_ori/0/n0503gxv6nd_496_280/0",
            //主题 
            "sTheme": "交通", 
            //标题
            "sTitle": "郑州机场一女乘务员从后舱门跌落登机坪 当场骨折送医", 
            //视频 id
            "sVid": "n0503gxv6nd", 
            //标签
            "vTags": [
                "意外事件", 
                "人身安全", 
                "新闻现场", 
                "郑州"
            ]
        }
        
    ],
    //长视频数据 数组
    "vecVideoData": [
        {
            // 视频种类 1 电影，2 电视剧，3 综艺，4 动漫
            "iVideoType": 2,
            //地区
            "sArea": "内地",
            //概述
            "sBrief": "",
            //当前剧集
            "sCurSetNum": "全56集",
            //正片，预告片
            "sEdition": "",
            //视频名称
            "sName": "择天记",
            //别名
            "sNickName": "",
            //图片Url
            "sPicUrl": "http://cdn.read.html5.qq.com/image?src=video_hot&q=5&h=411&w=312&r=0&imageUrl=http%3A%2F%2Fpuui%2Eqpic%2Ecn%2Fvcover%5Fvt%5Fpic%2F0%2Fnuijxf6k13t6z9b1492410994%2F0",
            //视频播放Url
            "sPlayUrl": "http://v.html5.qq.com/?ch=001411#p=detail&vId=4390656&vType=2",
            //评分
            "sScore": "0.0",
            //7天播放量
            "sSevenCount": "136196",
            //子类型
            "sSubType": "0-其他|仙侠|偶像|偶像剧|古力娜扎|古装|古装剧|奇幻|小说改编|择天记|武侠|玄幻|鹿晗|鹿饭福利",
            //总剧集
            "sToTalSetNum": "全56集",
            //类型
            "sType": "电视剧",
            //视频ID
            "sVideoId": "4390656",
            //年份
            "sYear": "2017",
            //演员列表
            "vecActor": [
                "具贤皓",
                "刘美含",
                "古力娜扎",
                "吴倩",
                "姚笛",
                "尤靖茹",
                "张兆辉",
                "张峻宁",
                "曾志伟",
                "曾舜晞",
                "林思意",
                "许龄月",
                "陈数",
                "高圣远",
                "高瀚宇",
                "魏大勋",
                "鹿晗"
            ],
            //导演列表
            "vecDirector": [
                "孔厉大",
                "钟澍佳",
                "麦咏麟"
            ]
        },
        {
            "iVideoType": 2,
            "sArea": "中国大陆",
            "sBrief": "",
            "sCurSetNum": "更新至第1集",
            "sEdition": "",
            "sName": "白鹿原",
            "sNickName": "",
            "sPicUrl": "http://cdn.read.html5.qq.com/image?src=video_hot&q=5&h=411&w=312&r=0&imageUrl=http%3A%2F%2Fres%2Eimtt%2Eqq%2Ecom%2Fhotvideo%2Freal%2F8a3d4841576246b0849a861075437b75%2Ejpg",
            "sPlayUrl": "http://v.html5.qq.com/?ch=001411#p=detail&vId=3524724&vType=2",
            "sScore": "0.0",
            "sSevenCount": "124064",
            "sSubType": "0-其他|伦理|剧情|年代|经典",
            "sToTalSetNum": "全85集",
            "sType": "电视剧",
            "sVideoId": "3524724",
            "sYear": "2017",
            "vecActor": [
                "何冰",
                "刘佩琦",
                "姬他",
                "孙铱",
                "小斯琴高娃",
                "张嘉译",
                "张瑶",
                "戈治均",
                "扈强",
                "李沁",
                "李洪涛",
                "杨帆",
                "杨皓宇",
                "王骁",
                "田昊",
                "秦海璐",
                "翟天临",
                "董洁",
                "邓伦",
                "郝洋",
                "郭涛",
                "雷佳音"
            ],
            "vecDirector": [
                "刘惠宁",
                "刘进"
            ]
        }
```