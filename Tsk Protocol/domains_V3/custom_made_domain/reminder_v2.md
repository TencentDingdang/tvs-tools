[TOC]

### 查看提醒

#### 没有数据

##### 示例

```json
{
    "stCalendarData": {
        "sSpeakTips": "我查了查，你没有提醒事项。", 
        "stBroadData": {
            "mBroadData": { }, 
            "mGatherBroadData": { }
        },
        "vAffectReminderCell": [ ], 
        "vReminderCell": [ ], 
        "vUIReminderCell": [ ]
    }
}
```

##### 字段含义

| 字段名称                           | 字段类型 | 字段含义                         |
| ---------------------------------- | -------- | -------------------------------- |
| stCalendarData                     | Object   | 主数据字段，存放客户端需要的数据 |
| stCalendarData.sSpeakTips          | string   | 回复语字段，可选                 |
| stCalendarData.stBroadData         | Object   | 见 公共模块 の 播报语 部分       |
| stCalendarData.vAffectReminderCell | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vReminderCell       | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vUIReminderCell     | Object   | 见 公共模块 の 数据列表 部分     |

#### 命中数据

##### 示例

```json
{
    "stCalendarData": {
        "sSpeakTips": "你明天上午8点整有一个提醒。", 
        "stBroadData": {
            "mBroadData": {
                "1539734400": "time##的提醒时间到了"
            }
        }, 
        "vAffectReminderCell": [ ], 
        "vReminderCell": [
            {
                "eRepeatType": 1, 
                "lId": 1539676338558, 
                "lStart": 1539734400, 
                "lUpdate": 1539676338, 
                "sNote": "", 
                "vImageUrl": [ ], 
                "vStrUrlId": [
                    "resource.search$10038"
                ]
            }
        ], 
        "vUIReminderCell": [
            {
                "eRepeatType": 1, 
                "lId": 1539676338558, 
                "lStart": 1539734400, 
                "lUpdate": 1539676338, 
                "sNote": "", 
                "vImageUrl": [ ], 
                "vStrUrlId": [ ]
            }
        ]
    }
}
```

##### 字段含义

| 字段名称                           | 字段类型 | 字段含义                         |
| ---------------------------------- | -------- | -------------------------------- |
| stCalendarData                     | Object   | 主数据字段，存放客户端需要的数据 |
| stCalendarData.sSpeakTips          | string   | 回复语字段，可选                 |
| stCalendarData.stBroadData         | Object   | 见 公共模块 の 播报语 部分       |
| stCalendarData.vAffectReminderCell | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vReminderCell       | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vUIReminderCell     | Object   | 见 公共模块 の 数据列表 部分     |

### 新增提醒

#### 成功

##### 示例

```json
{
    "stCalendarData": {
        "sSpeakTips": "这就为你设置好明天上午9点整的提醒。", 
        "stBroadData": {
            "mBroadData": {
                "1539734400": "time##的提醒时间到了", 
                "1539738000": "time##的提醒时间到了"
            }
        }, 
        "vAffectReminderCell": [
            {
                "eRepeatType": 1, 
                "lId": 1539676383839, 
                "lStart": 1539738000, 
                "lUpdate": 1539676383, 
                "sNote": "", 
                "vSelfRingCell": [
                    {
                        "sAuditionUrl": "", 
                        "sBackgroundImageUrl": "http://soft.imtt.qq.com/browser/TBS/dingdang/resource_manager/cover/daji.jpg", 
                        "sId": "resource.search$10038", 
                        "sName": "妲己", 
                        "sType": "王者荣耀"
                    }
                ], 
                "vStrUrlId": [
                    "resource.search$10038"
                ]
            }
        ], 
        "vReminderCell": [
            {
                "eRepeatType": 1, 
                "lId": 1539676338558, 
                "lStart": 1539734400, 
                "lUpdate": 1539676338, 
                "sNote": "", 
                "vImageUrl": [ ], 
                "vStrUrlId": [
                    "resource.search$10038"
                ]
            }, 
            {
                "eRepeatType": 1, 
                "lId": 1539676383839, 
                "lStart": 1539738000, 
                "lUpdate": 1539676383, 
                "sNote": "", 
                "vImageUrl": [ ], 
                "vStrUrlId": [
                    "resource.search$10038"
                ]
            }
        ], 
        "vUIReminderCell": [ ]
    }
}
```

##### 字段含义

| 字段名称                           | 字段类型 | 字段含义                         |
| ---------------------------------- | -------- | -------------------------------- |
| stCalendarData                     | Object   | 主数据字段，存放客户端需要的数据 |
| stCalendarData.sSpeakTips          | string   | 回复语字段，可选                 |
| stCalendarData.stBroadData         | Object   | 见 公共模块 の 播报语 部分       |
| stCalendarData.vAffectReminderCell | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vReminderCell       | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vUIReminderCell     | Object   | 见 公共模块 の 数据列表 部分     |

#### 失败

##### 示例

```json
{
    "stCalendarData": {
        "sSpeakTips": "设置时间是过去的提醒，这个太难了，叮当还做不到呢！", 
        "stBroadData": {
            "mBroadData": {
                "1539734400": "time##的提醒时间到了"
            }
        }, 
        "vAffectReminderCell": [ ], 
        "vReminderCell": [
            {
                "eRepeatType": 1, 
                "lId": 1539676338558, 
                "lStart": 1539734400, 
                "lUpdate": 1539676338, 
                "sNote": "", 
                "vImageUrl": [ ], 
                "vStrUrlId": [
                    "resource.search$10038"
                ]
            }
        ], 
        "vUIReminderCell": [ ]
    }, 
    "stGetAllSelfRing": {
        "vSelfRingCell": { }
    }
}
```

##### 字段含义

| 字段名称                           | 字段类型 | 字段含义                         |
| ---------------------------------- | -------- | -------------------------------- |
| stCalendarData                     | Object   | 主数据字段，存放客户端需要的数据 |
| stCalendarData.sSpeakTips          | string   | 回复语字段，可选                 |
| stCalendarData.stBroadData         | Object   | 见 公共模块 の 播报语 部分       |
| stCalendarData.vAffectReminderCell | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vReminderCell       | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vUIReminderCell     | Object   | 见 公共模块 の 数据列表 部分     |

### 删除提醒

#### 成功

##### 示例

```json
{
    "sSpeakTips": "明天上午9点整的提醒已取消，你放心去忙吧。", 
    "stBroadData": {
        "mBroadData": {
            "1539734400": "time##的提醒时间到了"
        }
    }, 
    "vAffectReminderCell": [
        {
            "eRepeatType": 1, 
            "lId": 1539676383839, 
            "lStart": 1539738000, 
            "lUpdate": 1539676383, 
            "sNote": "", 
            "vSelfRingCell": [
                {
                    "sAuditionUrl": "", 
                    "sBackgroundImageUrl": "http://soft.imtt.qq.com/browser/TBS/dingdang/resource_manager/cover/daji.jpg", 
                    "sId": "resource.search$10038", 
                    "sName": "妲己", 
                    "sType": "王者荣耀"
                }
            ], 
            "vStrUrlId": [
                "resource.search$10038"
            ]
        }
    ], 
    "vReminderCell": [
        {
            "eRepeatType": 1, 
            "lId": 1539676338558, 
            "lStart": 1539734400, 
            "lUpdate": 1539676338, 
            "sNote": "", 
            "vImageUrl": [ ], 
            "vStrUrlId": [
                "resource.search$10038"
            ]
        }
    ], 
	"vUIReminderCell": [ ]
}
```

##### 字段含义

| 字段名称                           | 字段类型 | 字段含义                         |
| ---------------------------------- | -------- | -------------------------------- |
| stCalendarData                     | Object   | 主数据字段，存放客户端需要的数据 |
| stCalendarData.sSpeakTips          | string   | 回复语字段，可选                 |
| stCalendarData.stBroadData         | Object   | 见 公共模块 の 播报语 部分       |
| stCalendarData.vAffectReminderCell | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vReminderCell       | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vUIReminderCell     | Object   | 见 公共模块 の 数据列表 部分     |

#### 失败

##### 示例

```json
{
    "sSpeakTips": "我查了查，你明天上午10点整没有提醒事项。", 
    "stBroadData": {
        "mBroadData": {
            "1539734400": "time##的提醒时间到了"
        }
    }, 
    "vAffectReminderCell": [ ], 
    "vReminderCell": [
        {
            "eRepeatType": 1, 
            "lId": 1539676338558, 
            "lStart": 1539734400, 
            "lUpdate": 1539676338, 
            "sNote": "", 
            "vImageUrl": [ ], 
            "vStrUrlId": [
                "resource.search$10038"
            ]
        }
    ], 
    "vUIReminderCell": [ ]
}
```

##### 字段含义

| 字段名称                           | 字段类型 | 字段含义                         |
| ---------------------------------- | -------- | -------------------------------- |
| stCalendarData                     | Object   | 主数据字段，存放客户端需要的数据 |
| stCalendarData.sSpeakTips          | string   | 回复语字段，可选                 |
| stCalendarData.stBroadData         | Object   | 见 公共模块 の 播报语 部分       |
| stCalendarData.vAffectReminderCell | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vReminderCell       | Object   | 见 公共模块 の 数据列表 部分     |
| stCalendarData.vUIReminderCell     | Object   | 见 公共模块 の 数据列表 部分     |

### 公共模块

#### 领域内全局铃声

存放领域内全局铃声的信息

##### 示例

```json
[
    {
        "sBackgroundImageUrl": "http://soft.imtt.qq.com/browser/TBS/dingdang/resource_manager/cover/daji.jpg", 
        "sName": "妲己", 
        "sUrlId": "111111"
    }
]
```

##### 字段含义

| 字段名称            | 字段类型 | 字段含义           |
| ------------------- | -------- | ------------------ |
| sBackgroundImageUrl | string   | 铃声配套的图片资源 |
| sName               | string   | 铃声名称           |
| sUrlId              | string   | 铃声 ID            |

#### 播报语

存放提醒被触发时的播报语

##### 示例

```json
{
    "mBroadData": {
        "1539734400": "time##的提醒时间到了"
    }, 
    "mGatherBroadData": {
        "1539734400": {
            "eAISpeechType": 6, 
            "eAIVoiceTTSEngineType": 6, 
            "iCount": 0, 
            "sBroadInfo": "time##的提醒时间到了", 
            "vNote": [ ], 
            "vSoundRing": [ ]
        }
    }
}
```

##### 字段含义

| 字段名称         | 字段类型 | 字段含义                                                     |
| ---------------- | -------- | ------------------------------------------------------------ |
| mBroadData       | object   | 播报语信息                                                   |
| mBroadData.key   | string   | 响铃时间的时间戳字符串，单位 秒                              |
| mBroadData.value | string   | 事件发生时的播报语 `time##` 需要替换为真实的响铃时间。例如:"8点的提醒时间到了" |

#### 数据列表

返回三个数据列表，分别是：受本次请求影响的数据列表、本次终端需要展示的数据列表、全量数据列表

**上述三个数据列表均是可选状态，根据实际场景选用**

##### 示例

```json
"vAffectReminderCell": [ ], 
"vReminderCell": [
    {
        "eRepeatType": 1, 
        "lId": 1539676338558, 
        "lStart": 1539734400, 
        "lUpdate": 1539676338, 
        "sNote": "", 
        "vImageUrl": [ ], 
        "vStrUrlId": [
            "resource.search$10038"
        ]
    }
], 
"vUIReminderCell": [
    {
        "eRepeatType": 1, 
        "lId": 1539676338558, 
        "lStart": 1539734400, 
        "lUpdate": 1539676338, 
        "sNote": "", 
        "vImageUrl": [ ], 
        "vStrUrlId": [ ]
    }
]
```

##### 字段含义

| 字段名称            | 字段类型 | 字段含义                                        |
| ------------------- | -------- | ----------------------------------------------- |
| vAffectReminderCell | Array    | 受影响的数据列表，元组含义见 数据元组           |
| vReminderCell       | Array    | 全量数据列表，元组含义见 数据元组               |
| vUIReminderCell     | Array    | 根据请求条件命中的数据列表，元组含义见 数据元组 |

#### 数据元组

事件属性

##### 示例

```json
{                        
    "eRepeatType": 1, 
    "lId": 1539676338558, 
    "lStart": 1539734400, 
    "lUpdate": 1539676338, 
    "sNote": "", 
    "vImageUrl": [ ], 
    "vStrUrlId": [
        "resource.search$10038"
    ]
}
```

##### 字段含义

| 字段名称    | 字段类型 | 字段含义                             |
| ----------- | -------- | ------------------------------------ |
| eRepeatType | int      | 事件重复类型，见附录 E_REPEAT_TYPE   |
| lId         | long     | 事件唯一 ID, 由服务端生成            |
| lStart      | long     | 事件最近一次的触发时间，单位 秒      |
| sNote       | string   | 事件备注，例如“吃饭”、“喝水”         |
| vStrUrlId   | Array    | 事件铃声，响铃时需要以该资源ID，获取 |

### 附录

#### E_REPEAT_TYPE

```c++
enum E_REPEAT_TYPE{
    E_REPEAT_EXCEPT = 0, 		// 异常类型
    E_REPEAT_ONCE = 1, 			// 一次性
    E_REPEAT_DAY = 2, 			// 每天
    E_REPEAT_WEEK = 3, 			// 每周
    E_REPEAT_MONTH = 4, 		// 每月
    E_REPEAT_WORKDAY = 5, 		// 工作日
    E_REPEAT_WEEKEND = 6, 		// 节假日
};
```



