[TOC]

### 领域名称

笑话

### 意图列表

| Intent | Description                         |
| ------ | ----------------------------------- |
| tell   | 讲笑话                                 |
| next   | 下一个， 返回跟最近一次请求一样类型的笑话 文字/音频/长音频/短音频 |

### 数据示例

##### tell next 音频类模版

```json
/*
 * tell next 音频类模版
 * 语料：讲个笑话
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "好的",
	"strSpeakTipsText": "好的"
}
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"textSpeak": "true", 
		"type": "AUDIO"
	}, 
	"listItems": [
		{
			"audio": {
				"stream": {
					"url": "http://softfile.3g.qq.com/myapp/trom_l/dobby/joke/201804/20180417/D_J_2018041719.mp3"
				}
			}, 
			"image": {
				"contentDescription": "", 
				"sources": [ ]
			}, 
			"mediaId": "b70ad96e19c852cfaaeb59e046e74ac3", 
			"textContent": ""
		}
	]
}
```

##### tell next 纯文本模版

```json
/*
 * tell next 纯文本模版
 * 语料：讲个笑话
 * BOT：腾讯叮当App (ad415e3e-643c-489a-88ca-3fda41f976c1)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "好的",
	"strSpeakTipsText": "好的"
}
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"textSpeak": "true", 
		"type": "TEXT"
	}, 
	"listItems": [
		{
			"audio": {
				"stream": {
					"url": ""
				}
			}, 
			"image": {
				"contentDescription": "", 
				"sources": [ ]
			}, 
			"mediaId": "68b4705f05a2300a8eb7fd86640668ea", 
			"textContent": "记得小学的时候，好不容易考了个第一名，我爸说带我去海洋馆玩，在过了若干年后，我才知道那是个海鲜市场～海鲜市场～海鲜市场～"
		}
	]
}
```

##### tell next 图文模版

```json
/*
 * tell next 图文模版
 * 语料：讲个笑话
 * BOT：腾讯叮当App (ad415e3e-643c-489a-88ca-3fda41f976c1)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "好的",
	"strSpeakTipsText": "好的"
}
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"textSpeak": "true", 
		"type": "GRAPHIC"
	}, 
	"listItems": [
		{
			"audio": {
            	"stream": {
					"url": ""
				}
			}, 
			"image": {
				"contentDescription": "怎么下去", 
				"sources": [
					{
						"url": "http://i4.xiaohua.fd.zol-img.com.cn/t_s300x2000/g2/M00/0E/03/Cg-4WVWuAoOIY-IQAAwlYCsDb-YAAHchAEtY2wADCV4714.gif"
					}
				]
			}, 
			"mediaId": "bfa8bb230e053ef095db7fc523b46af2", 
			"textContent": ""
		}
	]
}
```

