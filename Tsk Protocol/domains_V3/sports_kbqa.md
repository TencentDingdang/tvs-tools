### 领域名称
sports


### 意图列表

| Intent    | Description |
| --------- | ----------- |
| search_match_info_kg       |    查询赛事信息  |
|search_team_info_kg|查询球队信息(通用)|
|search_team_time_kg|查询球队信息(时间类)|
|search_player_info_kg|查询球星信息(通用)|
|search_player_time_kg|查询球星信息(时间类)|
### 数据示例

##### 纯文本模版

```json
/*
 * 所有意图仅有回复语 无 Json 数据
 * 语料：历届世界杯举办地？
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 

    {
        "controlInfo": {
            "textSpeak": "true", 
            "type": "TEXT", 
            "version": "1.0.0"
            }, 
        "listItems": [
            {
                "textContent": "帮您查询到近5届的数据，2014届：巴西，2010届：南非，2006届：德国，2002届：韩国和日本，1998届：法国。"
            }
            ]
        }
    }
    