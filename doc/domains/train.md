# 火车票

### train.*
#### 问法
帮我查下明天北京到深圳的火车票
#### JSON
```c++
enum TRAIN_TYPE
{
    E_TRAINTYPE_G = 0,      // 高铁
    E_TRAINTYPE_C = 1,      // 城际高铁
    E_TRAINTYPE_D = 2,      // 动车
    E_TRAINTYPE_Z = 3,      // 直达
    E_TRAINTYPE_T = 4,      // 特快
    E_TRAINTYPE_K = 5,      // 普快
    E_TRAINTYPE_OTHERS = 6, // 其他
};

enum SEAT_TYPE
{
    E_SEATTYPE_YZ    = 0,       // 硬座
    E_SEATTYPE_YW    = 1,       // 硬卧
    E_SEATTYPE_SWZ   = 2,       // 商务座
    E_SEATTYPE_TDZ   = 3,       // 特等座
    E_SEATTYPE_YDZ   = 4,       // 一等座
    E_SEATTYPE_EDZ   = 5,       // 二等座
    E_SEATTYPE_GJRW  = 6,       // 高级软卧
    E_SEATTYPE_RW    = 7,       // 软卧
    E_SEATTYPE_WZ    = 8,       // 无座
    E_SEATTYPE_OTHERS= 9,       // 其他
    E_SEATTYPE_YWS   = 10,      // 硬卧上
    E_SEATTYPE_YWZ   = 11,      // 硬卧中
    E_SEATTYPE_YWX   = 12,      // 硬卧下
    E_SEATTYPE_RWS   = 13,      // 软卧上
    E_SEATTYPE_RWX   = 14,      // 软卧下
};
```
```json
{
    "moreUrl": "http://p.html5.qq.com/h?u=https%3a%2f%2fm.ctrip.com%2fwebapp%2ftrain%2fv2%2findex.html%3fpage%3dlist%26dstation%3d%e6%b7%b1%e5%9c%b3%26astation%3d%e5%8c%97%e4%ba%ac%26ddate%3d2017-10-23%26allianceid%3d317332%26sid%3d896292&ch=20161223&b=SmartService4TrainTicket",  // 更多链接
    "trainInfos": [
        {
            "additionStationNum": 0,    // 多买或少买的站点数
            "buyTicketUrl": "http://p.html5.qq.com/h?u=https%3a%2f%2fm.ctrip.com%2fwebapp%2ftrain%2fv2%2findex.html%3fpage%3dbooking%26dstation%3d%e7%a6%8f%e7%94%b0%26astation%3d%e5%8c%97%e4%ba%ac%e8%a5%bf%26ddate%3d2017-10-23%26trainnumber%3dG72%26allianceid%3d317332%26sid%3d896292&ch=20161223&b=SmartService4TrainTicket",    //购票链接
            "canWebBuy": true,          // 是否可网上购买
            "controlDay": 29,           // 可提前多少天购买
            "date": "2017-10-23",       // 日期
            "dayDiff": 0,               // 火车需多少天
            "filterType": [ ],
            "fromStation": "福田",        // 出发站点
            "fromStationType": "起点",    // 出发站点类型：起点、终点、经停
            "fromTime": "07:00",        // 出发时间
            "note": "", 
            "realStationName": "",      // 实际购票站点名称
            "realTrainSeats": [ ],      // 实际购票站点座位情况
            "saleDate": "2017-09-24",   // 开售日期
            "saleTime": "14:00",        // 开售时间
            "saleTimestamp": 1506232800,
            "seats": [
                {
                    "bookable": true,       // 是否可预订
                    "price": 944.5,         // 价格
                    "remainNum": 99,        // 剩余坐席
                    "seatName": "二等座",  // 坐席名称
                    "seatType": 5
                }, 
                {
                    "bookable": true, 
                    "price": 1488, 
                    "remainNum": 99, 
                    "seatName": "一等座", 
                    "seatType": 4
                }, 
                {
                    "bookable": true, 
                    "price": 2939, 
                    "remainNum": 9, 
                    "seatName": "商务座", 
                    "seatType": 2
                }
            ], 
            "toStation": "北京西",             // 达到站点名称
            "toStationType": "终点",      // 到达站点类型
            "toTime": "18:21",              // 到达时间
            "trainId": "6i00000G720F",      // 车次ID
            "trainNum": "G72",              // 火车编号
            "trainType": 0,
            "useTime": 681                  // 全程耗时（分钟）
        }
    ]
}
```