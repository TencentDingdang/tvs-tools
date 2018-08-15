### 领域名称
astro


### 意图列表

| Intent    | Description |
| --------- | ----------- |
| search_astro  |    搜索星座  |
|search_fastfate|星座速配|
|search_info|搜索星座的基本资料|
|search_scope|搜索星座的运势|
|search_astrodate|搜索星座日期|
### 数据示例

##### 纯文本模版

```json
/*
 *
 * 语料：天秤座运势？
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 


"controlInfo": {
	"textSpeak": "true",
	"type": "TEXT"
},
"listItems": [{
	"selfData": {
		"iSubCmd": 2,//子命令字
		"sJsonData": "{ 
			"iFortuneLevel": 3, 
			"sAstroName": "天秤座", //星座名称
			"sFortuneDesc": "今天对工作非常在意，做什么都认真，能够充分表现出个人能力，偶尔会有思想摇摆的时候，不过很快能回过神来。但要做每件事都不能马虎，都要多检查细节，还有时刻不忘给自己点赞，给自己多点自信心。", 
			"sFortuneType": "今日运势", 
			"sLogo": "http://cache.xzw.com/mapi/static/img/xz/1.jpg", 
			"sMoreUrl": "https://m.xzw.com/fortune/libra/?/_app=dingdang", 
			"sValidDate": "" }",//私有数据
		"sMoreUrl": "https://m.xzw.com/fortune/libra/?_app=dingdang",//跳转的URL
		"vcData": [],//二进制数据
		"vcDataV2": []//新版的实际数据Translate
	},
	"textContent": "天秤座今日运势不错。今天对工作非常在意，做什么都认真，能够充分表现出个人能力，偶尔会有思想摇摆的时候，不过很快能回过神来。",
	"title": "天秤座今日运势不错。今天对工作非常在意，做什么都认真，能够充分表现出个人能力，偶尔会有思想摇摆的时候，不过很快能回过神来。"
}]
}
```



