[TOC]

### 领域名称

火车票

### 意图列表

| Intent              | Description                         |
| ------------------  | ----------------------------------- |
| search_ticket       | 火车票查询                          |


### 数据示例

##### search_ticket 意图，火车票查询模版

```json
/*
 * search_ticket意图，火车票查询模版
 * 语料：明天北京到深圳的火车票
 * BOT：腾讯叮当App (ad415e3e-643c-489a-88ca-3fda41f976c1)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "为你找到了8趟2018-08-24到深圳的车次：
G71，列车07:27从北京西出发，于18:03抵达福田，车票1488元起
G79，列车10:00从北京西出发，于18:46抵达福田，车票944.5元起
Z107，列车19:53从北京西出发，于次日18:10抵达深圳，车票254.5元起
D901，列车20:10从北京西出发，于次日07:06抵达深圳北，车票1430元起
D903，列车20:15从北京西出发，于次日07:11抵达深圳北，车票1430元起
D909，列车20:20从北京西出发，于次日07:16抵达深圳北，车票1430元起
D927，列车20:25从北京西出发，于次日07:25抵达深圳北，车票1430元起
K105，列车23:16从北京西出发，于 第3天04:20抵达深圳，车票254.5元起",

	"strSpeakTipsText": "为你找到了8趟2018-08-24到深圳的车次：
G71，列车07:27从北京西出发，于18:03抵达福田，车票1488元起
G79，列车10:00从北京西出发，于18:46抵达福田，车票944.5元起
Z107，列车19:53从北京西出发，于次日18:10抵达深圳，车票254.5元起
D901，列车20:10从北京西出发，于次日07:06抵达深圳北，车票1430元起
D903，列车20:15从北京西出发，于次日07:11抵达深圳北，车票1430元起
D909，列车20:20从北京西出发，于次日07:16抵达深圳北，车票1430元起
D927，列车20:25从北京西出发，于次日07:25抵达深圳北，车票1430元起
K105，列车23:16从北京西出发，于 第3天04:20抵达深圳，车票254.5元起"
}
// ======================= Json 数据 =======================
{
            "baseInfo": {
                "skillName": "火车票查询"                     //技能名称
            }, 
            "controlInfo": {
                "textSpeak": "false",                         //默认不播报 
                "type": "GRAPHIC",                            //图文卡片
                "version": "1.0.0"                            //版本
            }, 
	
            "globalInfo": {
                "seeMore": "https://m.ctrip.com/webapp/train/v2/index.html?page=list&dstation=北京&astation=深圳&ddate=2018-08-24&allianceid=317332&sid=896292",    //查看更多url
                "selfData": {                                 //私有数据
                    "eSeatTypes": [                           //要求坐席   0硬座 1硬卧 2商务座 3特等座 4一等座 5二等座 6高级软卧 7软卧 8无座 9其他 10硬卧上 11硬卧中 12硬卧下 13软卧上 14软卧下 15动卧上 16动卧下
                        9
                    ], 
                    "fromName": "北京",                       //出发地
                    "inputTime": "2018-08-24",                //用户输入原始时间
                    "lunarTime": "",                          // 农历时间
                    "needSmartQuery": 0,                      // 是否需要智能查询：0 关闭；1 打开；
                    "period": "",                             // 时间段
                    "periodEnd": "",                          // 时间段结束时间点
                    "periodStart": "",                        // 时间段开始时间点
                    "seatType": "",                           // 坐席类型
                    "startDate": "2018-08-24",                // 出发日期 2016-12-20
                    "time": "",                               // 出发时间 09:00
                    "toName": "深圳",                         // 目的地
                    "trainNum": "",                           // 列车车次
                    "trainType": "",                          // 列车类型
                    "userBase": {
                        "bSave": true, 
                        "botType": {
                            "sBotID": "", 
                            "sBotType": ""
                        }, 
                        "iMCC": 0, 
                        "iMNC": 0, 
                        "sAPN": "", 
                        "sAdId": "", 
                        "sCellNumber": "", 
                        "sCellid": "", 
                        "sCellphone": "", 
                        "sChannel": "", 
                        "sFirstChannel": "", 
                        "sGUID": [
                            98, 
                            105, 
                            110, 
                            107, 
                            102, 
                            117, 
                            95, 
                            119, 
                            101, 
                            98, 
                            65, 
                            73, 
                            80, 
                            114, 
                            111, 
                            120, 
                            121, 
                            83, 
                            105, 
                            109, 
                            117, 
                            108, 
                            97, 
                            116, 
                            105, 
                            111, 
                            110, 
                            67, 
                            108, 
                            105, 
                            101, 
                            110, 
                            116
                        ], 
                        "sIMEI": "", 
                        "sIP": "183.36.108.110", 
                        "sLAC": "", 
                        "sLC": "", 
                        "sMac": [ ], 
                        "sQUA2": "DE=PHONE&ENV=RELEASE&NB=WEB&PL=ADR&PP=com.tencent.ai&PR=TVS&QV=3&SP=1&SPtest=3&VE=V0.1&VN=1000", 
                        "sUA": "", 
                        "sUin": "", 
                        "sVenderId": "", 
                        "vLBSKeyData": [
                            49, 
                            49, 
                            51, 
                            46, 
                            57, 
                            50, 
                            57, 
                            54, 
                            51, 
                            52, 
                            52, 
                            48, 
                            48, 
                            48, 
                            124, 
                            50, 
                            50, 
                            46, 
                            53, 
                            52, 
                            51, 
                            53, 
                            49, 
                            51, 
                            50, 
                            57, 
                            48, 
                            48
                        ], 
                        "vWifiMacs": [ ]
                    }, 
                    "userId": ""
                }
            }, 

            "listItems": [
                {
                    "selfData": {
                        "additionStationNum": 0,                 // 额外买的站数：上车补票为负；多买站为正
                        "buyTicketUrl": "https://m.ctrip.com/webapp/train/v2/index.html?page=booking&dstation=北京西&astation=福田&ddate=2018-08-24&trainnumber=G71&allianceid=317332&sid=896292", // 购票链接
                        "canWebBuy": true,                       // 是否可网上购买
                        "controlDay": 29, 
                        "date": "2018-08-24",                    // 发车日期
                        "dayDiff": 0,                            // 跨越天数
                        "filterType": [ ],                       // 车次特点
                        "fromStation": "北京西",                 // 出发站
                        "fromStationType": "起点",               // 出发站类型：起点、途经
                        "fromTime": "07:27",                     // 出发时间
                        "note": "", 
                        "realStationName": "",                   // 实际购票站点名
                        "realTrainSeats": [ ],                   // 实际购票站点的坐席信息
                        "saleDate": "2018-07-26",                // 发售日期
                        "saleTime": "08:00",                     // 发售时间      
                        "saleTimestamp": 1532563200,             // 发售时间戳

                        "seats": [                               // 坐席信息
                            {
                                "bookable": false,               // 是否可预订
                                "price": 944.5,                  // 票价
                                "remainNum": 0,                  // 剩余票数
                                "seatName": "二等座",            // 坐席名称
                                "seatType": 5                    // 坐席类型id
                            }, 
                            {
                                "bookable": true, 
                                "price": 1488, 
                                "remainNum": 6, 
                                "seatName": "一等座", 
                                "seatType": 4
                            }, 
                            {
                                "bookable": false, 
                                "price": 2939, 
                                "remainNum": 0, 
                                "seatName": "商务座", 
                                "seatType": 2
                            }, 
                            {
                                "bookable": false, 
                                "price": 944.5, 
                                "remainNum": 0, 
                                "seatName": "无座", 
                                "seatType": 8
                            }
                        ], 
                        "toStation": "福田",                      // 目的站
                        "toStationType": "终点",                  // 目的站类型：途经、终点
                        "toTime": "18:03",                        // 到达时间
                        "trainId": "2400000G710Q", 
                        "trainNum": "G71",                        // 火车车次号
                        "trainType": 0,                           // 列车类型
                        "useTime": 636                            // 总用时：分钟
                    }
                }, 
                {
                    "selfData": {
                        "additionStationNum": 0, 
                        "buyTicketUrl": "https://m.ctrip.com/webapp/train/v2/index.html?page=booking&dstation=北京西&astation=福田&ddate=2018-08-24&trainnumber=G79&allianceid=317332&sid=896292", 
                        "canWebBuy": true, 
                        "controlDay": 29, 
                        "date": "2018-08-24", 
                        "dayDiff": 0, 
                        "filterType": [ ], 
                        "fromStation": "北京西", 
                        "fromStationType": "起点", 
                        "fromTime": "10:00", 
                        "note": "", 
                        "realStationName": "", 
                        "realTrainSeats": [ ], 
                        "saleDate": "2018-07-26", 
                        "saleTime": "08:00", 
                        "saleTimestamp": 1532563200, 
                        "seats": [
                            {
                                "bookable": true, 
                                "price": 944.5, 
                                "remainNum": 99, 
                                "seatName": "二等座", 
                                "seatType": 5
                            }, 
                            {
                                "bookable": true, 
                                "price": 1488, 
                                "remainNum": 19, 
                                "seatName": "一等座", 
                                "seatType": 4
                            }, 
                            {
                                "bookable": true, 
                                "price": 2939, 
                                "remainNum": 5, 
                                "seatName": "商务座", 
                                "seatType": 2
                            }
                        ], 
                        "toStation": "福田", 
                        "toStationType": "终点", 
                        "toTime": "18:46", 
                        "trainId": "2400000G790E", 
                        "trainNum": "G79", 
                        "trainType": 0, 
                        "useTime": 526
                    }
                }
            ]
        }
```
