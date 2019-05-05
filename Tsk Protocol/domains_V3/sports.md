[TOC]

### 领域名称

体育服务

### 意图列表

| Intent             | Description                           |
| :----------------- | ------------------------------------- |
| search_schedule    | 搜索最近有什么比赛                    |
| search_record      | 某个球队的排名多少了                  |
| search_round       | 比赛到第几轮了                        |
| search_score       | 查比赛结果的比分                      |
| search_status      | 搜索比赛是否有开始，到什么状态了      |
| search_time        | 查下比赛时间                          |
| search_channel     | 比赛在哪个频道播                      |
| search_statistics  | 查询某个球队/球员的技术统计数据       |
| search_rankinglist | 技术统计对比，比如“NBA今天谁得分最多” |
| search_information | 查询球队/球员等的基本信息             |
| search_rank_stat   | 查询球队球员成绩计算                  |
| search_group       | 球队与分组的正反向查询                |
| search_player_goal | 查询谁进球了                          |



### 数据示例

##### search_schedule、search_status、search_time、search_channel无模板是自定义数据

```json
/*
 * 语料：世界杯的比赛、世界杯的比开始开始了吗、世界杯什么时候开始、世界杯在哪个平台有直播
 * BOT：410音响
*/ 
{
 	"strTipsText": "这是今天世界杯的比赛安排", 
   	"strSpeakTipsText": "明天世界杯共有2场比赛，明天晚上10点，乌拉圭对阵法国；周六凌晨2点，巴西对阵比利时"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": ""
    }, 
    "listItems": [
        {
            "selfData": {
                "allMatchObj": {
                    "href": "", 
                    "name": ""
                }, 
                "noSupport": "", 
                "replyWords": "这是明天世界杯的比赛安排", 
                "sGuid": "winnyli_webAIProxySimulationClient", 
                "speakerReplyWords": "明天世界杯共有2场比赛，明天晚上10点，乌拉圭对阵法国；周六凌晨2点，巴西对阵比利时", 
                "sportsScores": [ ], 
                "sportsdataObjs": [
                    {
                        "awayTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "http://inews.gtimg.com/newsapp_ls/0/337822212/0.jpg", 
                            "teamName": "法国"
                        }, 
                        "cancelNotify": "", 
                        "channel": "CCTV5 优酷 北体 上体 广体", 
                        "competition": "世界杯", 
                        "detailObj": {
                            "href": "https://aiwx.sparta.html5.qq.com/sports/detail?matchId=958078&sportstype=2", 
                            "name": ""
                        }, 
                        "groupName": "", 
                        "homeTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "http://f.seals.qq.com/filestore/10006/da/64/87/0/sportlogo/team_1_837.png?v=7", 
                            "teamName": "乌拉圭"
                        }, 
                        "livesobjs": [
                            {
                                "href": "http://www.bisai8.com/channel/cctv5/", 
                                "name": "CCTV5"
                            }
                        ], 
                        "matchId": "958078", 
                        "notityObj": {
                            "href": "", 
                            "name": ""
                        }, 
                        "period": "未开始", 
                        "roundNumber": "5", 
                        "roundType": "四分之一决赛第5轮", 
                        "sportsStartTime": "07月06日 22:00", 
                        "sportsStartTimeStamp": 1530885600, 
                        "sportsType": 2
                    }, 
                    {
                        "awayTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "http://f.seals.qq.com/filestore/10006/da/64/87/0/sportlogo/team_1_360.png?v=6", 
                            "teamName": "比利时"
                        }, 
                        "cancelNotify": "", 
                        "channel": "CCTV5 优酷 CCTV1 北体 上体 广体", 
                        "competition": "世界杯", 
                        "detailObj": {
                            "href": "https://aiwx.sparta.html5.qq.com/sports/detail?matchId=958079&sportstype=2", 
                            "name": ""
                        }, 
                        "groupName": "", 
                        "homeTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "http://inews.gtimg.com/newsapp_ls/0/308983532/0.jpg", 
                            "teamName": "巴西"
                        }, 
                        "livesobjs": [
                            {
                                "href": "http://www.bisai8.com/channel/cctv5/", 
                                "name": "CCTV5"
                            }
                        ], 
                        "matchId": "958079", 
                        "notityObj": {
                            "href": "", 
                            "name": ""
                        }, 
                        "period": "未开始", 
                        "roundNumber": "5", 
                        "roundType": "四分之一决赛第5轮", 
                        "sportsStartTime": "07月07日 02:00", 
                        "sportsStartTimeStamp": 1530900000, 
                        "sportsType": 2
                    }
                ], 
                "strJsonToSemantic": ""
            }, 
            "textContent": "明天世界杯共有2场比赛，明天晚上10点，乌拉圭对阵法国；周六凌晨2点，巴西对阵比利时"
        }
    ]
}

```

##### search_record 无模板是自定义数据

```json
/*
 * 语料：世界杯的排名
 * BOT：410音响
*/ 
{
 	"strTipsText": "为你找到了世界杯的排名", 
   	"strSpeakTipsText": "2018赛季世界杯A组积分榜排名前4依次是乌拉圭第1，积分9、俄罗斯第2，积分6、沙特第3，积分3、埃及第4，积分0；B组依次是西班牙第1，积分5、葡萄牙第2，积分5、伊朗第3，积分4、摩洛哥第4，积分1；C组依次是法国第1，积分7、丹麦第2，积分5、秘鲁第3，积分3、澳大利亚第4，积分1；D组依次是克罗地亚第1，积分9、阿根廷第2，积分4、尼日利亚第3，积分3、冰岛第4，积分1；E组依次是巴西第1，积分7、瑞士第2，积分5、塞尔维亚第3，积分3、哥斯达黎加第4，积分1；F组依次是瑞典第1，积分6、墨西哥第2，积分6、韩国第3，积分3、德国第4，积分3；G组依次是比利时第1，积分9、英格兰第2，积分6、突尼斯第3，积分3、巴拿马第4，积分0；H组依次是哥伦比亚第1，积分6、日本第2，积分4、塞内加尔第3，积分4、波兰第4，积分3。"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": "https://aiwx.sparta.html5.qq.com/sports/rank?param=D0fduEabSh32gixc37RggeCaSbYmi4%2FcIf7zEtQSUozOaPJl7YVZArJ2rqhBH4Fy"
    }, 
    "listItems": [
        {
            "selfData": {
                "detailLink": {
                    "href": "https://aiwx.sparta.html5.qq.com/sports/rank?param=D0fduEabSh32gixc37RggeCaSbYmi4%2FcIf7zEtQSUozOaPJl7YVZArJ2rqhBH4Fy", 
                    "name": "查看全部排名"
                }, 
                "iGroupIndex": 0,
                "noSupport": "", 
                "rankdata": {
                    "competitionName": "", 
                    "rankdataObjs": [ ], 
                    "requestField": "", 
                    "subject": ""
                }, 
                "replyWords": "为你找到了世界杯的排名", 
                "sGuid": "winnyli_webAIProxySimulationClient", 
                "speakerReplyWords": "2018赛季世界杯A组积分榜排名前4依次是乌拉圭第1，积分9、俄罗斯第2，积分6、沙特第3，积分3、埃及第4，积分0；B组依次是西班牙第1，积分5、葡萄牙第2，积分5、伊朗第3，积分4、摩洛哥第4，积分1；C组依次是法国第1，积分7、丹麦第2，积分5、秘鲁第3，积分3、澳大利亚第4，积分1；D组依次是克罗地亚第1，积分9、阿根廷第2，积分4、尼日利亚第3，积分3、冰岛第4，积分1；E组依次是巴西第1，积分7、瑞士第2，积分5、塞尔维亚第3，积分3、哥斯达黎加第4，积分1；F组依次是瑞典第1，积分6、墨西哥第2，积分6、韩国第3，积分3、德国第4，积分3；G组依次是比利时第1，积分9、英格兰第2，积分6、突尼斯第3，积分3、巴拿马第4，积分0；H组依次是哥伦比亚第1，积分6、日本第2，积分4、塞内加尔第3，积分4、波兰第4，积分3。", 
                "sportsRecords": [
                    {
                        "competition": "世界杯", 
                        "group": "A组", 
                        "sportsType": 2, 
                        "teamStatVec": [
                            {
                                "competition": "4", 
                                "gamesBack": 0, 
                                "lostMatchCount": 0, 
                                "matchCount": 3, 
                                "planishMatchCount": 0, 
                                "rank": "1", 
                                "score": "9", 
                                "teamId": "837", 
                                "teamLogo": "http://mat1.gtimg.com/2018/images/team/837.png", 
                                "teamName": "乌拉圭", 
                                "winMatchCount": 3
                            },
                            ... 
                            ]
                    }, 
                    {
                        "competition": "世界杯", 
                        "group": "B组", 
                        "sportsType": 2, 
                        "teamStatVec": [
                            {
                                "competition": "4", 
                                "gamesBack": 0, 
                                "lostMatchCount": 0, 
                                "matchCount": 3, 
                                "planishMatchCount": 2, 
                                "rank": "1", 
                                "score": "5", 
                                "teamId": "118", 
                                "teamLogo": "http://mat1.gtimg.com/2018/images/team/118.png", 
                                "teamName": "西班牙", 
                                "winMatchCount": 1
                            }, 
                            ...
                        ]
                    }, 
                    ...
                }
            "textContent": "2018赛季世界杯A组积分榜排名前4依次是乌拉圭第1，积分9、俄罗斯第2，积分6、沙特第3，积分3、埃及第4，积分0；B组依次是西班牙第1，积分5、葡萄牙第2，积分5、伊朗第3，积分4、摩洛哥第4，积分1；C组依次是法国第1，积分7、丹麦第2，积分5、秘鲁第3，积分3、澳大利亚第4，积分1；D组依次是克罗地亚第1，积分9、阿根廷第2，积分4、尼日利亚第3，积分3、冰岛第4，积分1；E组依次是巴西第1，积分7、瑞士第2，积分5、塞尔维亚第3，积分3、哥斯达黎加第4，积分1；F组依次是瑞典第1，积分6、墨西哥第2，积分6、韩国第3，积分3、德国第4，积分3；G组依次是比利时第1，积分9、英格兰第2，积分6、突尼斯第3，积分3、巴拿马第4，积分0；H组依次是哥伦比亚第1，积分6、日本第2，积分4、塞内加尔第3，积分4、波兰第4，积分3。"
        }
    ]
}
```

##### search_round 无模板是自定义数据

```json
/*
 * 语料：世界杯进行到第几轮了
 * BOT：410音响
*/ 
{
 	"strTipsText": "为你找到了世界杯的排名", 
   	"strSpeakTipsText": "世界杯进入到四分之一决赛第5轮了。"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": ""
    }, 
    "listItems": [
        {
            "selfData": {
                "noSupport": "", 
                "replyWords": "世界杯进入到四分之一决赛第5轮了。", 
                "sGuid": "winnyli_webAIProxySimulationClient", 
                "speakerReplyWords": "", 
                "strJsonToSemantic": "{\"params\":[{\"entity_type\":\"usr.sports.round\",\"name\":\"round\",\"values\":[\"四分之一决赛第5轮\"]}]}
    "
            }, 
            "textContent": "世界杯进入到四分之一决赛第5轮了。"
        }
    ]
    }
}
```

##### search_score 无模板是自定义数据

```json
/*
 * 语料：世界杯的比赛结果
 * BOT：410音响
*/ 
{
 	"strTipsText": "这是周二世界杯的比赛结果", 
   	"strSpeakTipsText": "周二世界杯的2场比赛已经全部结束。哥伦比亚4比5不敌英格兰；瑞典1比0战胜瑞士。"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": ""
    }, 
    "listItems": [
        {
            "selfData": {
                "allMatchObj": {
                    "href": "", 
                    "name": ""
                }, 
                "noSupport": "", 
                "replyWords": "这是周二世界杯的比赛结果", 
                "sGuid": "winnyli_webAIProxySimulationClient", 
                "speakerReplyWords": "周二世界杯的2场比赛已经全部结束。哥伦比亚4比5不敌英格兰；瑞典1比0战胜瑞士。", 
                "sportsScores": [
                    {
                        "awayTeam": {
                            "teamGoal": 5, 
                            "teamLogo": "http://img1.gtimg.com/sports/pics/hv1/90/239/2271/147732810.png", 
                            "teamName": "英格兰"
                        }, 
                        "competition": "世界杯", 
                        "detailObj": {
                            "href": "http://sports.qq.com/kbsweb/game.htm?mid=4:958076", 
                            "name": ""
                        }, 
                        "gifLinks": [ ], 
                        "gifObj": {
                            "href": "", 
                            "name": ""
                        }, 
                        "groupName": "", 
                        "homeTeam": {
                            "teamGoal": 4, 
                            "teamLogo": "http://f.seals.qq.com/filestore/10006/da/64/87/0/sportlogo/team_1_832.png?v=6", 
                            "teamName": "哥伦比亚"
                        }, 
                        "matchId": "958076", 
                        "period": "已结束", 
                        "roundNumber": "4", 
                        "roundType": "八分之一决赛第4轮", 
                        "sportsStartTime": "07月04日 02:00", 
                        "sportsStartTimeStamp": 1530640800, 
                        "sportsType": 2
                    }, 
                    {
                        "awayTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "http://inews.gtimg.com/newsapp_ls/0/308983578/0.jpg", 
                            "teamName": "瑞士"
                        }, 
                        "competition": "世界杯", 
                        "detailObj": {
                            "href": "http://sports.qq.com/kbsweb/game.htm?mid=4:958077", 
                            "name": ""
                        }, 
                        "gifLinks": [ ], 
                        "gifObj": {
                            "href": "", 
                            "name": ""
                        }, 
                        "groupName": "", 
                        "homeTeam": {
                            "teamGoal": 1, 
                            "teamLogo": "http://inews.gtimg.com/newsapp_ls/0/304886139/0.jpg", 
                            "teamName": "瑞典"
                        }, 
                        "matchId": "958077", 
                        "period": "已结束", 
                        "roundNumber": "4", 
                        "roundType": "八分之一决赛第4轮", 
                        "sportsStartTime": "07月03日 22:00", 
                        "sportsStartTimeStamp": 1530626400, 
                        "sportsType": 2
                    }
                ], 
                "strJsonToSemantic": ""
            }, 
            "textContent": "周二世界杯的2场比赛已经全部结束。哥伦比亚4比5不敌英格兰；瑞典1比0战胜瑞士。"
        }
    ]
}
```

##### search_statistics 无模板是自定义数据

```json
/*
 * 语料：世界杯的比赛结果
 * BOT：410音响
*/ 
{
 	"strTipsText": "克里斯蒂亚诺.罗纳尔多在05月27日皇家马德里对阵利物浦的欧冠比赛中没有进球", 
   	"strSpeakTipsText": "克里斯蒂亚诺.罗纳尔多在05月27日皇家马德里对阵利物浦的欧冠比赛中没有进球。"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": ""
    }, 
    "listItems": [
        {
            "selfData": {
               "noSupport": "", 
                "replyWords": "", 
                "sGuid": "", 
                "speakerReplyWords": "", 
                "sportsStatisticsObjs": [
                    "2017赛季，克里斯蒂亚诺.罗纳尔多在西甲进球26个"
                ], 
                "stExtStructData": {
                    "iDataType": 1, 
                    "vTeamPlayerPostionInfo": [ ]
                }, 
                "stPlayerAndTeamInfo": {
                    "iDataType": 1, //0 比赛，1：赛季
                    "sBelongLogo": "http://f.seals.qq.com/filestore/10006/da/64/87/0/sportlogo/team_1_359.png?v=7", 
                    "sLogo": "http://f.seals.qq.com/filestore/10006/da/64/87/0/sportlogo/player_1_14937_pCountryBig.jpg?v=4", 
                    "sName": "克里斯蒂亚诺.罗纳尔多", 
                    "sNumber": "7", 
                    "sPosition": "前锋", 
                    "stSportsData": {//比赛相关
                        "awayTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "", 
                            "teamName": ""
                        }, 
                        "cancelNotify": "", 
                        "channel": "", 
                        "competition": "", 
                        "detailObj": {
                            "href": "", 
                            "name": ""
                        }, 
                        "groupName": "", 
                        "homeTeam": {
                            "teamGoal": 0, 
                            "teamLogo": "", 
                            "teamName": ""
                        }, 
                        "livesobjs": [ ], 
                        "matchId": "", 
                        "notityObj": {
                            "href": "", 
                            "name": ""
                        }, 
                        "period": "", 
                        "roundNumber": "", 
                        "roundType": "", 
                        "sportsStartTime": "", 
                        "sportsStartTimeStamp": 0, 
                        "sportsType": 1
                    }, 
                    "stSportsSeason": {//赛季相关
                        "sCompetition": "西甲", 
                        "sRound": "", 
                        "sSeason": "2017"
                    }
                }, 
                "stSessionItem": {
                    "iType": 0, 
                    "sValue": ""
                }, 
                "vStatistics": [
                    {
                        "sCnName": "赛事名", 
                        "sValue": "西甲"
                    }, 
                    {
                        "sCnName": "上场数", 
                        "sValue": "27"
                    }, 
                    {
                        "sCnName": "首发数", 
                        "sValue": "27"
                    }, 
                    {
                        "sCnName": "进球", 
                        "sValue": "26"
                    }, 
                    {
                        "sCnName": "射门", 
                        "sValue": "177"
                    }, 
                    {
                        "sCnName": "射正", 
                        "sValue": "77"
                    }, 
                    {
                        "sCnName": "助攻", 
                        "sValue": "5"
                    }, 
                    {
                        "sCnName": "抢断", 
                        "sValue": "6"
                    }, 
                    {
                        "sCnName": "传球", 
                        "sValue": "735"
                    }
                ]
            }, 
            "textContent": "2018赛季，克里斯蒂亚诺.罗纳尔多在世界杯进球4个"
        }
    ]
}
```

##### search_rankinglist无模板是自定义数据

```json
/*
 * 语料：世界杯谁进球最多
 * BOT：410音响
*/ 
{
 	"strTipsText": "2018赛季世界杯进球第1的球员是凯恩，进球6个。", 
   	"strSpeakTipsText": "2018赛季世界杯进球第1的球员是凯恩，进球6个。"
}
// ======================= Json 数据 ======================= 
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": ""
    }, 
    "listItems": [
        {
            "selfData": {
                "noSupport": "", 
                "replyWords": "", 
                "sGuid": "", 
                "speakerReplyWords": "", 
                "sportsStatisticsObjs": [
                    "2018赛季世界杯进球第1的球员是凯恩，进球6个。"
                ], 
                "stSessionItem": {
                    "iType": 0, 
                    "sValue": "凯恩"
                }, 
                "vStatistics": [ ]
            }, 
            "textContent": "2018赛季世界杯进球第1的球员是凯恩，进球6个。"
        }
    ]
}
```

##### search_information、search_rank_stat、search_group、search_player_goal无模板是自定义数据

```json
/*
 * 语料：C罗的身高、俄罗斯参加过几次世界杯、世界杯的分组、俄罗斯这场比赛谁进球了
 * BOT：410音响
*/ 
{
 	"strTipsText": "西班牙和俄罗斯上周日的比赛中，俄罗斯进球球员有：久巴，进球1个", 
   	"strSpeakTipsText": "西班牙和俄罗斯上周日的比赛中，俄罗斯进球球员有：久巴，进球1个"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "false", 
        "type": "TEXT"
    }, 
    "globalInfo": {
        "seeMore": ""
    }, 
    "listItems": [
        {
            "selfData": {
                "noSupport": "", 
                "replyWords": "西班牙和俄罗斯上周日的比赛中，俄罗斯进球球员有：", 
                "sGuid": "", 
                "speakerReplyWords": "", 
                "sportsStatisticsObjs": [
                    "久巴，进球1个"
                ], 
                "stSessionItem": {
                    "iType": 0, 
                    "sValue": ""
                }, 
                "vStatistics": [ ]
            }, 
            "textContent": "西班牙和俄罗斯上周日的比赛中，俄罗斯进球球员有：
久巴，进球1个"
        }
    ]
}
```



#### 备注

1. 比赛状态（period）的取值范围

   未开始
   比赛延期
   比赛中
   上半时
   中场休息
   下半时
   加时赛上半时
   加时赛下半时
   互罚点球
   第一节
   第二节
   第三节
   第四节
   已结束



