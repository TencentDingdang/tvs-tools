# 情绪系统接入指南



[TOC]
# 一. 接入前置条件


## 1.1 要求

- 在云小微开放平台开通了情绪系统的能力，并按照文档进行配置，可以见[文档]()说明
- 接入基础API [语义请求接口](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/%E8%85%BE%E8%AE%AF%E5%8F%AE%E5%BD%93HTTP%E6%96%B9%E5%BC%8F%E6%8E%A5%E5%85%A5API%E6%96%87%E6%A1%A3.md#51-%E8%AF%AD%E4%B9%89%E8%AF%B7%E6%B1%82%E6%8E%A5%E5%8F%A3)，情绪系统数据从本接口返回。

# 二. 功能介绍

​	 用户进行交互时，云小微会在响应的json字段里面生成情绪动作数据，设备可以根据下发的情绪动作数据做自定义的逻辑，比如机器人挥手、音箱UI界面切换和音箱虚拟人动作交互等等。云小微平台仅下发情绪动作数据，设备在使用时自定义用法。



# 三. 功能流程

示例：
- 用户发起交互说：我很喜欢你
- 云小微下发数据时，携带情绪系统“喜欢”的表情数据和“欢迎”的动作数据
- 设备根据表情数据在屏幕上显示一个“喜欢”动画表情，根据“欢迎”的动作数据做出欢迎的动作。

# 四. 接入方法



## 4.1 接入数据协议

情绪系统的数据在基础API 语义请求的响应数据`payload.data.json`字段中。其结构为

```
{
	"innerInfo": {
		"directiveInfo": {
			"action": {
				"description": "示爱",
				"tag": "show_love"
			},
			"emotion": {
				"description": "喜爱",
				"tag": "like"
			},
			"ruleInfo": {
				"weight": 0
			},
			"tts": {
				"description": "中性",
				"style": 0
			}
		}

	}
}
```

 

**字段含义及类型说明：**

| 字段名称            | 字段含义         | 字段类型 |
| ------------------- | ---------------- | -------- |
| emotion             | 情绪数据         | object   |
| emotion.tag         | 情绪标签         | string   |
| emotion.description | 情绪描述         | string   |
| action              | 动作数据         | object   |
| action.tag          | 动作标签         | string   |
| action.description  | 动作描述         | string   |
| ruleInfo            | 情绪命中规则信息，终端无需关心 | object   |
| ruleInfo.weight     | 命中的规则权重   | int      |
| tts                 | 语言合成信息，仅用于调用云小微语音合成接口     | object   |
| tts.description     | 语音音色描述     | string   |
| tts.style           | 语音音色类型     | int      |


备注：**使用时请以emotion.tag和action.tag标签字段为准**，其他字段作为描述和补充信息，不保证取值有效性，不建议使用来做逻辑。



**字段取值说明：**

emotion.tag和emotion.description的取值成对出现，具体如下：

| emotion.tag | emotion.description |
| ----------- | ------------------- |
| like        | 喜爱                |
| surprise    | 惊喜                |
| neutral     | 中性                |
| sad         | 哀                  |
| fear        | 惧                  |
| angry       | 怒                  |



action.tag和action.description取值成对出现，具体如下：

| action.tag         | action.description |
| ------------------ | ------------------ |
| welcome            | 欢迎               |
| show_love          | 示爱               |
| shy_state          | 害羞态             |
| hands_on_hips      | 不满               |
| sad_face           | 沮丧态             |
| compliment_state   | 称赞               |
| longing            | 期待               |
| doubt_chin         | 质疑态             |
| speaking_circle    | 循环播报           |
| speaking_explain   | 讲解播报           |
| speaking_introduce | 介绍播报           |
| speaking_point     | 指点播报           |



rule.weight是情绪规则命中的权重，取值>=0。



tts.description和tts.style字段成对出现，取值如下：
| tts.style | tts.description |
| --------- | --------------- |
| 0         | 其他            |
| 1         | 悲伤            |
| 2         | 快乐            |
| 3         | 害怕            |
| 4         | 厌恶            |
| 5         | 喜欢            |
| 6         | 生气            |

## 4.2 根据数据做具体行为

### 4.2.1 表情与动作数据

设备自行根据emotion.tag和action.tag做自定义逻辑。

### 4.2.2 语音音色类型

tts.tag仅能用于调用云小微语音合成接口，如果接入方不打算计入云小微语音合成能力，可以忽略这块数据。







# 五. 验证用例

- 

# 六. 常见问题

- 
