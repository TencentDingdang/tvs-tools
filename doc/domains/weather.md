# 天气
### weather.*
#### 问法
深圳今天天气怎样
#### JSON
```json
{
    "eAction": 3, //请求的意图
    "iRet": 0, //返回值
    "sError": "", 错误码
    "sPlace": "", // 请求时上报的地名，目前没有填
    "vecCityWeatherInfo": [//城市列表
        {
            "iDayIndex": -1, // 用户想查的是哪天的天气 -1:展示天气查询几天卡片 0:今天 1:明天 对应到vcWeatherInfo里面的索引
            "sCityID": "", //城市id，现在没用
            "sCounty": "武汉", //城市名
            "sDisplayTips": "武汉今天多云，气温24到31度。未来4天以中雨为主。明天多云。最高32度，最低24度。", // 简要朗读天气信息
            "sDistrict": "", //地区
            "sMoreUrl": "http://www.caiyunapp.com/share/?#114.27067,30.58094",//查看更多的地址
            "sProvince": "", //省份
            "sWeatherTips": "武汉今天多云，气温二十四到三十一度。未来4天以中雨为主。明天多云。最高三十二度，最低二十四度。", // 展示用的天气文案
            "stLiveIndex": {//指数 后续可能会切换到别的源，数据没有这么详细了
                "vLiveIndex": [ {
                  iCode: 7 //编码
                  sDay: 2017-08-09 //日期
                  sDesc: 建议用露质面霜打底，水质无油粉底霜，透明粉饼，粉质胭脂。 //描述
                  sLevel: 10 //级别
                  sName: 化妆指数 //名字
                  sStatus: 控油 //状态
                  sUrl: http://index.moji.com/show/show/index?indexid=7&cityid=892&channelno=5323 ////跳转url
                }]
            }, 
            "stWeatherActivity": {//活动 目前只填充了洗车活动
                "iSuggestion": 0, //建议
                "sActivity": "", //活动名称
                "sReason": ""//原因
            }, 
            "vWeatherWarning": [ ], //预警信息，可能没有数据
            "vcWeatherInfo": [//天气信息，包括5天的信息
                {
                    "sAQI": "66", //空气质量
                    "sAQIDes": "空气良", //空气描述
                    "sCurrentT": "29", //当前温度
                    "sDWeaIndex": "1",  //白天天气信息Index,取BWEA, 0.晴 1.多云 2.阴 3.小雨 4.中雨/冻雨 5.大雨 6.暴雨 7.雷阵雨 8.阵雨 9.小雪 10.中雪 11.大雪 12.暴雪 13.雾 14.沙尘 15.雨夹雪 16.台风 如遇“小雨-中雨”，以后面为准
                    "sDressingIndex": "", //穿衣指数 目前没有数据
                    "sDweather": "多云", //天气状态
                    "sHoliday": "", //节假日信息
                    "sJumpUrl": "", //跳转地址 目前没有数据
                    "sLunarYear": "", //农历信息
                    "sMaxT": "31", //最高温度，单位摄氏度
                    "sMinT": "24", //最低温度，单位摄氏度
                    "sName": "武汉", //城市名称
                    "sNewCurT": "29", //新实时温度字段
                    "sPm25": "38", // pm2.5
                    "sTim": "2017-08-15",//天气时间 
                    "sWeek": "周二", //星期
                    "sWind": "", //风向1,如：东南风
                    "sWindPower": "", //风力1,如：3-4级
                    "stHumidity": {//湿度
                        "fAvg": 0.43, //平均
                        "fCurrent": 0.36, //当前
                        "fMax": 0.49, //最高
                        "fMin": 0.35//最低
                    }, 
                    "stWeatherDetail": {
                        "nDayWeaIndex": 0, //白天天气信息index
                        "nNightWeaIndex": 0, //晚上天气信息index
                        "sDayWeather": "", //白天天气信息
                        "sDayWind": "",  //白天风向
                        "sDayWindPower": "", //白天风力
                        "sNightWeather": "", //晚上天气信息
                        "sNightWind": "",  //晚上风向
                        "sNightWindPower": "" //晚上风力
                    },
                    "vDobbyLiveIndex": [//指数
                        {
                            "iType": 0, //指数类型
                            "sDesc": "适宜", //描述
                            "sLevel": "1", //等级
                            "sName": "洗车"//指数名
                        }, 
                        {
                            "iType": 1, 
                            "sDesc": "凉爽", 
                            "sLevel": "5", 
                            "sName": "穿衣"
                        }, 
                        {
                            "iType": 2, 
                            "sDesc": "最弱", 
                            "sLevel": "1", 
                            "sName": "紫外线"
                        }, 
                        {
                            "iType": 3, 
                            "sDesc": "易发", 
                            "sLevel": "3", 
                            "sName": "感冒"
                        }
                    ]
                }, 
                {
                    "sAQI": "66", 
                    "sAQIDes": "空气良", 
                    "sCurrentT": "29", 
                    "sDWeaIndex": "1", 
                    "sDressingIndex": "", 
                    "sDweather": "多云", 
                    "sHoliday": "", 
                    "sJumpUrl": "", 
                    "sLunarYear": "", 
                    "sMaxT": "32", 
                    "sMinT": "24", 
                    "sName": "武汉", 
                    "sNewCurT": "29", 
                    "sPm25": "38", 
                    "sTim": "2017-08-16", 
                    "sWeek": "周三", 
                    "sWind": "", 
                    "sWindPower": "", 
                    "stWeatherDetail": {
                        "nDayWeaIndex": 0, 
                        "nNightWeaIndex": 0, 
                        "sDayWeather": "", 
                        "sDayWind": "", 
                        "sDayWindPower": "", 
                        "sNightWeather": "", 
                        "sNightWind": "", 
                        "sNightWindPower": ""
                    }
                }, 
                {
                    "sAQI": "66", 
                    "sAQIDes": "空气良", 
                    "sCurrentT": "29", 
                    "sDWeaIndex": "4", 
                    "sDressingIndex": "", 
                    "sDweather": "中雨", 
                    "sHoliday": "", 
                    "sJumpUrl": "", 
                    "sLunarYear": "", 
                    "sMaxT": "31", 
                    "sMinT": "24", 
                    "sName": "武汉", 
                    "sNewCurT": "29", 
                    "sPm25": "38", 
                    "sTim": "2017-08-17", 
                    "sWeek": "周四", 
                    "sWind": "", 
                    "sWindPower": "", 
                    "stWeatherDetail": {
                        "nDayWeaIndex": 0, 
                        "nNightWeaIndex": 0, 
                        "sDayWeather": "", 
                        "sDayWind": "", 
                        "sDayWindPower": "", 
                        "sNightWeather": "", 
                        "sNightWind": "", 
                        "sNightWindPower": ""
                    }
                }, 
                {
                    "sAQI": "66", 
                    "sAQIDes": "空气良", 
                    "sCurrentT": "29", 
                    "sDWeaIndex": "4", 
                    "sDressingIndex": "", 
                    "sDweather": "中雨", 
                    "sHoliday": "", 
                    "sJumpUrl": "", 
                    "sLunarYear": "", 
                    "sMaxT": "30", 
                    "sMinT": "24", 
                    "sName": "武汉", 
                    "sNewCurT": "29", 
                    "sPm25": "38", 
                    "sTim": "2017-08-18", 
                    "sWeek": "周五", 
                    "sWind": "", 
                    "sWindPower": "", 
                    "stWeatherDetail": {
                        "nDayWeaIndex": 0, 
                        "nNightWeaIndex": 0, 
                        "sDayWeather": "", 
                        "sDayWind": "", 
                        "sDayWindPower": "", 
                        "sNightWeather": "", 
                        "sNightWind": "", 
                        "sNightWindPower": ""
                    }
                }, 
                {
                    "sAQI": "66", 
                    "sAQIDes": "空气良", 
                    "sCurrentT": "29", 
                    "sDWeaIndex": "4", 
                    "sDressingIndex": "", 
                    "sDweather": "中雨", 
                    "sHoliday": "", 
                    "sJumpUrl": "", 
                    "sLunarYear": "", 
                    "sMaxT": "30", 
                    "sMinT": "24", 
                    "sName": "武汉", 
                    "sNewCurT": "29", 
                    "sPm25": "38", 
                    "sTim": "2017-08-19", 
                    "sWeek": "周六", 
                    "sWind": "", 
                    "sWindPower": "", 
                    "stWeatherDetail": {
                        "nDayWeaIndex": 0, 
                        "nNightWeaIndex": 0, 
                        "sDayWeather": "", 
                        "sDayWind": "", 
                        "sDayWindPower": "", 
                        "sNightWeather": "", 
                        "sNightWind": "", 
                        "sNightWindPower": ""
                    }
                }
            ]
        }
    ]
}

eAction取值：
enum DOBBY_WEATHER_ACTION
{
    GENERAL_SEARCH = 3,//查询天气
    CONDITIONAL_SEARCH_DESCRIPTION = 4,//查询气象
    CONDITIONAL_SEARCH_FEEL = 5,//查询冷热
    CONDITIONAL_SEARCH_ACTIVITY = 6,//查询活动
    CONDITIONAL_SEARCH_OUTFIT = 7,//查询服装
    AQI_SEARCH = 8,//查询空气质量

};
//指数类型
enum IndexType
{
    E_INDEX_CARWASHING      = 0,           //洗车
    E_INDEX_DRESSING        = 1,           //穿衣。
    E_INDEX_ULTRAVIOLET     = 2,           //紫外线。
    E_INDEX_COLDRISK        = 3,           //感冒。
};
```