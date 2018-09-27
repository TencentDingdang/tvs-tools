[TOC]

### 领域名称

汇率服务

### 意图列表

| Intent             | Description                         |
| ------------------ | ----------------------------------- |
| exchangecalculate  | 美元汇率                            |
| exchangerate       | 港币汇率走势                        |

### 数据示例

##### exchangecalculate exchangerate 纯文本模版

```json
/*
 * exchangecalculate exchangerate 纯文本模版
 * 语料：美元汇率
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "汇率信息如下",
	"strSpeakTipsText": "当前1美元可兑换6.39人民币"
}
// ======================= Json 数据 =======================
{
	"baseInfo": {
		"skillName": ""
	},
	"controlInfo": {
		"textSpeak": "false",
		"type": "TEXT"
	},
	"listItems": [{
		"textContent": "",
		"title": "当前1美元=6.3864人民币(实时数据仅供参考，交易以柜台成交价为准)"
	}]
}
```
