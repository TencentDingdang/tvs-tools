[TOC]

### 领域名称

存贷款和金价服务

### 意图列表

| Intent             | Description |
| ------------------ | ----------- |
| search_price       | 黄金价格    |
| search_loanrate    | 贷款利率    |
| search_depositrate | 存款利率    |

### 数据示例

##### search_price 无模版

```json
/*
 * search_price 纯文本模版
 * 语料：黄金价格
 * BOT：410音响 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "textContent": "最新国际黄金价格是1227.8美元每盎司，上海黄金交易所价格是268.57人民币每克"
        }
    ]
}
```

##### search_loanrate 纯文本模版

```json
/*
 * search_loanrate 纯文本模版
 * 语料：贷款利率
 * BOT：410音响 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"textSpeak": "false",
		"type": "TEXT"
	},
	"listItems": [{
		"textContent": "商业贷款利率:
6个月内:          4.35%，
6个月至一年:      4.75%，
一年至三年:       4.90%，
三年至五年:       4.90%，
五年以上:         4.90%。
公积金贷款利率:
五年以内:         2.75%。
五年以上:         3.25%。"
	}]
}
```

##### search_depositrate纯文本模版

```json
/*
 * search_loanrate 纯文本模版
 * 语料：存款利率
 * BOT：410音响 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"textSpeak": "false",
		"type": "TEXT"
	},
	"listItems": [{
		"textContent": "整存整取年利率:
活期:         0.30%，
3个月:        1.35%，
6个月:        1.55%，
一年:         1.75%，
二年:         2.25%，
三年:         2.75%，
五年:         2.75%。
零存整取、整存零取年利率:
一年:         1.35%，
三年:         1.55%，
五年:         1.55%。
其他存款方式年利率:
协定存款:     1%，
一天通知存款: 0.55%，
七天通知存款: 1.1%。"
	}]
}
```

