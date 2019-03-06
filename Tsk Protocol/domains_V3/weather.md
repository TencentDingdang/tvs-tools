[TOC]

### 领域名称

天气服务

### 意图列表

| Intent                         | Description                    |
| :----------------------------- | ------------------------------ |
| general_search                 | 查天气                         |
| conditional_search_feel        | 查冷热                         |
| conditional_search_activity    | 查询与天气相关的活动建议       |
| conditional_search_outfit      | 查询服装、雨伞等               |
| conditional_search_description | 查询风、雨、雪等具体的气象情况 |
| aqi_search                     | 查询空气质量                   |
| conditional_search_humidity    | 查询湿度                       |
| conditional_search_ultraviolet | 查询紫外线                     |
| conditional_search_temperature | 查询温度                       |



### 数据示例

##### 天气无模板都是自定义数据

```json
/*
 * weather 该意图仅有回复语 无 Json 数据
 * 语料：今天的天气、今天热吗、今天适合打球吗、今天适合穿什么、今天会下雨吗、今天的空气怎么样、今天的空气湿度、今天的紫外线、今天的温度
 * BOT：410音响
*/ 
// ======================= Json 数据 =======================
 {
     "controlInfo": {
         "audioConsole": "", 
         "textSpeak": "false", 
         "type": "TEXT"
     }, 
     "globalInfo": {
         "seeMore": "https://sdk.sparta.html5.qq.com/dingdang/weather.html?gps=113.929634094,22.543512344"
     }, 
     "listItems": [
         {
             "selfData": {
                 "eAction": 3, 
                 "iRet": 0, 
                 "sError": "", 
                 "sPlace": "", 
                 "vecCityWeatherInfo": [
                     {
                         "iDayIndex": 0, 
                         "sCityID": "", 
                         "sCounty": "南山区", 
                         "sDisplayTips": "南山区今天多云，气温和昨天差不多，28度到31度，空气质量优。不过今天晚上9点左右会开始下小雨，出门别忘了带伞。", 
                         "sDistrict": "", 
                         "sMoreUrl": "https://sdk.sparta.html5.qq.com/dingdang/weather.html?gps=113.929634094,22.543512344", 
                         "sProvince": "", 
                         "sWeatherTips": "南山区今天多云，气温和昨天差不多，28度到31度，空气质量优。不过今天晚上9点左右会开始下小雨，出门别忘了带伞。", 
                         "stDobbyCurrentWeather": {
                             "sAQI": "32", 
                             "sAQIDes": "空气优", 
                             "sAQILevel": "1", 
                             "sCloudrate": "0", 
                             "sDWeaIndex": "1", 
                             "sDescription": "晴转多云，今天晚间22点钟后转小雨", 
                             "sDirection": "南西南风", 
                             "sDweather": "多云", 
                             "sHumidity": "0.61", 
                             "sPm25": "16", 
                             "sSpeed": "4级", 
                             "sTemperature": "31", 
                             "stDetailAddr": {
                                 "sAddress": "广东省深圳市南山区深南大道10000号", 
                                 "sCity": "深圳市", 
                                 "sDistict": "南山区", 
                                 "sNation": "中国", 
                                 "sProvince": "广东省", 
                                 "sStreet": "深南大道"
                             }
                         }, 
                         "stLiveIndex": {//今天的指数信息，每天的数据还是保存在vcWeatherInfo中
                             "iFromChannel": 1, 
                             "vLiveIndex": [
                                 {
                                     "iCode": 0, 
                                     "sDay": "2018-06-30", 
                                     "sDesc": "较不适宜", 
                                     "sLevel": "3", 
                                     "sName": "洗车", 
                                     "sStatus": "较不适宜", 
                                     "sUrl": ""
                                 }, 
                                 {
                                     "iCode": 1, 
                                     "sDay": "2018-06-30", 
                                     "sDesc": "热", 
                                     "sLevel": "3", 
                                     "sName": "穿衣", 
                                     "sStatus": "热", 
                                     "sUrl": ""
                                 }, 
                                 {
                                     "iCode": 2, 
                                     "sDay": "2018-06-30", 
                                     "sDesc": "中等", 
                                     "sLevel": "3", 
                                     "sName": "紫外线", 
                                     "sStatus": "中等", 
                                     "sUrl": ""
                                 }, 
                                 {
                                     "iCode": 3, 
                                     "sDay": "2018-06-30", 
                                     "sDesc": "易发", 
                                     "sLevel": "3", 
                                     "sName": "感冒", 
                                     "sStatus": "易发", 
                                     "sUrl": ""
                                 }
                             ]
                         }, 
                         "stWeatherActivity": {
                             "iSuggestion": 0, 
                             "sActivity": "", 
                             "sReason": ""
                         }, 
                         "stWeatherSuggestion": {
                             "sSuggestion": "", 
                             "sWeatherBaseInfo": ""
                         }, 
                         "stYWeatherInfo": {
                             "sAQI": "33", 
                             "sAQIDes": "空气优", 
                             "sAQILevel": "1", 
                             "sCurrentT": "31", 
                             "sDWeaIndex": "2", 
                             "sDressingIndex": "", 
                             "sDweather": "阴", 
                             "sHoliday": "", 
                             "sJumpUrl": "", 
                             "sLunarYear": "", 
                             "sMaxT": "33", 
                             "sMinT": "28", 
                             "sName": "南山区", 
                             "sNewCurT": "31", 
                             "sPm25": "17", 
                             "sTim": "2018-06-29", 
                             "sWeek": "周五", 
                             "sWind": "南西南风", 
                             "sWindPower": "3级", 
                             "stHumidity": {
                                 "fAvg": 0.6600000262260437, 
                                 "fCurrent": 0.6100000143051147, 
                                 "fMax": 0.75, 
                                 "fMin": 0.5400000214576721
                             }, 
                             "stWeatherDetail": {
                                 "nDayWeaIndex": 0, 
                                 "nNightWeaIndex": 0, 
                                 "sDayWeather": "", 
                                 "sDayWind": "", 
                                 "sDayWindPower": "", 
                                 "sNightWeather": "", 
                                 "sNightWind": "", 
                                 "sNightWindPower": ""
                             }, 
                             "vDobbyLiveIndex": [
                                 {
                                     "iType": 0, 
                                     "sDesc": "较不适宜", 
                                     "sLevel": "3", 
                                     "sName": "洗车"
                                 }, 
                                 {
                                     "iType": 1, 
                                     "sDesc": "热", 
                                     "sLevel": "3", 
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
                         "vBgImg": [
                             {
                                 "sImg": "http://soft.imtt.qq.com/browser/smart_service/weather/img/cloudy.jpg",
                                 "eAstroType": 0,
                                 "sMusic": ""
                             }
                         ], 
                         "vFutureIndex": [ ], 
                         "vWeatherWarning": [ {
                            "sAlarmLeveNum": "02", //等级
                            "sAlarmTypeNum": "02", //类型
                            "sAlertId": "43010041600000_20180530101833", 
                            "sCity": "长沙", 
                            "sCityId": "101250101", 
                            "sContent": "长沙市气象台2018年5月30日10时18分发布暴雨黄色预警信号：预计长沙市区、长沙县、浏阳市未来6小时降雨量将达50毫米以上，请注意防范。", 
                            "sIssueTime": "2018-05-30 10:18", 
                            "sLevel": "黄色", //级别
                            "sLinkSuffix": "", 
                            "sProvince": "湖南", 
                            "sStation": "湖南长沙", 
                            "sTitle": "预警中", 
                            "sType": "暴雨"//类型
                        }], 
                         "vcHourlyWeatherInfo": [
                             {
                                 "sAQI": "32", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "1", 
                                 "sDweather": "多云", 
                                 "sHumidity": "0.61", 
                                 "sName": "南山区", 
                                 "sPm25": "16", 
                                 "sPrecipitation": "0", 
                                 "sTemperature": "31", 
                                 "sTim": "2018-06-30 16:00"
                             }, 
                             {
                                 "sAQI": "24", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "1", 
                                 "sDweather": "多云", 
                                 "sHumidity": "0.62", 
                                 "sName": "南山区", 
                                 "sPm25": "16", 
                                 "sPrecipitation": "0", 
                                 "sTemperature": "31", 
                                 "sTim": "2018-06-30 17:00"
                             }, 
                             {
                                 "sAQI": "24", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "0", 
                                 "sDweather": "晴", 
                                 "sHumidity": "0.65", 
                                 "sName": "南山区", 
                                 "sPm25": "16", 
                                 "sPrecipitation": "0", 
                                 "sTemperature": "31", 
                                 "sTim": "2018-06-30 18:00"
                             }, 
                             {
                                 "sAQI": "26", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "0", 
                                 "sDweather": "晴", 
                                 "sHumidity": "0.69", 
                                 "sName": "南山区", 
                                 "sPm25": "17", 
                                 "sPrecipitation": "0", 
                                 "sTemperature": "30", 
                                 "sTim": "2018-06-30 19:00"
                             }, 
                             {
                                 "sAQI": "27", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "1", 
                                 "sDweather": "多云", 
                                 "sHumidity": "0.73", 
                                 "sName": "南山区", 
                                 "sPm25": "18", 
                                 "sPrecipitation": "0", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-06-30 20:00"
                             }, 
                             {
                                 "sAQI": "27", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.76", 
                                 "sName": "南山区", 
                                 "sPm25": "18", 
                                 "sPrecipitation": "0.063500002", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-06-30 21:00"
                             }, 
                             {
                                 "sAQI": "30", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.78", 
                                 "sName": "南山区", 
                                 "sPm25": "20", 
                                 "sPrecipitation": "0.131500006", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-06-30 22:00"
                             }, 
                             {
                                 "sAQI": "31", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.80", 
                                 "sName": "南山区", 
                                 "sPm25": "21", 
                                 "sPrecipitation": "0.170300007", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-06-30 23:00"
                             }, 
                             {
                                 "sAQI": "33", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.81", 
                                 "sName": "南山区", 
                                 "sPm25": "22", 
                                 "sPrecipitation": "0.156599998", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-07-01 00:00"
                             }, 
                             {
                                 "sAQI": "33", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.82", 
                                 "sName": "南山区", 
                                 "sPm25": "22", 
                                 "sPrecipitation": "0.116300002", 
                                 "sTemperature": "28", 
                                 "sTim": "2018-07-01 01:00"
                             }, 
                             {
                                 "sAQI": "31", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.83", 
                                 "sName": "南山区", 
                                 "sPm25": "21", 
                                 "sPrecipitation": "0.088100001", 
                                 "sTemperature": "28", 
                                 "sTim": "2018-07-01 02:00"
                             }, 
                             {
                                 "sAQI": "30", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.83", 
                                 "sName": "南山区", 
                                 "sPm25": "20", 
                                 "sPrecipitation": "0.100100003", 
                                 "sTemperature": "28", 
                                 "sTim": "2018-07-01 03:00"
                             }, 
                             {
                                 "sAQI": "29", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.83", 
                                 "sName": "南山区", 
                                 "sPm25": "19", 
                                 "sPrecipitation": "0.1391", 
                                 "sTemperature": "28", 
                                 "sTim": "2018-07-01 04:00"
                             }, 
                             {
                                 "sAQI": "27", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.82", 
                                 "sName": "南山区", 
                                 "sPm25": "18", 
                                 "sPrecipitation": "0.181299999", 
                                 "sTemperature": "28", 
                                 "sTim": "2018-07-01 05:00"
                             }, 
                             {
                                 "sAQI": "27", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.81", 
                                 "sName": "南山区", 
                                 "sPm25": "18", 
                                 "sPrecipitation": "0.217999995", 
                                 "sTemperature": "28", 
                                 "sTim": "2018-07-01 06:00"
                             }, 
                             {
                                 "sAQI": "26", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.79", 
                                 "sName": "南山区", 
                                 "sPm25": "17", 
                                 "sPrecipitation": "0.299499989", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-07-01 07:00"
                             }, 
                             {
                                 "sAQI": "24", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.76", 
                                 "sName": "南山区", 
                                 "sPm25": "16", 
                                 "sPrecipitation": "0.491100013", 
                                 "sTemperature": "29", 
                                 "sTim": "2018-07-01 08:00"
                             }, 
                             {
                                 "sAQI": "22", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.72", 
                                 "sName": "南山区", 
                                 "sPm25": "14", 
                                 "sPrecipitation": "0.819800019", 
                                 "sTemperature": "30", 
                                 "sTim": "2018-07-01 09:00"
                             }, 
                             {
                                 "sAQI": "19", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "4", 
                                 "sDweather": "中雨", 
                                 "sHumidity": "0.67", 
                                 "sName": "南山区", 
                                 "sPm25": "12", 
                                 "sPrecipitation": "1.161499977", 
                                 "sTemperature": "30", 
                                 "sTim": "2018-07-01 10:00"
                             }, 
                             {
                                 "sAQI": "15", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "4", 
                                 "sDweather": "中雨", 
                                 "sHumidity": "0.64", 
                                 "sName": "南山区", 
                                 "sPm25": "9", 
                                 "sPrecipitation": "1.353600025", 
                                 "sTemperature": "30", 
                                 "sTim": "2018-07-01 11:00"
                             }, 
                             {
                                 "sAQI": "10", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "4", 
                                 "sDweather": "中雨", 
                                 "sHumidity": "0.62", 
                                 "sName": "南山区", 
                                 "sPm25": "5", 
                                 "sPrecipitation": "1.281100035", 
                                 "sTemperature": "31", 
                                 "sTim": "2018-07-01 12:00"
                             }, 
                             {
                                 "sAQI": "7", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "4", 
                                 "sDweather": "中雨", 
                                 "sHumidity": "0.61", 
                                 "sName": "南山区", 
                                 "sPm25": "3", 
                                 "sPrecipitation": "1.017199993", 
                                 "sTemperature": "31", 
                                 "sTim": "2018-07-01 13:00"
                             }, 
                             {
                                 "sAQI": "7", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.62", 
                                 "sName": "南山区", 
                                 "sPm25": "3", 
                                 "sPrecipitation": "0.682399988", 
                                 "sTemperature": "32", 
                                 "sTim": "2018-07-01 14:00"
                             }, 
                             {
                                 "sAQI": "7", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sDWeaIndex": "3", 
                                 "sDweather": "小雨", 
                                 "sHumidity": "0.63", 
                                 "sName": "南山区", 
                                 "sPm25": "3", 
                                 "sPrecipitation": "0.380299985", 
                                 "sTemperature": "32", 
                                 "sTim": "2018-07-01 15:00"
                             }
                         ], 
                         "vcWeatherInfo": [
                             {
                                 "sAQI": "27", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "1", 
                                 "sDressingIndex": "", 
                                 "sDweather": "多云", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "31", 
                                 "sMinT": "28", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "17", 
                                 "sTim": "2018-06-30", 
                                 "sWeek": "周六", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "3级", 
                                 "stHumidity": {
                                     "fAvg": 0.699999988079071, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.800000011920929, 
                                     "fMin": 0.5600000023841858
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
                                         "sName": "穿衣"
                                     }, 
                                     {
                                         "iType": 2, 
                                         "sDesc": "中等", 
                                         "sLevel": "3", 
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
                                 "sAQI": "18", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "4", 
                                 "sDressingIndex": "", 
                                 "sDweather": "中雨", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "32", 
                                 "sMinT": "28", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "11", 
                                 "sTim": "2018-07-01", 
                                 "sWeek": "周日", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "3级", 
                                 "stHumidity": {
                                     "fAvg": 0.7400000095367432, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.8299999833106995, 
                                     "fMin": 0.6100000143051147
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
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
                                 "sAQI": "19", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "3", 
                                 "sDressingIndex": "", 
                                 "sDweather": "小雨", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "30", 
                                 "sMinT": "27", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "12", 
                                 "sTim": "2018-07-02", 
                                 "sWeek": "周一", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "3级", 
                                 "stHumidity": {
                                     "fAvg": 0.7400000095367432, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.8299999833106995, 
                                     "fMin": 0.6600000262260437
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
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
                                 "sAQI": "17", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "4", 
                                 "sDressingIndex": "", 
                                 "sDweather": "中雨", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "30", 
                                 "sMinT": "27", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "11", 
                                 "sTim": "2018-07-03", 
                                 "sWeek": "周二", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "4级", 
                                 "stHumidity": {
                                     "fAvg": 0.7200000286102295, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.8299999833106995, 
                                     "fMin": 0.5799999833106995
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
                                         "sName": "穿衣"
                                     }, 
                                     {
                                         "iType": 2, 
                                         "sDesc": "中等", 
                                         "sLevel": "3", 
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
                                 "sAQI": "15", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "4", 
                                 "sDressingIndex": "", 
                                 "sDweather": "中雨", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "31", 
                                 "sMinT": "28", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "9", 
                                 "sTim": "2018-07-04", 
                                 "sWeek": "周三", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "4级", 
                                 "stHumidity": {
                                     "fAvg": 0.75, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.8399999737739563, 
                                     "fMin": 0.6200000047683716
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
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
                                 "sAQI": "18", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "4", 
                                 "sDressingIndex": "", 
                                 "sDweather": "中雨", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "32", 
                                 "sMinT": "28", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "11", 
                                 "sTim": "2018-07-05", 
                                 "sWeek": "周四", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "4级", 
                                 "stHumidity": {
                                     "fAvg": 0.7400000095367432, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.8399999737739563, 
                                     "fMin": 0.6000000238418579
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
                                         "sName": "穿衣"
                                     }, 
                                     {
                                         "iType": 2, 
                                         "sDesc": "弱", 
                                         "sLevel": "2", 
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
                                 "sAQI": "18", 
                                 "sAQIDes": "空气优", 
                                 "sAQILevel": "1", 
                                 "sCurrentT": "31", 
                                 "sDWeaIndex": "3", 
                                 "sDressingIndex": "", 
                                 "sDweather": "小雨", 
                                 "sHoliday": "", 
                                 "sJumpUrl": "", 
                                 "sLunarYear": "", 
                                 "sMaxT": "31", 
                                 "sMinT": "28", 
                                 "sName": "南山区", 
                                 "sNewCurT": "31", 
                                 "sPm25": "11", 
                                 "sTim": "2018-07-06", 
                                 "sWeek": "周五", 
                                 "sWind": "南西南风", 
                                 "sWindPower": "4级", 
                                 "stHumidity": {
                                     "fAvg": 0.7400000095367432, 
                                     "fCurrent": 0.6100000143051147, 
                                     "fMax": 0.8199999928474426, 
                                     "fMin": 0.6200000047683716
                                 }, 
                                 "stWeatherDetail": {
                                     "nDayWeaIndex": 0, 
                                     "nNightWeaIndex": 0, 
                                     "sDayWeather": "", 
                                     "sDayWind": "", 
                                     "sDayWindPower": "", 
                                     "sNightWeather": "", 
                                     "sNightWind": "", 
                                     "sNightWindPower": ""
                                 }, 
                                 "vDobbyLiveIndex": [
                                     {
                                         "iType": 0, 
                                         "sDesc": "较不适宜", 
                                         "sLevel": "3", 
                                         "sName": "洗车"
                                     }, 
                                     {
                                         "iType": 1, 
                                         "sDesc": "热", 
                                         "sLevel": "3", 
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
                             }
                         ]
                     }
                 ]
             }, 
             "textContent": "南山区今天多云，气温和昨天差不多，28度到31度，空气质量优。不过今天晚上9点左右会开始下小雨，出门别忘了带伞。"
         }
     ]
 }
}

//eAction取值：
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
//告警类型
01=台风
02=暴雨
03=暴雪
04=寒潮
05=大风
06=沙尘暴
07=高温
08=干旱
09=雷电
10=冰雹
11=霜冻
12=大雾
13=霾
14=道路结冰
15=森林火灾
16=雷雨大风

//天气状况
晴=0 
多云=1 
阴=2 
小雨=3 
中雨=4
大雨=5 
暴雨=6
雷阵雨=7
阵雨=8 
小雪=9 
中雪=10 
大雪=11 
暴雪=12 
雾=13 
沙尘=14 
霾=14
冻雨=15
雨夹雪=15
风=16

支持的天气类型：
晴
多云
阴
小雨
中雨
冻雨
大雨
暴雨
小雪
中雪
大雪
雾
沙尘
霾
风
 

//空气质量等级
未知=0
空气优=1
空气良=2
轻度污染=3
中度污染=4
重度污染=5
严重污染=6

//eAstroType类型
enum AstroType
{
    E_ASTRO_DAY		= 0,           //白天
    E_ASTRO_NIGHT  	= 1,           //黑夜
};


```

