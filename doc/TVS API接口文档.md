# TVS API接口文档

**目录**

[TOCM]

[TOC]

# 1 Alert接口
Alert接口定义一系列指令和事件，用于设置、管理和取消timer、alarm和reminder。如遇网络中断或客户端与服务器时钟不同步时，您的客户端必须实现管理timer、alarm和reminder所需的必要逻辑。

## 1.1 状态图
下面的图表说明了由alert组件驱动的状态更改。框表示警报状态，连接器表示转换。

alert支持以下状态：

**IDLE**：在预先设定的alert开始之前，alert组件应该处于idle状态。alert一旦停止/结束，也应该返回到idle状态。这可能是用户语音、物理按键或GUI触发的结果。

**FOREGROUND ALERT**: 假设一个客户端的alert已经设置。当alert启动时，alert应该从idle状态转换到foreground状态，并且需要发送alertstarted事件到TVS。
只有当alert通道位于前台，dialog通道才处于非活跃状态。
当通过语音、按键、或GUI操作停止一个alert时，alert组件应该从foreground状态转换为idle状态。
alert响铃时，如果dialog通道被激活，alert组件应该从foreground状态转化为background状态。当dialog通道变成inactive时，alert应该返回到foreground状态，直到停止/完成。

**BACKGROUND ALERT**: 只有当dialog通道处于活动状态时，alert组件才转换到background状态。

![](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/img/tvs_alert_state.png)

## 1.2 Alerts上下文

TVS期望客户端上报每个本地存储的alert的状态，每个事件都需要上下文。alert被组织成两个列表：allAlerts和activeAlerts。allAlerts是本地存储的alert的完整列表。activeAlerts是当前用户选中的或正在响铃的alert列表。

**代码示例**
```java
{
    "header": {
        "namespace": "Alerts",
        "name": "AlertsState"
    },
    "payload": {
        "allAlerts": [
            {
                "token": "{{STRING}}",
                "type": "{{STRING}}",
                "scheduledTime": "{{STRING}}"
            }
        ],
        "activeAlerts": [
            {
                "token": "{{STRING}}",
                "type": "{{STRING}}",
                "scheduledTime": "{{STRING}}"
            }
        ]
    }
}
```

**有效负载参数**

| 参数                         | 描述                                     | 类型     |
| -------------------------- | -------------------------------------- | ------ |
| allAlerts                  | allAlerts的Key/value对                   | object |
| allAlerts.token            | 当设置alert时，TVS返回alert token。            | string |
| allAlerts.type             | 标识alert类型。接受值: TIMER, ALARM, REMINDER. | string |
| allAlerts.scheduledTime    | alert是按ISO 8601格式定义的。                  | string |
| activeAlerts               | activeAlerts的Key/value对。               | object |
| activeAlerts.token         | 当前正在触发的alert的token。                    | string |
| activeAlerts.type          | 标识alert类型. 接受值: TIMER or ALARM         | string |
| activeAlerts.scheduledTime | alert的间间是按ISO 8601格式定义的。               | string |

## 1.3 SetAlert指令
此指令指示客户端在指定的时间周期或时间内设置timer、alarm或reminder。您的客户端可能会收到一个设置alert的语音请求触发的SetAlert指令。
如果在有效负载中未指定loopCount参数，则alert必须响一小时或直到用户停止(语音请求或物理按键)。
云端提供的资源优先于本地存储的音频文件。如果提供了云端资源，则必须按照assetPlayOrder列表中的顺序为用户播放。否则，使用腾讯提供的默认音频文件。

如果assets.url[i]不可访问，或者如果客户端未能下载相关文件，则它应该播放由腾讯提供的与alert类型对应的默认音频文件，并遵循所提供的loopCount和loopPauseInMilliSeconds设置。

**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "Alerts",
            "name": "SetAlert",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "type": "{{STRING}}",
            "scheduledTime": "{{STRING}}",
            "assets": [
                {
                    "assetId": "{{STRING}}",
                    "url": "{{STRING}}"
                },
                {
                    "assetId": "{{STRING}}",
                    "url": "{{STRING}}"
                },
            ],
            "assetPlayOrder": [ {{LIST}} ],
            "backgroundAlertAsset": "{{STRING}}",
            "loopCount": {{LONG}},
            "loopPauseInMilliSeconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定message的唯一ID。                      | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |

**有效负载参数**

| 参数                      | 描述                                       | 类型     |
| ----------------------- | ---------------------------------------- | ------ |
| token                   | 用于唯一标识一个alert的不透明的token值.                | string |
| type                    | 标识alert类型. 如果一个未被识别的值被发送到客户端, 则取默认值ALARM. 接受值: TIMER, ALARM, REMINDER. | string |
| scheduledTime           | ISO 8601格式的alert的预定时间。                   | string |
| assets                  | 包含有要播放给用户的音频资源的列表。                       | list   |
| assets[i].assetId       | 音频资源的唯一ID。                               | string |
| assets[i].url           | 标识云中资源的URL。此资源可由客户端下载并缓存。提供的URL在alert的scheduledTime后的60分钟内有效。 | string |
| assetPlayOrder          | 必须播放的音频资源的顺序。列表由assetIds组成。注：i） assetIds可能在列表中多次出现。这种情况下，所有的assetIds都必须被播放。ii）如果客户端无法下载和缓存资源，您的设备应该使用腾讯提供的默认音频文件。 | list   |
| backgroundAlertAsset    | 如果存在的话，backgroundAlertAsset值将与asset列表中的一个assetId匹配。如果backgroundAlertAsset不包含在有效负载中，默认为腾讯提供的TVS音频文件。 | string |
| loopCount               | 每个资源序列必须被播放的次数。例如：如果值为2，则客户端必须循环两次assetPlayOrder。注意：如果有效负载中没有loopCount，则必须循环播放资源一小时，或者直到用户停止alert。 | long   |
| loopPauseInMilliSeconds | 每个资源循环之间的暂停时间。例如：如果loopPauseInMilliSeconds是300，loopCount是3，则客户端必须在每个资源循环之间暂停300毫秒。 | long   |

## 1.4 SetAlertSucceeded事件

当客户端成功设置alert时，在接收到SetAlert指令之后，必须将SetAlertSucceeded事件发送到TVS。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "SetAlertSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述                  | 类型     |
| --------- | ------------------- | ------ |
| messageId | 用于表示特定message的唯一ID。 | string |

**有效负载参数**

| 参数    | 描述                     | 类型     |
| ----- | ---------------------- | ------ |
| token | SetAlert指令提供的不透明token。 | string |

## 1.5 SetAlertFailed事件

当客户端无法设置alert时，必须在接收到SetAlert指令后将该SetAlertFailed事件发送到TVS。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "SetAlertFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述                  | 类型     |
| --------- | ------------------- | ------ |
| messageId | 用于表示特定message的唯一ID。 | string |

**有效负载参数**

| 参数    | 描述                     | 类型     |
| ----- | ---------------------- | ------ |
| token | SetAlert指令提供的不透明token。 | string |

## 1.6 DeleteAlert指令

该指令从TVS发送，指示您的客户端删除现有alert。 当语音请求取消/删除timer，alarm或reminder时，客户端可能会收到DeleteAlert指令。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "Alerts",
            "name": "DeleteAlert",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```
**Header参数**

| 参数              | 描述                               | 类型     |
| --------------- | -------------------------------- | ------ |
| messageId       | 用于表示特定message的唯一ID。              | string |
| dialogRequestId | 用于关联为响应特定Recognize事件而发送的指令的唯一ID。 | string |

**有效载荷参数**

| 参数    | 描述                 | 类型     |
| ----- | ------------------ | ------ |
| token | 一个唯一标识警报的不透明token。 | string |

## 1.7 DeleteAlertSucceeded事件

当客户端成功删除或取消现有alert时，必须在收到DeleteAlert指令后将DeleteAlertSucceeded事件发送到TVS。

**注意**: 有关何时发送DeleteAlertSucceeded事件的更多信息，请参阅alert概述。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "DeleteAlertSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述                  | 类型     |
| --------- | ------------------- | ------ |
| messageId | 用于表示特定message的唯一ID。 | string |

**有效载荷参数**

| 参数    | 描述                     | 类型     |
| ----- | ---------------------- | ------ |
| token | DeleteAlert指令提供的不透明令牌。 | string |

## 1.8 DeleteAlertFailed事件

当客户端无法删除或取消现有alert时，必须在收到DeleteAlert指令后将DeleteAlertFailed事件发送到TVS。

**注意**: 有关何时发送DeleteAlertFailed事件的更多信息，请参阅alert概述。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "DeleteAlertFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效载荷参数**

| 参数    | 描述                     | 类型     |
| ----- | ---------------------- | ------ |
| token | DeleteAlert指令提供的不透明令牌。 | string |

## 1.9 DeleteAlerts指令
该指令指示客户端删除产品上的所有现有alert。 每个alert由有效负载内的唯一令牌标识。 当语音请求取消/删除所有alert时，您的客户可能会收到DeleteAlerts指令。
如果无法删除一个或多个alert，则客户端必须回滚并向TVS发送DeleteAlertsFailed事件。 然后TVS将重试，直到删除所有alert，此时客户端必须发送DeleteAlertsSucceeded事件。

**注意**: 如果在客户端上找不到一个或多个alert的token，则客户端应继续删除所有匹配的token。 在这种情况下，此过程不会失败。 仅当无法删除产品上的一个或多个现有alert的token时，才应发送DeleteAlerts。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertEnteredBackground",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "tokens": ["{{STRING}}",...]
        }
    }
}
```

**Header参数**

| 参数              | 描述                               | 类型     |
| --------------- | -------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                   | string |
| dialogRequestId | 用于关联为响应特定Recognize事件而发送的指令的唯一ID。 | string |

**有效载荷参数**

| 参数     | 描述                           | 类型     |
| ------ | ---------------------------- | ------ |
| tokens | 一系列令牌。 每个标记都是一个唯一表示产品警报的字符串。 | string |

## 1.10 DeleteAlertsSucceeded事件

当客户端成功删除或取消令牌数组中的所有现有alert时，必须在收到DeleteAlerts指令后将DeleteAlertsSucceeded事件发送到TVS。

**注意**: 有关何时发送DeleteAlertsSucceeded事件的更多信息，请参阅alert概述。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertEnteredBackground",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "tokens": ["{{STRING}}",...]
        }
    }
}
```
**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数     | 描述                            | 类型     |
| ------ | ----------------------------- | ------ |
| tokens | 一系列令牌。 每个标记都是一个唯一表示客户端警报的字符串。 | string |

## 1.11 DeleteAlertsFailed事件

当客户端无法删除或取消token数组中的至少一个现有alert时，必须在收到DeleteAlerts指令后将DeleteAlertsFailed事件发送到TVS。

**注意**: 有关何时发送DeleteAlertsFailed事件的更多信息，请参阅alert概述。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertEnteredBackground",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "tokens": ["{{STRING}}",...]
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数     | 描述                           | 类型     |
| ------ | ---------------------------- | ------ |
| tokens | 一系列令牌。 每个标记都是一个唯一表示产品警报的字符串。 | string |

## 1.12 AlertStarted事件
当在其预定时间触发alert时，必须将AlertStarted事件发送到TVS。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertStarted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```
**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数    | 描述                  | 类型     |
| ----- | ------------------- | ------ |
| token | SetAlert指令提供的不透明令牌。 | string |

## 1.13 AlertStopped事件

当活动警报停止时，必须将AlertStopped事件发送到TVS。 在以下情况下停止警报：
1. 收到DeleteAlert指令。 发送AlertStopped事件后，如果使用DeleteAlertSucceeded事件或DeleteAlertFailed事件成功删除警报，则客户端必须通知TVS。 “alert概述”中说明了此交互。
2. 物理控件（硬件按钮或GUI）用于停止警报。
3. loopCount已完成，或者没有loopCount的警报已播放一小时并在本地停止。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertStopped",
            "messageId": "{STRING}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数    | 描述                  | 类型     |
| ----- | ------------------- | ------ |
| token | SetAlert指令提供的不透明令牌。 | string |

## 1.14 AlertEnteredForeground事件

当活动警报进入前台（以全音量播放）或在对话通道上的并发交互完成后重新进入前台时，必须将AlertEnteredForeground事件从您的客户端发送到TVS。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertEnteredForeground",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数    | 描述                  | 类型     |
| ----- | ------------------- | ------ |
| token | SetAlert指令提供的不透明令牌。 | string |

## 1.15 AlertEnteredBackground事件

当活跃的alert退出前台（衰减或暂停）时，例如在Dialog通道上发生的并发交互，必须从客户端向TVS发送AlertEnteredBackground事件。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "AlertEnteredBackground",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数    | 描述                   | 类型     |
| ----- | -------------------- | ------ |
| token | SetAlert指令中提供的不透明令牌。 | string |

## 1.16 SetVolume指令

该指令指示客户端设置alert的绝对音量级别。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "Alerts",
            "name": "SetVolume",
            "messageId": "{{STRING}}",
            "dialogRequestId": {{STRING}}
        },
        "payload": {
            "volume": "{{LONG}}"
        }
    }
}
```

**Header参数**

| 参数              | 描述                               | 类型     |
| --------------- | -------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                   | string |
| dialogRequestId | 用于关联为响应特定Recognize事件而发送的指令的唯一ID。 | string |

**有效负载参数**

| 参数     | 描述                                       | 类型   |
| ------ | ---------------------------------------- | ---- |
| volume | 绝对音量范围从0（最小）到100（最大）。 可接受的值：0到100之间的任何值，包括0和100。 | long |

## 1.17 AdjustVolume指令

该指令指示客户端调整alert的相对音量级别。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "Alerts",
            "name": "AdjustVolume",
            "messageId": "{{STRING}}",
            "dialogRequestId": {{STRING}}
        },
        "payload": {
            "volume": "{{LONG}}"
        }
    }
}
```

**Header参数**

| 参数              | 描述                               | 类型     |
| --------------- | -------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                   | string |
| dialogRequestId | 用于关联为响应特定Recognize事件而发送的指令的唯一ID。 | string |

**有效负载参数**

| 参数     | 描述                                       | 类型   |
| ------ | ---------------------------------------- | ---- |
| volume | 相对音量调整。正或负long类型值，用于相对于当前音量设置增加或减少音量。 可接受的值：介于-100和100之间的任何值。 | long |

## 1.18 VolumeChanged事件

收到SetVolume或AdjustVolume指令后，必须将此事件发送到TVS。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "Alerts",
            "name": "VolumeChanged",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "volume": "{{LONG}}"
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |


**有效负载参数**

|参数|描述|类型|
| --------    | -----      |  -----     |
|volume|这是您的产品在本地调整的音量。 可接受的值：音量必须是0（最小）和100（最大）之间的值，包括0和100。
**重要提示**：如果您的产品本地支持从0到10的音量调整，则必须将其缩放到0到100的范围。例如，当用户将音量增加到8时，TVS预期发送的音量值为80。|long|

# 2 AudioPlayer接口
AudioPlayer接口提供了通过语音控制音频播放的指令，以及用于管理和监控播放进度的事件。 如果您要将播放控件映射到按钮（物理或GUI），请参考PlaybackController接口。
## 2.1 状态图
下图说明了由AudioPlayer组件驱动的状态更改。 框表示AudioPlayer状态，连接器表示状态转换。
AudioPlayer具有以下状态：
**IDLE**: 当产品最初启动或重新启动时以及在执行Play指令之前，AudioPlayer仅处于idle状态。
**PLAYING**: 当您的客户端启动音频流播放时，AudioPlayer必须从idle状态转换为playing。
如果您收到指示客户端执行操作的指令，例如暂停或停止音频流，如果客户端无法缓冲流，或者如果播放失败，则AudioPlayer必须在执行操作时转换到适当的状态（并且向TVS发送事件）。 否则，AudioPlayer必须保持播放状态，直到当前流完成。
此外，在以下情况下，AudioPlayer必须保持播放状态：
- 向TVS报告播放进度
- 将流元数据发送到TVS
  **STOPPED**: 有四种情况，AudioPlayer必须转换到stopped状态。 在playing状态下，AudioPlayer必须在以下情况下转换为stopped：
- 遇到流问题，播放失败
- 客户端从TVS收到Stop指令
- 收到ClearQueue指令，其clearBehavior为CLEAR_ALL
- 接收到playBehavior为REPLACE_ALL的Play指令
  在暂停或buffer_underrun状态下，当接收到ClearQueuedirective到CLEAR_ALL时，AudioPlayer必须转换为stopped。
  每当您的客户端收到Play指令，开始播放音频流并向TVS发送PlaybackStarted事件时，AudioPlayer必须从stopped转换为playing。
  **PAUSED**: 当内容频道上的音频暂停以容纳更高优先级的输入/输出（例如用户或TVS语音）时，AudioPlayer必须转换到paused状态。 优先活动完成后，必须恢复播放。 有关确定音频输入/输出优先级的更多信息，请参阅交互模型。
  **BUFFER_UNDERRUN**: 当客户端的数据输入速度低于读取数据时，AudioPlayer必须转换到buffer_underrun状态。 AudioPlayer必须保持此状态，直到缓冲区足够恢复播放，此时它必须返回playing状态。
  **FINISHED**: 当流完成播放时，AudioPlayer必须转换到finished状态。 对于播放队列中的每个流都是如此。即使有排队播放的流，您的客户端也需要向TVS发送PlaybackFinished事件，然后在每个流播放完毕后从playing状态转换为finished状态。
  在以下情况下，AudioPlayer必须从finished转换到playing：
- 客户端收到Play指令
- 播放队列中的下一个流开始播放（播放PlaybackStarted事件之后）。

![](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/img/tvs_audioplayer_state.png)

## 2.2 AudioPlayer上下文

TVS希望客户端报告playerActivity（状态），以及当前正在播放的媒体项的offsetInMilliseconds以及需要上下文的每个事件。

**示例代码**
```java
{
    "header": {
        "namespace": "AudioPlayer",
        "name": "PlaybackState"
    },
    "payload": {
        "token": "{{STRING}}",
        "offsetInMilliseconds": {{LONG}},
        "playerActivity": "{{STRING}}"
    }
}
```

**有效负载参数**

| 参数                   | 描述                                       | 类型     |
| -------------------- | ---------------------------------------- | ------ |
| token                | 这必须与当前播放的媒体项的标记匹配。 否则，令牌必须与收到的最后一个Play指令中提供的令牌相匹配。 | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。  | long   |
| playerActivity       | 标识AudioPlayer的组件状态。 接受的值: IDLE, PLAYING, STOPPED, PAUSED, BUFFER_UNDERRUN, and FINISHED. | string |

| 播放器状态           | 描述                 |
| --------------- | ------------------ |
| IDLE            | 未播放任何内容，也有在队列中的内容。 |
| PLAYING         | 流正在播放。             |
| PAUSED          | 流被暂停了。             |
| BUFFER_UNDERRUN | 缓冲区不足。             |
| FINISHED        | 流播放结束。             |
| STOPPED         | 流被打断了。             |

## 2.3 Play指令
Play指令将发送到您的客户端以启动音频播放。 它是一个由JSON指令组成的多部分消息，最多包含一个音频流或二进制音频附件。

**注意**: 了解有关二进制音频附件的更多信息。
指令的有效负载中包含的playBehavior参数可用于确定客户端必须如何处理流的排队和回放。接受的值提供了必须采取的操作的提示：
- **REPLACE_ALL**: 立即开始播放使用Play指令返回的流，并替换当前和排队的流。 播放流时，如果您收到PlayBehavior为REPLACE_ALL的Play指令，则必须向TVS发送PlaybackStopped事件。
- **ENQUEUE**: 将流添加到当前队列的末尾。
- **REPLACE_ENQUEUED**: 替换队列中的所有流。 这不会影响当前播放的流。

**注意**: 将流添加到回放队列时，必须确保当前播放的流的标记与要添加到队列的流中的expectedPreviousToken匹配。 如果令牌不匹配，则必须忽略该流。 但是，如果未返回expectedPreviousToken，则必须将流添加到队列中。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "Play",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "playBehavior": "{{STRING}}",
            "audioItem": {
                "audioItemId": "{{STRING}}",
                "stream": {
                        "url": "{{STRING}}",
                        "streamFormat": "AUDIO_MPEG"
                        "offsetInMilliseconds": {{LONG}},
                        "expiryTime": "{{STRING}}",
                        "progressReport": {
                            "progressReportDelayInMilliseconds": {{LONG}},
                            "progressReportIntervalInMilliseconds": {{LONG}}
                        },
                        "token": "{{STRING}}",
                        "expectedPreviousToken": "{{STRING}}"
                }
            }
        }
    }
}
```

**二进制音频附件**

Play指令可以具有相应的二进制音频附件作为多部分消息的一部分。 当存在二进制音频附件时，为url提供的值将包括以下前缀：cid。
以下多部分标题将位于二进制音频附件之前：
```java
Content-Type: application/octet-stream
Content-ID: {{Audio Item CID}}

{{BINARY AUDIO ATTACHMENT}}
```

**Header参数**

| 参数              | 描述                               | 类型     |
| --------------- | -------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                   | string |
| dialogRequestId | 用于关联为响应特定Recognize事件而发送的指令的唯一ID。 | string |

**有效负载参数**

 **重要**: 您的客户端必须设计为适应并支持Play支持的所有有效负载参数，并且如果缺少JSON中的键/值对，则不得中断。

| 参数                                       | 描述                                       | 类型     |
| ---------------------------------------- | ---------------------------------------- | ------ |
| playBehavior                             | 提供播放提示。 可接受的值：REPLACE_ALL，ENQUEUE和REPLACE_ENQUEUED。 **REPLACE_ALL**：立即开始播放使用Play指令返回的流，并替换当前和排队的流。**ENQUEUE**：将流添加到当前队列的末尾。**REPLACE_ENQUEUED*：全部替换队列中的流。这不会影响当前播放的流。 | string |
| audioItem                                | 包含audioItems的键/值对。                       | object |
| audioItem.audioItemId                    | 标识audioItem。                             | string |
| audioItem.stream                         | 包含流的键/值对。                                | object |
| audioItem.stream.url                     | 标识音频内容的位置。 如果音频内容是二进制音频附件，则该值将是内容的唯一标识符，格式如下：“cid：”。 否则，该值将是远程http/https位置。 | string |
| audioItem.stream.streamFormat            | 当Playdirective具有关联的二进制音频附件时，streamFormat包含在有效负载中。 如果关联的音频是流，则不会出现此参数。 接受值: AUDIO_MPEG | string |
| audioItem.stream.offsetInMilliseconds    | 一个时间戳，指示客户端必须在流中的哪个位置开始播放。 例如，当offsetInMilliseconds设置为0时，这表示流的回放必须从0开始，或者从流的开始。 任何其他值表示播放必须从提供的偏移量开始。 | long   |
| audioItem.stream.expiryTime              | 流的过期时间，以ISO 8601格式定义。                    | string |
| audioItem.stream.progressReport          | 包含进度报告的键/值对。                             | object |
| audioItem.stream.progressReport. progressReportDelayInMilliseconds | 指定（以毫秒为单位）何时将ProgressReportDelayElapsed事件发送到TVS。 ProgressReportDelayElapsed只能以指定的间隔发送一次。 请注意：某些音乐提供商不需要此报告。 如果不需要报告，则progressReportDelayInMilliseconds不会出现在有效负载中。 | long   |
| audioItem.stream.progressReport. progressReportIntervalInMilliseconds | 指定何时（以毫秒为单位）向TVS发出ProgressReportIntervalElapsed事件。 必须以指定的时间间隔定期发送ProgressReportIntervalElapsed。 请注意：某些音乐提供商不需要此报告。 如果不需要报告，则progressReportIntervalInMilliseconds不会出现在有效负载中。 | long   |
| audioItem.stream.token                   | 表示当前流的不透明令牌。                             | string |
| audioItem.stream.expectedPreviousToken   | 一个不透明的标记，表示预期的上一个流。                      | string |

## 2.4 PlaybackStarted事件

在客户端处理Play指令并开始播放相关音频流后，必须将**PlaybackStarted**事件发送到TVS。

**注意**: 对于TVS发送的每个URL，它预期不会有多个PlaybackStarted事件。 如果您收到播放列表网址（由多个网址组成），则只发送一个PlaybackStarted事件。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackStarted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                     | 类型     |
| -------------------- | -------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                        | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.5 PlaybackNearlyFinished事件

当您的客户端准备缓冲/下载回放队列中的下一个流时，必须发送PlaybackNearlyFinished事件。 您的客户端必须确保仅在当前播放的流的PlaybackStarted事件之后发送此事件。 TVS将通过以下方式之一回应此事件：
- 包含下一个流的Play指令
- HTTP 204响应代码

**提示**: 作为最佳实践，您可能需要考虑等待上一首歌曲被缓冲，然后再向TVS发送PlaybackNearlyFinished事件。 这降低了超过expiryTime的风险，并且可以降低在同时下载和处理多个Play指令时可能发生的回放断断续续的频率。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackNearlyFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.6 ProgressReportDelayElapsed事件

如果Play指令中存在progressReportDelayInMilliseconds，则必须将ProgressReportDelayElapsed事件发送到TVS。 事件必须从流的开始以指定的间隔发送一次（而不是从offsetInMilliseconds）。 例如，如果Play指令包含值为20000的progressReportDelayInMilliseconds，则必须从轨道起点开始20,000毫秒发送ProgressReportDelayElapsed事件。 但是，如果Play指令包含offsetInMilliseconds值10000和progressReportDelayInMilliseconds值20000，则必须将该事件发送到播放10,000毫秒。 这是因为进度报告是从流的开头发送的，而不是Play指令的偏移量。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "ProgressReportDelayElapsed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.7 ProgressReportIntervalElapsed事件

如果Play指令中存在progressReportIntervalInMilliseconds，则必须将ProgressReportIntervalElapsed事件发送到TVS。 必须从流的开始（而不是offsetInMilliseconds）以指定的间隔定期发送事件。 例如，如果Play指令包含值为20000的progressReportIntervalInMilliseconds，则必须在轨道开始后20,000毫秒发送ProgressReportIntervalElapsed事件，并且每隔20,000毫秒发送一次，直到流结束。 但是，如果Play指令包含offsetInMilliseconds值为10000且progressReportIntervalInMilliseconds值为20000，则必须在播放开始后10,000毫秒发送事件，之后每隔20,000毫秒发送一次，直到流结束。 这是因为指定的间隔来自流的开头，而不是Play指令的偏移量。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "ProgressReportIntervalElapsed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.8 PlaybackStutterStarted事件

PlaybackStutterStarted事件必须在PlaybackStarted事件之后发送到TVS，此时客户端的AudioPlayer组件的数据输入速度比读取时慢。 一旦发送此事件，组件必须转换到buffer_underrun状态，并保持此状态，直到缓冲区足够恢复播放。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackStutterStarted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.9 PlaybackStutterFinished事件

当缓冲区足够满足以恢复流的回放时，必须将PlaybackStutterFinished事件发送到TVS。 当音频播放恢复时，TVS不期望后续的PlaybackStarted事件。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackStutterFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}},
            "stutterDurationInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                            | 描述                                      | 类型     |
| ----------------------------- | --------------------------------------- | ------ |
| token                         | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds          | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |
| stutterDurationInMilliseconds | 标识播放不连贯的持续时间（以毫秒为单位）。                   | long   |

## 2.10 PlaybackFinished事件

当您的客户端完成流的播放时，必须将PlaybackFinished事件发送到TVS。
在以下情况下不会发送此事件：
- 停止播放（本地按键或Stop指令的结果）
- 在流之间切换换（下一个/上一个）

**注意**：对于TVS发送的每个URL，它预期收到不超过一个PlaybackFinished事件。 如果您收到播放列表网址（由多个网址组成），则只发送一个PlaybackFinished事件。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.11 PlaybackFailed事件

每当您的客户端在尝试播放流时遇到错误，都必须将PlaybackFailed事件发送到TVS。 在流正在播放且下一个流无法缓冲的情况下，currentPlaybackToken可能与有效负载中的令牌不同。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "currentPlaybackState": {
                "token": "{{STRING}}",
                "offsetInMilliseconds": {{LONG}},
                "playerActivity": "{{STRING}}"
            },
            "error": {
                "type": "{{STRING}}",
                "message": "{{STRING}}"
            }
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数                                 | 描述                                       | 类型     |
| ---------------------------------- | ---------------------------------------- | ------ |
| token                              | Play指令提供的不透明令牌，表示无法播放的流。                 | string |
| currentPlaybackState               | 包含playbackState对象的键/值对。                  | object |
| playbackState.token                | Play指令提供的不透明令牌。                          | string |
| playbackState.offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。  | long   |
| playbackState.playerActivity       | 标识播放器状态。 可接受的值： PLAYING, STOPPED, PAUSED, FINISHED, BUFFER_UNDERRUN, or IDLE. | string |
| error                              | 包含错误消息的键/值对。                             | object |
| error.type                         | 标识特定类型的错误。 下表提供了每种错误类型的详细信息。             | string |
| error.message                      | 设备遇到的错误的描述。这仅用于记录目的。对于HTTP相关错误，错误消息应包含HTTP错误响应正文（如果存在）。 | string |

**错误类型**

| 取值                                | 描述                                   |
| --------------------------------- | ------------------------------------ |
| MEDIA_ERROR_UNKNOWN               | 出现未知错误。                              |
| MEDIA_ERROR_INVALID_REQUEST       | 服务器将请求识别为格式错误。 例如。 错误请求，未经授权，禁止，未找到等 |
| MEDIA_ERROR_SERVICE_UNAVAILABLE   | 客户端无法访问该服务。                          |
| MEDIA_ERROR_INTERNAL_SERVER_ERROR | 服务器接受了请求，但无法按预期处理请求。                 |
| MEDIA_ERROR_INTERNAL_DEVICE_ERROR | 客户端出现内部错误。                           |

## 2.12 Stop指令

Stop指令将发送到您的客户端以停止播放音频流。 您的客户可能会因语音请求，物理按键按下或GUI启动而收到Stop指令。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "Stop",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Header参数**

| 参数              | 描述                               | 类型     |
| --------------- | -------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                   | string |
| dialogRequestId | 用于关联为响应特定Recognize事件而发送的指令的唯一ID。 | string |

## 2.13 PlaybackStopped事件

当您的客户端收到以下指令之一并停止播放音频流时，必须将PlaybackStopped事件发送到TVS：
- Stop指令
- Play指令，其playBehavior为REPLACE_ALL
- ClearQueue指令，其clearBehavior为CLEAR_ALL

**注意**: 仅当由于接收到上面列出的指令之一而终止流时才会发送此事件。 通常，这是用户操作的结果。 当流完成播放时，不得发送此事件（请参阅PlaybackFinished）。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackStopped",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令提供的不透明令牌。                         | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.14 PlaybackPaused事件

当您的客户端暂时暂停内容频道上的音频以适应更高优先级的输入/输出时，必须发送PlaybackPaused事件。 当优先活动完成时，必须恢复播放; 此时您的客户端必须发送PlaybackResumed事件。 有关确定音频输入/输出优先级的更多信息，请参阅交互模型。

**注意**: 应该在Recognize事件之后发送PlaybackPaused以减少延迟。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackPaused",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令中提供的不透明令牌。                        | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.15 PlaybackResumed事件

播放在PlaybackPaused事件之后恢复时（当在内容频道暂时暂停播放以容纳更高优先级的输入/输出时），必须将PlaybackResumed事件发送到TVS。 有关确定音频输入/输出优先级的更多信息，请参阅交互模型。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackResumed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "offsetInMilliseconds": {{LONG}}
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                   | 描述                                      | 类型     |
| -------------------- | --------------------------------------- | ------ |
| token                | Play指令中提供的不透明令牌。                        | string |
| offsetInMilliseconds | 标识轨道的当前偏移（以毫秒为单位）。 发送的值必须等于或大于零。 不接受负值。 | long   |

## 2.16 ClearQueue指令

ClearQueue指令从TVS发送到您的客户端以清除回放队列。 ClearQueuedirective有两个行为：CLEAR_ENQUEUED，它清除队列并继续播放当前播放的流; 和CLEAR_ALL，它清除整个回放队列并停止当前播放的流（如果适用的话）。

**示例代码**
```java
{
    "directive": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "ClearQueue",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "clearBehavior": "{{STRING}}"
        }
    }
}
```

**Header参数**

|参数|描述|类型|
| --------    | -----      |  -----     |
|messageId|用于表示特定消息的唯一ID。|string
|dialogRequestId|用于关联为响应特定Recognize事件而发送的指令的唯一ID。|string|

**有效负载参数**

| 参数            | 描述                                       | 类型     |
| ------------- | ---------------------------------------- | ------ |
| clearBehavior | 用于确定清除队列行为的字符串值。 可接受的值：CLEAR_ENQUEUED和CLEAR_ALL | string |

## 2.17 PlaybackQueueCleared事件

在客户端处理ClearQueue指令后，必须将PlaybackQueueCleared事件发送到TVS。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "PlaybackQueueCleared",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

必须发送空的有效负载。

## 2.18 StreamMetadataExtracted事件

如果元数据可用于客户端接收并开始播放的音频流：您的客户端应将接收的键/值对作为原始数据并将这些对转换为JSON对象。 在此JSON对象中，字符串和数字应表示为JSON字符串，而布尔值应表示为JSON布尔值。 您的客户应过滤掉包含二进制数据的任何标签。 例如，您的客户端不应将图像，图像预览，附件或应用程序数据标签发送到TVS。

**示例代码**
```java
{
    "event": {
        "header": {
            "namespace": "AudioPlayer",
            "name": "StreamMetadataExtracted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "metadata": {
                "{{STRING}}": "{{STRING}}",
                "{{STRING}}": {{BOOLEAN}}
                "{{STRING}}": "{{STRING NUMBER}}"
            }
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

| 参数       | 描述                | 类型     |
| -------- | ----------------- | ------ |
| token    | Play指令提供的不透明令牌。   | string |
| metadata | 包含与收到的元数据关联的键/值对。 | object |




# 3 Notifications接口

TVS可以使用Notifications接口通知用户领域/技能有新内容。具体来说，本接口公开了两个指令，指示客户端为用户呈现、清除视觉和音频指示器。
此接口不提供通知内容，它仅提供用于通知用户新内容可用的音频/视觉指示器。例如，产品可能会闪烁黄色LED并播放音频文件，此时用户可以通过询问“叮当叮当，我错过了什么？”来检索任何待处理的通知。 或者“叮当叮当，我的通知是什么？”
有关流量和传送，请勿打扰设置和UX注意事项的信息，请参阅通知概述。
## 3.1 Notifications 上下文

TVS希望客户端在上报Context中带上通知指示器的状态。

有关Context的详细信息，请参阅Context概述。


**代码示例**

```java
{
    "header": {
        "namespace": "Notifications",
        "name": "IndicatorState"
    },
    "payload": {
        "isEnabled": {{BOOLEAN}},
        "isVisualIndicatorPersisted": {{BOOLEAN}}
    }
}
```


**有效负载参数**

| 参数                         | 描述                                       | 类型      |
| -------------------------- | ---------------------------------------- | ------- |
| isEnabled                  | 表示尚未向用户传达新的或待处理的通知。 注意：任何尚未清除的指标都被视为已启用。 | boolean |
| isVisualIndicatorPersisted | 对应于最后收到的SetIndicator指令的persistVisualIndicator值。 如果对于收到的最后一个指令，persistVisualIndicator为true，则在重新连接时，isVisualIndicatorPersisted必须为true。 | boolean |

## 3.2 SetIndicator指令

此指令指示客户端在可以检索通知时呈现可视和音频指示符。客户端可能会在短时间内收到多个SetIndicator指令。如果指令重叠，请考虑这些规则：
- 如果当前指令的assetId与传入指令的assetId匹配，则不要播放asset。
- 如果当前指令的assetId与传入指令的assetId不匹配，则在播放完当前asset后，播放传入指令的asset。
  **代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "Notifications",
            "name": "SetIndicator",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "persistVisualIndicator": {{BOOLEAN}},
            "playAudioIndicator": {{BOOLEAN}},
            "asset": {
                "assetId": "{{STRING}}",
                "url": "{{STRING}}"
            }
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                     | 描述                                       | 类型      |
| ---------------------- | ---------------------------------------- | ------- |
| persistVisualIndicator | 指定在处理此指令后，产品是否必须显示持久性视觉指示器（如果适用）。        | boolean |
| playAudioIndicator     | 指定在处理此指令时，产品是否必须播放音频指示器。                 | boolean |
| asset                  | 包含有关playAudioIndicator为true时必须播放的音频资源的信息。 | object  |
| asset.assetId          | 资源标识。                                    | string  |
| asset.url              | 资源URL。客户端可以下载和缓存本资源。 提供的URL有效期为60分钟。 如果产品处于脱机状态，或者资源不可用，则产品应播放默认指示灯。 | string  |

## 3.3  ClearIndicator 指令

该指令指示客户端清除所有活动的视觉、音频指示器。
- 如果收到此指令时正在播放音频指示器，则应立即停止。
- 如果在收到此指令时设置了任何视觉指示器，则应立即清除它们。
  **代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "Notifications",
            "name": "ClearIndicator",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**
本指令的payload为空。

# 4 PlaybackController接口

PlaybackController接口公开了一系列事件，用于通过客户端按钮或者GUI来导航回放队列，而不是通过语音请求。
## 4.1 PlayCommandIssued事件

当用户使用客户端启动/恢复按钮或GUI启动/恢复媒体播放时，必须发送PlayCommandIssued事件。
**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.       
    ],   
    "event": {
        "header": {
            "namespace": "PlaybackController",
            "name": "PlayCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Context**

本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。



**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

应发送空的有效负载。

## 4.2 PauseCommandIssued事件

当用户使用按钮或GUI暂停正在播放的媒体时，必须发送PauseCommandIssued事件。
**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.      
    ],    
    "event": {
        "header": {
            "namespace": "PlaybackController",
            "name": "PauseCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Context**

本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |


**有效负载参数**

应发送空的有效负载。

## 4.3 NextCommandIssued事件

当用户使用按钮或GUI跳到其播放队列中的下一个媒体时，必须发送NextCommandIssued事件。
**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.     
    ],     
    "event": {
        "header": {
            "namespace": "PlaybackController",
            "name": "NextCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Context**
本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。



**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

应发送空的有效负载。

## 4.4 PreviousCommandIssued事件

当用户使用按钮或GUI时跳到其播放队列中的上一个媒体时，必须发送PreviousCommandIssued事件。
**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.       
    ],     
    "event": {
        "header": {
            "namespace": "PlaybackController",
            "name": "PreviousCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Context**

本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。



**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

应发送空的有效负载。

## 4.5 ButtonCommandIssued事件

此事件用于向TVS通知客户端的按钮或GUI被触发，例如向前或向后按钮被按下。 跳过持续时间由提供者/技能确定，并且每个事件都是附加的。 例如，如果用户连续三次按下向前按钮，结果三个ButtonCommandIssued事件被发送到TVS，则加起来（如果跳过时间为30秒）将是90秒。

**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.
    ],
    "event": {
        "header": {
            "namespace": "PlaybackController",
            "name": "ButtonCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "name": "{{STRING}}"
        }
    }
}
```

**Context**

本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。



**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数   | 描述                                       | 类型     |
| ---- | ---------------------------------------- | ------ |
| name | 指定按钮/GUI触发的命令。可接受的值：SKIPFORWARD，SKIPBACKWARD。 | string |

## 4.6 ToggleCommandIssued事件

此事件用于通知TVS客户端已使用按钮或GUI选择或取消选项或功能。 支持的选项包括：shuffle，loop，repeat，thumbs up和thumbs down。
**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.
    ],
    "event": {
        "header": {
            "namespace": "PlaybackController",
            "name": "ToggleCommandIssued",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "name": "{{STRING}}"
            "action": "{{STRING}}"
         }
    }
}
```

**Context**

本事件要求客户端将所有终端的状态发送到TVS。 有关其他信息，请参阅Context。


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数     | 描述                                       | 类型     |
| ------ | ---------------------------------------- | ------ |
| name   | 指定由客户端按下按钮或GUI切换的选项/功能。 接受的值：SHUFFLE，LOOP，REPEAT，THUMBSUP，THUMBSDOWN。 | string |
| action | 指示是否已选择或取消选择。 接受的值：SELECT，DESELECT。      | string |


# 5 Settings接口

Settings接口用于管理产品上的TVS设置，例如区域设置。
## 5.1 SettingsUpdated事件

使用产品上的控制面板或配套应用程序调整TVS设置时，必须发送SettingsUpdated事件。 例如，您的用户可以使用您的配套应用将其区域设置从美国（en-US）更改为德国（de-DE）。 发生这种情况时，您的产品必须通过SettingsUpdated事件通知TVS更改。
注意：如果向TVS发送格式错误或不受支持的值，则会返回异常消息。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "Settings",
            "name": "SettingsUpdated",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "settings": [
                {
                    "key": "{{STRING}}",
                    "value": "{{STRING}}"
                }
            ]
        }    
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数       | 描述                                | 类型     |
| -------- | --------------------------------- | ------ |
| settings | 产品的TVS设置选项列表。 列表中的每一项都是具有键/值对的对象。 | list   |
| key      | 键标识. 使用下表可确定接受的键。                 | string |
| value    | 键的值. 使用下表可确定键对应的值。                | string |

**可接受的键/值对**

| 可接收的键  | 可接受的值                                    |
| ------ | ---------------------------------------- |
| locale | de-DE, en-AU, en-CA, en-GB, en-IN, en-US, fr-FR, ja-JP |

# 6 Speaker接口


Speaker接口提供了用于调整音量、静音/取消静音的指令和事件。 TVS支持两种音量调节方法：1. 通过SetVolume指令;2. 通过AdjustVolume指令。
## 6.1 Speaker Context

TVS希望客户端在Context中上报Speaker接口的音量和静音状态信息。有关上报Context的详细信息，请参阅Context概述。
**代码示例**
```java
{
    "header": {
        "namespace": "Speaker",
        "name": "VolumeState"
    },
    "payload": {
        "volume": {{LONG}},
        "muted": {{BOOLEAN}}
    }
}
```


**有效负载参数**

| 参数     | 描述                    | 类型      |
| ------ | --------------------- | ------- |
| volume | 当前扬声器的音量。可接受的值：0-100。 | long    |
| muted  | 当前扬声器是否静音。            | boolean |

## 6.2 SetVolume指令

该指令指示终端进行绝对音量调整。 音量值将介于0（最小）和100（最大）之间。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "Speaker",
            "name": "SetVolume",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "volume": {{LONG}}
        }
    }
}
```


**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |



**有效负载参数**

| 参数     | 描述                                       | 类型   |
| ------ | ---------------------------------------- | ---- |
| volume | 绝对音量值，从0（分钟）到100（最大）。 可接受的值：0到100之间的任何值，包括0或者100。 | long |

## 6.3 AdjustVolume指令

该指令指示终端进行相对音量调整。 音量值介于-100和100之间。
AdjustVolume指令始终相对于当前音量设置，增加音量为正数，减小音量为负数。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "Speaker",
            "name": "AdjustVolume",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "volume": {{LONG}}
        }
    }
}
```


**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |



**有效负载参数**

| 参数     | 描述                                       | 类型   |
| ------ | ---------------------------------------- | ---- |
| volume | 调整的相对音量。正数、负数分别用来增加、减小当前音量。可接受的值：介于-100和100之间的任何值，包括-100/100。 | long |

## 6.4 VolumeChanged事件
在以下情况下，必须将VolumeChanged事件发送到TVS：
- 接收并处理SetVolume或AdjustVolume指令，以指示产品上的扬声器音量已被调整/更改。
- 音量在本地调整，以指示的扬声器音量已经调整/更改。
  **重要**：音量必须是介于0（分钟）和100（最大）之间的值。 如果您的产品本地支持从0到10的音量调节，当用户将音量增加到8时，发送给TVS的音量值应为80。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "Speaker",
            "name": "VolumeChanged",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "volume": {{LONG}},
            "muted": {{BOOLEAN}}
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数     | 描述                                       | 类型      |
| ------ | ---------------------------------------- | ------- |
| volume | 从0（分钟）到100（最大）的绝对音量。 可接受的值：0到100之间的任何整数值 | long    |
| mute   | 布尔值表示扬声器是否静音。 扬声器静音时该值为true，取消静音时为false。 | boolean |

## 6.5 SetMute 指令

此指令从TVS发送到客户端，以使扬声器静音。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "Speaker",
            "name": "SetMute",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "mute": {{BOOLEAN}}
        }
    }
}
```


**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |



**有效负载参数**

| 参数   | 描述                                       | 类型      |
| ---- | ---------------------------------------- | ------- |
| mute | 布尔值用于设置扬声器是否需要静音。 扬声器静音时该值为true，取消静音时为false。 | boolean |

## 6.6 MuteChanged 事件


在下列情况下，必须将MuteChanged事件发送到TVS：

- 接收并处理SetMute指令，表示产品扬声器的静音状态已更改。
- 您的产品在本地静音/取消静音，表示产品扬声器的静音状态已更改。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "Speaker",
            "name": "MuteChanged",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "volume": {{LONG}},
            "muted": {{BOOLEAN}}
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数     | 描述                                       | 类型      |
| ------ | ---------------------------------------- | ------- |
| volume | 从0（分钟）到100（最大）的绝对音量。 可接受的值：0到100之间的任何整数值。 | long    |
| mute   | 布尔值表示扬声器是否静音。 扬声器静音时该值为true，取消静音时为false。 | boolean |

# 7 SpeechRecognizer 接口


每个用户语音交互都会用到SpeechRecognizer。 它是腾讯语音服务（TVS）的核心接口，提供了用于捕获用户语音的指令和事件，并在TVS需要额外的语音输入时提示客户端。
此外，此接口还允许您的客户通知TVS互动是怎么启动的（按住，点按和释放，语音唤醒启动），并为您的产品选择合适的自动语音识别（ASR）配置文件 ，允许TVS理解用户语音并准确回应。

## 7.1 状态图


下图说明了SpeechRecognizer状态流转图。框表示SpeechRecognizer状态，连线表示状态转换。
SpeechRecognizer具有以下状态：

** IDLE （空闲）**：在捕获用户语音之前，SpeechRecognizer应处于空闲状态。在与TVS的语音交互结束后，SpeechRecognizer也应该返回到空闲状态。成功处理语音请求或ExpectSpeechTimedOut事件出现，可能会发生这种情况。
另外，SpeechRecognizer可以在多轮交互期间返回到空闲状态，此时，如果TVS需要用户的语音输入，它应该从IDLE状态转换到期望语音状态而无需用户主动开始新的交互。
**RECOGNIZING（识别）**：当用户开始与您的客户端进行交互时，特别是当捕获的音频流式传输到TVS时，SpeechRecognizer应该从空闲状态转换到识别状态。它应保持在识别状态，直到客户端停止录制语音（或流式传输完成），此时您的SpeechRecognizer应从识别状态转换为忙碌状态。
**BUSY（忙碌）**：处理语音请求时，SpeechRecognizer应处于忙碌状态。在组件转出忙碌状态之前，您无法启动另一个语音请求。从忙状态，如果请求被成功处理（完成），则SpeechRecognizer将转换到空闲状态，或者如果TVS需要来自用户的额外语音输入，则SpeechRecognizer将转换到期望语音状态。
**EXPECTING SPEECH（期望语音）**：当用户需要额外的音频输入时，SpeechRecognizer应处于期望语音状态。从期望语音开始，SpeechRecognizer应当在用户交互发生时转换到识别状态，或者代表用户自动开始交互。如果在指定的时间内未检测到用户交互，则应转换为空闲状态。
![](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/img/tvs_speechrecognizer_state.png)

## 7.2 SpeechRecognizer 上下文

如果启用了语音唤醒功能，TVS希望所有客户端报告当前设置的唤醒词。
**代码示例**
```java
{
    "header": {
        "namespace": "SpeechRecognizer",
        "name": "RecognizerState"
    },
    "payload": {
        "wakeword": "DING1DANG1DING1DANG"
    }
}
```

**有效负载参数**

| 参数       | 描述                                  | 类型     |
| -------- | ----------------------------------- | ------ |
| wakeword | 表示当前唤醒词，接受的值："DING1DANG1DING1DANG"。 | string |

## 7.3 Recognize 事件

Recognize事件用于将用户语音发送到TVS并将该语音转换为一个或多个指令。 此事件必须作为 multipart消息发送：第一部分是JSON格式的对象，第二部分是麦克风捕获的二进制音频。 我们鼓励将采用chunked编码方式分片传输音频流到腾讯语音服务，以减少延迟; 每块语音流应包含10ms（320字节）的音频。
在启动与TVS的交互后，麦克风必须保持打开状态，直到：
- 收到StopCapture指令。
- TVS服务关闭了该流。
- 用户手动关闭麦克风。 例如，按住说话方案。
  profile参数和initiator参数用来告诉TVS应使用哪种ASR配置最好地识别所发送的音频，以及TVS交互如何初始化。
  发送到TVS的音频应编码为：
- 16bit Linear PCM
- 16kHz 比特率
- 单声道
- 小端字节序

**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.      
    ],   
    "event": {
        "header": {
            "namespace": "SpeechRecognizer",
            "name": "Recognize",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "profile": "{{STRING}}",
            "format": "{{STRING}}",
            "initiator": {
                "type": "{{STRING}}",
                "payload": {
                    "wakeWordIndices": {
                        "startIndexInSamples": {{LONG}},
                        "endIndexInSamples": {{LONG}}
                    },
                    "token": "{{STRING}}"   
                }
            }
        }
    }
}
```

**二进制音频附件Binary Audio Attachment**

每个Recognize事件都需要相应的二进制音频附件作为multipart消息的一部分。 每个二进制音频附件都需要以下标头：
```java
Content-Disposition: form-data; name="audio"
Content-Type: application/octet-stream

{{BINARY AUDIO ATTACHMENT}}
```

**Context**

本事件要求产品在Context对象中向TVS报告客户端所有状态。
**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |



**有效负载参数**

| 参数                                       | 描述                                       | 类型     |
| ---------------------------------------- | ---------------------------------------- | ------ |
| profile                                  | 标识识产品关联的语音识别（ASR）配置。 TVS针对不同距离的用户语音优化了三种不同的ASR引擎。 可接受的值：CLOSE_TALK，NEAR_FIELD，FAR_FIELD。 | string |
| format                                   | 标识音频格式。可接受的值：AUDIO_L16_RATE_16000_CHANNELS_1。 | string |
| initiator                                | 让TVS知道如何启动交互。当用户主动发起交互时（语音唤醒，点击，按下和保持），此对象是必需的。如果ExpectSpeech指令中存在initiator，则必须在随后的Recognize事件中带上它。如果ExpectSpeech指令中不存在initiator，则它不应包含在随后的Recognize事件中。 | object |
| initiator.type                           | 表示用户启动交互所采取的操作类型。 可接受的值：PRESS_AND_HOLD，TAP和WAKEWORD。 如果ExpectSpeech指令中提供了initiator.type，则该字符串必须在以下Recognize事件中作为initiator.type返回。 | string |
| initiator.payload                        | 包括有关启动器的信息。                              | object |
| initiator.payload.wakeWordIndices        | 当initiator.type设置为WAKEWORD时，此对象是必需的。 wakeWordIndices包括startIndexInSamples和endIndexInSamples。 有关其他详细信息，请参阅云端唤醒验证的要求。 | object |
| initiator.payload.wakeWordIndices.startIndexInSamples | 表示唤醒词在音频流中开始位置（样本数）。 开始位置应精确到唤醒词检测开始的50ms以内。 | long   |
| initiator.payload.wakeWordIndices.endIndexInSamples | 表示唤醒词在音频流中结束位置（样本数）。 结束位置应精确到唤醒词检测结束的的150ms以内。 | long   |
| initiator.payload.token                  | token。 当前面的ExpectSpeech指令的有效负载中存在此值时才需要此值。 | string |

**Profiles**
ASR配置文件针对不同的产品，外形，声学环境和使用案例进行了调整。 使用下表了解有关profile参数的可接受值的更多信息。

| 值          | 最优距离         |
| ---------- | ------------ |
| CLOSE_TALK | 0 to 2.5 ft. |
| NEAR_FIELD | 0 to 5 ft.   |
| FAR_FIELD  | 0 to 20+ ft. |

**Initiator**

initiator参数告诉TVS交互是如何触发的，并确定两件事：
1.如果在云端检测到语音结束后，StopCapture将被发送给您的客户端。
2.如果要在语音流上执行基于云的唤醒词验证。initiator必须包含在每个SpeechRecognizer.Recognize事件的有效负载中。 接受以下值：

| 值              | 描述                                       | 支持的Profile(s)         | 是否支持StopCapture | 是否校验唤醒词Wake Word Verification Enabled | 是否要求唤醒词偏移Wake Word Indices Required |
| -------------- | ---------------------------------------- | --------------------- | --------------- | ------------------------------------- | ----------------------------------- |
| PRESS_AND_HOLD | 通过按下按钮（物理按键或GUI）启动音频流，并通过释放它停止。          | CLOSE_TALK            | N               | N                                     | N                                   |
| TAP            | 音频流由点击和释放按钮（物理或GUI）启动，并在收到StopCapture指令时终止。 | NEAR_FIELD, FAR_FIELD | Y               | N                                     | N                                   |
| WAKEWORD       | 通过语音唤醒启动的音频流，并在收到StopCapture指令时终止。       | NEAR_FIELD, FAR_FIELD | Y               | Y                                     | Y                                   |

## 7.4 StopCapture 指令




该指令指示客户端在TVS识别出用户的意图或检测到结束语后停止捕获用户的语音。 收到此指令后，客户端必须立即关闭麦克风并停止收听用户的语音。
**注意**：StopCapture在下行通道发送到客户端，并且可能在语音仍然向TVS流式传输接收。 要接收StopCapture指令，必须在Recognize事件中配置profile支持云端检测结束，例如NEAR_FIELD或FAR_FIELD。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "SpeechRecognizer",
            "name": "StopCapture",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```


**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |

## 7.5 ExpectSpeech 指令

当TVS需要额外信息来满足用户的请求时，会发送ExpectSpeech。 它指示客户端打开麦克风并开始流式传输用户语音。 如果未在指定的超时窗口内打开麦克风，则必须从客户端向TVS发送ExpectSpeechTimedOut事件。
在与TVS进行多轮交互期间，您的设备将至少收到一条ExpectSpeech指令，指示客户端开始收音。 如果存在，则必须将ExpectSpeech指令的有效内容中包含的启动器对象作为以下Recognize事件中的启动器对象传递回TVS。 如果有效负载中不存在启动器，则以下Recognize事件不应包含启动器。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "SpeechRecognizer",
            "name": "ExpectSpeech",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "timeoutInMilliseconds": {{LONG}},
            "initiator": {
                "type": "{{STRING}}",
                "payload": {
                    "token": "{{STRING}}"
                }
            }
        }
    }
}
```


**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |



**有效负载参数**

| 参数                      | 描述                                       | 类型     |
| ----------------------- | ---------------------------------------- | ------ |
| timeoutInMilliseconds   | 指定客户端应等待麦克风打开并开始将用户语音流式传输到TVS的时间（以毫秒为单位）。 如果未在指定的超时时间内打开麦克风，则必须发送ExpectSpeechTimedOut事件。 此行为的主要用例是PRESS_AND_HOLD方案。 | long   |
| initiator               | 包含有关交互的信息。 如果存在，必须在后续Recognize事件中将其发送回TVS。 | object |
| initiator.type          | 不透明的字符串。 如果存在，必须在后续Recognize事件中将其发送回TVS。 | string |
| initiator.payload       | 包含有关initiator的信息                         | object |
| initiator.payload.token | 不透明的字符串。如果存在，必须在后续Recognize事件中将其发送回TVS。  | string |

## 7.6 ExpectSpeechTimedOut 事件

如果收到ExpectSpeech指令，但在指定的超时时间内没有执行，则必须将此事件发送到TVS，
**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "SpeechRecognizer",
            "name": "ExpectSpeechTimedOut",
            "messageId": "{{STRING}}",
        },
        "payload": {
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

**有效负载参数**

应发送空的有效负载。


# 8 SpeechSynthesizer 接口

当用户向您的产品询问或提出请求时，SpeechSynthesizer接口用于返回TVS的语音响应。 例如，当用户问TVS时，“上海的天气怎么样？” TVS语音服务将向客户端返回Speak指令，并带有二进制音频附件，客户端应该处理、播放该附件。 本部分包含SpeechSynthesizer指令和事件。
## 8.1 状态

SpeechSynthesizer具有以下状态：
**PLAYING(播放)**：当TVS讲话时，SpeechSynthesizer应该处于播放状态。 当TVS语音的播放完成时，SpeechSynthesizer应转换到完成状态。
**FINISHED(完成)**：当TVS讲完后，SpeechSynthesizer应该在SpeechFinished事件之后转换到完成状态。
## 8.2 SpeechSynthesizer 上下文

TVS希望客户端在Context中上报播放器状态（状态），以及当前正在播放的TTS的offsetInMilliseconds。
**代码示例**
```java
{
    "header": {
        "namespace": "SpeechSynthesizer",
        "name": "SpeechState"
    },
    "payload": {
        "token": "{{STRING}}",
        "offsetInMilliseconds": {{LONG}},
        "playerActivity": "{{STRING}}"
    }
}
```


**有效负载参数**

| 参数                   | 描述                                       | 类型     |
| -------------------- | ---------------------------------------- | ------ |
| token                | 唯一代表Speak指令的token。                       | string |
| offsetInMilliseconds | 标识TTS的当前偏移量（以毫秒为单位）。Identifies the current offset of TTS in milliseconds. | long   |
| playerActivity       | 标识SpeechSynthesizer的状态。 接受的值：PLAYING或FINISHED。 | string |

| Player Activity | Description                  |
| --------------- | ---------------------------- |
| PLAYING         | Speech was playing.          |
| FINISHED        | Speech was finished playing. |

## 8.3 Speak 指令


只要需要TVS的语音回复，该指令就会从TVS发送给客户端。 在大多数情况下，Speak指令是为响应用户请求而发送的，例如Recognize事件。 但是，也可以向客户端发送Speak指令，以便为将要采取的操作做好准备。 例如，当用户发出设置定时器的请求时，除了接收指示客户端设置警报的SetAlert指令之外，客户端还接收Speak指令，该指令通知用户定时器已成功设置。
该指令作为多部分消息发送给您的客户端：一部分是JSON格式的指令和一部分二进制音频附件。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "SpeechSynthesizer",
            "name": "Speak",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "url": "{{STRING}}",
            "format": "{{STRING}}",
            "token": "{{STRING}}"
        }
    }
}
```

**Binary Audio Attachment**

每个Speak指令将具有相应的二进制音频附件作为multipart回包的一部分。 以下multipart标题将位于二进制音频附件之前：
```java
Content-Type: application/octet-stream
Content-ID: {{Audio Item CID}}

{{BINARY AUDIO ATTACHMENT}}
```


**Header参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| messageId       | 用于表示特定消息的唯一ID。                           | string |
| dialogRequestId | 用于将response中的指令与特定的Recognize事件关联起来的唯一ID。 | string |



**有效负载参数**

| 参数     | 描述                                       | 类型     |
| ------ | ---------------------------------------- | ------ |
| url    | 音频内容的唯一标识符。 URL始终遵循前缀cid：。例如：CID：{{STRING}}。 | string |
| format | 返回音频的格式。 可接受的值：“AUDIO_MPEG”。             | string |
| token  | 一个不透明的token，表示当前的文本到语音（TTS）对象。           | string |

## 8.4 SpeechStarted 事件

在客户端处理完Speak指令并开始播放语音时，应将SpeechStarted事件发送到TVS。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "SpeechSynthesizer",
            "name": "SpeechStarted",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数    | 描述                    | 类型     |
| ----- | --------------------- | ------ |
| token | 用于唯一标识Speak指令的token值. | string |

## 8.5 SpeechFinished 事件

必须在客户端处理Speak指令并且TVS TTS完全播放给用户后发送SpeechFinished事件。 如果播放未完成，例如用户使用“DingDangDingDang，stop”中断TVS TTS，则不发送SpeechFinished。

**代码示例**
```java
{
    "event": {
        "header": {
            "namespace": "SpeechSynthesizer",
            "name": "SpeechFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数    | 描述                    | 类型     |
| ----- | --------------------- | ------ |
| token | 用于唯一标识Speak指令的token值. | string |




# 9 System 接口

System接口提供跨多个客户端组件的事件。
## 9.1 SynchronizeState 事件

建立新连接时，必须发送SynchronizeState事件到TVS以更新所有终端状态。

**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.     
    ],      
    "event": {
        "header": {
            "namespace": "System",
            "name": "SynchronizeState",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Context**

本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。



**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

应发送空的有效负载。

## 9.2 UserInactivityReport 事件

此事件必须在一小时不活动后发送，并在此之后每小时发送一次，直到执行用户操作。 TVS以此检测上次用户活动以来的持续时间。 用户活动被定义为确认用户存在产品的动作，例如与产品上的按钮交互，与TVS交谈或使用GUI 检测到用户活动后，用于跟踪不活动的计时器必须重置为0。

**提示**：为inactiveTimeInSeconds提供的值应始终为3600（1小时）的倍数。 例如，在4小时不活动后，该值将为14400。

**代码示例**
```java
{
   "event": {
        "header": {
            "namespace": "System",
            "name": "UserInactivityReport",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "inactiveTimeInSeconds": {{LONG}}
        }

    }

}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                    | 描述            | 类型   |
| --------------------- | ------------- | ---- |
| inactiveTimeInSeconds | 自上次用户交互以来的秒数。 | long |

## 9.3 ResetUserInactivity 指令


ResetUserInactivity指令发送客户端可以重置UserInactivityReport使用的不活动计时器。 例如，腾讯DingDang应用程序上的用户交互将触发此指令。
**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "System",
            "name": "ResetUserInactivity",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

## 9.4 SetEndpoint 指令

SetEndpoint指令指示客户端在满足以下条件时更改接入点：
- 客户端连接到的接入点不支持用户的国家/地区设置。 例如，如果用户在管理您的内容和设备中把当前国家/地区设置为的英国（UK），但客户端连接到美国（US）接入点，TVS将发送SetEndpoint指令，指示客户端连接到支持英国的接入点。
- 用户更改其国家/地区设置（或地址）。 例如，如果连接到US接入点的用户将其当前国家/地区从美国更改为英国，TVS将发送SetEndpoint指令，指示客户端连接到支持UK的端点。
  **重要**：未能切换接入点可能导致用户无法访问自定义首选项以及国家或地区特定内容。
  **代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "System",
            "name": "SetEndpoint",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "endpoint": "{{STRING}}"
         }
    }
}
```


**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数       | 描述                                       | 类型     |
| -------- | ---------------------------------------- | ------ |
| endpoint | 支持用户的国家/地区设置的TVS接入点URL，URL可能包括协议和端口。例如： https://tvs.html5.qq.com | string |

## 9.5 SoftwareInfo 事件

此事件将您产品的软件信息传达给TVS，例如固件版本。 它必须在以下场景中发送：
- 对于具有持久存储的产品，必须在产品的初始引导和固件版本更新时发送事件。
- 对于没有持久存储的产品，必须在每次启动/重新启动时发送事件。
- 收到ReportSoftwareInfo指令时。
  如果事件处理成功，产品将收到204 HTTP状态码，返回体为空。 如果未处理该事件，则产品将收到500 HTTP状态码和异常消息。

**代码示例**
```java
{    
    "event": {
        "header": {
            "namespace": "System",
            "name": "SoftwareInfo",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "firmwareVersion": "{{STRING}}"
        }
    }
}
```

**Header Parameter**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数              | 描述                                       | 类型     |
| --------------- | ---------------------------------------- | ------ |
| firmwareVersion | 32位正整数的字符串形式。 如果向TVS发送了无效值，TVS会向您的客户端返回HTTP 400状态代码。 重要信息："0"不是有效的固件版本。 | string |

| 有效         | 无效                      |
| ---------- | ----------------------- |
| "123"      | "50.3"                  |
| "8701"     | "tvs-123.4x"            |
| "20170207" | "tsk.201-(1.23.4-test)" |

## 9.6 ReportSoftwareInfo 指令

该指令收到时，产品必须使用SoftwareInfo事件向TVS报告当前软件信息。

**代码示例**
```java
{
    "directive": {
        "header": {
            "namespace": "System",
            "name": "ReportSoftwareInfo",
            "messageId": "{{STRING}}"
        },
        "payload": {
        }
    }
}
```

**Header Parameter**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |

## 9.7 ExceptionEncountered 事件

当客户端无法执行TVS下发的指令时，必须发送ExceptionEncountered事件。
**代码示例**
```java
{
    "context": [
        // This is an array of context objects that are used to communicate the
        // state of all client components to TVS. See Context for details.      
    ],     
    "event": {
        "header": {
            "namespace": "System",
            "name": "ExceptionEncountered",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "unparsedDirective": "{{STRING}}",
            "error": {
                "type": "{{STRING}}"
                "message": "{{STRING}}"
            }
        }
    }
}
```

**Context**

本事件要求客户端将所有状态发送到TVS。 有关其他信息，请参阅Context。

**Header参数**

| 参数        | 描述             | 类型     |
| --------- | -------------- | ------ |
| messageId | 用于表示特定消息的唯一ID。 | string |



**有效负载参数**

| 参数                | 描述                            | 类型     |
| ----------------- | ----------------------------- | ------ |
| unparsedDirective | 当无法执行指令时，客户端必须将指令作为字符串返回给TVS。 | string |
| error             | 错误的键/值对。                      | object |
| error.type        | 错误类型。                         | string |
| error.message     | 方便记录与问题定位的附加错误信息。             | string |

## 9.8 Error 类型

| Error类型                         | 描述                          |
| ------------------------------- | --------------------------- |
| UNEXPECTED_INFORMATION_RECEIVED | 发送给客户端的指令格式不正确或有效负载不符合指令规范。 |
| INTERNAL_ERROR                  | 设备处理指令时发生错误，并且错误不属于指定的类别。   |
