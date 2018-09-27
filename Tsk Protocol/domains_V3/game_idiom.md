[TOC]

### 领域名称

成语接龙

### 意图列表

| Intent                 | Description                  |
| ---------------------- | ---------------------------- |
| game_idiom_enter   | 进入成语接龙游戏                      |
| game_idiom_answer | 成语接龙游戏                      |
| game_idiom_skip  | 跳过本条要接的成语，进入下一个成语                     |
| game_idiom_exit    | 退出成语接龙游戏 |

### 数据示例

##### 全意图 文本模版

```json
/*
 * 全意图 文本模版
 * 语料：我要玩成语接龙
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "来吧，试试你可以挑战几个回合，我先出题你来接，接不上有3次机会说跳过，结束游戏要说退出，开始吧，瞑思苦想",
	"strSpeakTipsText": "来吧，试试你可以挑战几个回合，我先出题你来接，接不上有3次机会说跳过，结束游戏要说退出，开始吧，瞑思苦想"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "true", 
        "orientation": "portrait", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "selfData": {
                "eCard": 1, 
                "iBeatPercentage": 0, 
                "iHignestScore": 0, 
                "iRemainingSkipCount": 3, 
                "iRemainingTimeoutCount": 2, 
                "iRet": 1000, 
                "iScore": 0, 
                "sBottomTips": "首尾拼音一样就可以，多音字也能接哦~", 
                "sRetInfo": "game_idiom_enter", 
                "sSpeakTips": "来吧，试试你可以挑战几个回合，我先出题你来接，接不上有3次机会说跳过，结束游戏要说退出，开始吧，瞑思苦想", 
                "stIdiomCellNew": {
                    "bShowPinyin": false, 
                    "ePlayer": 2, 
                    "sIdiom": "瞑思苦想", 
                    "sPinyin": ""
                }, 
                "stIdiomCellPre": {
                    "bShowPinyin": false, 
                    "ePlayer": 1, 
                    "sIdiom": "", 
                    "sPinyin": ""
                }
            }
        }
    ]
}
```

