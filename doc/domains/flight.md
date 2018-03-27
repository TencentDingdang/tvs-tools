# 航班
### flight.search
查机票
#### 问法
查一下明天深圳飞武汉的飞机票
#### JSON
```json
{
    "sErrorInfo": {
        "iErrorCode": 0, 
        "strErrorMsg": ""
    }, 
    "strMoreUrl": "http://m.ctrip.com/html5/flight/flight-list.html?triptype=1&popup=close&autoawaken=close&sourceid=&ouid=&seo=0&acode=BJS&dcode=SZX&ddate=2017-10-23&allianceid=317332&sid=896289",       // 更多链接
    "vFlightList": [    // 航班列表
        {
            "bIsShared": false,                 // 是否共享航班
            "bIsStop": true,                    // 是否经停
            "fBottomPrice": 0,                  // 是否最低价
            "lArriveTimestamp": 1508770500,     // 到达时间戳
            "lDepartTimestamp": 1508754000,     // 出发时间戳
            "sCraftInfo": {
                "strCraftCode": "73V",          // 飞机型号
                "strCraftName": "波音",         // 飞机名
                "strKind": ""
            }, 
            "sDestination": {
                "sAirport": {
                    "fLat": 0,
                    "fLng": 0, 
                    "strAirportCode": "NAY",        // 机场编号
                    "strAirportName": "南苑",       // 机场名
                    "strCityCode": "BJS",           // 城市航空三字码
                    "strCityName": "北京"           // 城市名称
                }, 
                "strTerminal": ""                   // 航站楼
            }, 
            "sOrigin": {
                "sAirport": {
                    "fLat": 0, 
                    "fLng": 0, 
                    "strAirportCode": "SZX", 
                    "strAirportName": "宝安", 
                    "strCityCode": "SZX", 
                    "strCityName": "深圳"
                }, 
                "strTerminal": "T3"
            }, 
            "strBuyTicketUrl": "http://m.ctrip.com/html5/flight/swift/domestic/cabinlist?acode=BJS&dcode=SZX&ddate=2017-10-23&dfltno=KN5912&allianceid=317332&sid=896289&triptype=1",   // 购票链接
            "strComfort": "", 
            "strCompanyCode": "KN",             // 航空公司编号
            "strCompanyName": "联航",           // 航空公司
            "strFlightNo": "KN5912",            // 航班编号
            "strIconUrl": "https://pic.c-ctrip.com/flight_intl/airline_logo/32/KN.png?v=2",     // 航空公司icon
            "vPolicyInfoList": [
                {
                    "fDiscountRate": 0.5,       // 折扣率
                    "fReturnDiscount": 0,
                    "iFlag": 32, 
                    "iPrice": 1034,             // 价格
                    "iRemainCount": 5,          // 剩余票数
                    "iReturnCash": 0, 
                    "strPolicyName": "", 
                    "strProductId": "tAG4CrEBeyJmbm8iOiJLTjU5MTIiLCJkZGF0ZSI6IjIwMTctMTAtMjMgMTg6MjA6MDABHjRjaXR5IjoiU1pYIiwiYQ0OUEJKUyIsInByaWNlIjowLjAsIndldw0KAHQuFwAAdgE98D0wLCJ0aWQiOiIzYTMwODdjYy0zMjgyLTRlNzctYjFmNi1iODhmNzk3MjM1MDQiLCJ2ZXJzaW9uIjpudWxsfQ==", 
                    "vClassInfoList": [
                        {
                            "iClassCode": 0, 
                            "strClassName": "经济舱",      // 仓位类型
                            "strSubClass": "R"
                        }
                    ], 
                    "vPolicyPkgList": [ ]
                }
            ], 
            "vStopCityInfoList": [  //经停城市信息
                {
                    "strArriveTime": "2017-10-23 20:40:00",     // 到达经停城市时间
                    "strCityName": "阜阳",                      // 经停城市
                    "strDepartTime": "2017-10-23 21:25:00"      // 离开经停城市时间
                }
            ]
        }
    ]
}
```

### flight.search_schedule/search_status/search_boarding/search_checkin/search_terminal/search_netcheckin/search_baggageid
航班动态查询
#### 问法
CA1233航班到了吗
#### JSON
```json
{
    "vFlights": [
        {
            "iShareFlag": 0,                        // 是否共享航班
            "iStopFlag": 1,                         // 是否经停航班
            "strArrAirport": "伊宁",                // 到达机场名
            "strArrAirportCode": "YIN",             // 到达机场编码
            "strArrCity": "伊宁",                   // 到达城市
            "strArrTerminal": "",                   // 到达航站楼
            "strArrTime": "2017-10-22 15:55:00",    // 到达时间
            "strBaggageID": "",                     // 行李转盘编号
            "strBoardGate": "C30",                  // 登机口
            "strCheckinTable": "F,J,K,L",           // 值机口
            "strDepAirport": "北京首都",            // 出发机场名
            "strDepAirportCode": "PEK",             // 出发机场编号
            "strDepCity": "北京",                   // 出发城市
            "strDepTerminal": "T3",                 // 出发航站楼
            "strDepTime": "2017-10-22 10:21:00",    // 出发时间
            "strFlightCompany": "中国国际航空股份有限公司",     // 航空公司
            "strFlightNum": "CA1233",               // 航班编号
            "strPlanArrTime": "2017-10-22 15:50:00",    // 计划到达时间
            "strPlanDepTime": "2017-10-22 09:45:00",    // 计划出发时间
            "strShareFlightNum": "",                // 共享航班的航班号
            "strState": "到达"                      // 当前状态
        }
    ]
}
```