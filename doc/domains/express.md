# 快递

### express.*
#### 问法
- 帮我查下快递
- 1234567789

#### JSON
```json
{
    "errorCode": 0, 
    "errorMsg": "", 
    "express": {
        "company": {
            "companyCode": "yuantong", 
            "companyName": "圆通速递",      // 快递公司
            "iconUrl": "http://cdn.kuaidi100.com/images/all/36/yuantong.png",   //快递公司图标
            "kfPhone": "", 
            "shortName": "圆通",      // 快递公司简称
            "website": ""
        }, 
        "departure": "", 
        "destination": "", 
        "detailUrl": "http://poweron.bugly.qq.com/html/express/detail.html?expressNum=1234567789&comCode=yuantong&userId=webAIProxySimulationClient", 
        "expressNum": "1234567789",     // 详情
        "lastState": 1, 
        "routes": [
            {
                "city": "", 
                "detail": "黑龙江省哈尔滨市五常市公司  已收件", 
                "time": "2016-05-04 15:42:51"
            }
        ], 
        "stateName": "已揽件",     // 状态
        "updateTime": 0, 
    }
}
```
