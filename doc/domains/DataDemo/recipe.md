[TOC]

### 领域名称

菜谱

### 意图列表

| Intent                 | Description                  |
| ---------------------- | ---------------------------- |
| search_by_recipename   | 根据菜谱名查询                      |
| search_by_foodmaterial | 据食材名查询                       |
| search_by_recipescene  | 根据美食场景查询                     |
| search_foodmaterial    | 同 search_by_foodmaterial，无意义 |

### 数据示例

##### 全意图 图文模版

```json
/*
 * 全意图 图文模版
 * 语料：红烧头怎么做
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "为您找到红烧肉的做法",
	"strSpeakTipsText": "为您找到红烧肉的做法"
}
// ======================= Json 数据 =======================
{
	"controlInfo": {
		"audioConsole": "", 
		"textSpeak": "false", 
		"type": "GRAPHIC"
	}, 
	"globalInfo": {
		"seeMore": ""
	}, 
	"listItems": [
		{
			"htmlView": "http://m.douguo.com/cookbook/219102.html?f=73586533", 
			"image": {
				"contentDescription": "", 
				"sources": [
					{
						"heightPixels": 0, 
						"size": "", 
						"url": "http://i1.douguo.net//upload/caiku/7/c/8/yuan_7c40817f8687b25a09206158a5ec5648.jpg", 
                                "widthPixels": 0
					}
				]
			}, 
			"mediaId": "219102", 
			"selfData": {
				"collectCnt": 264974, 
				"cookStepVec": [
					{
						"stepContent": "做法：将五花肉切块用黄酒腌一会（如果着急吃就腌15分钟）", 
						"stepLargeImageUrl": "http://cp1.douguo.net/upload/caiku/1/9/e/600_19fd6b95469ad2dd0e60272abffd504e.jpg", 
						"stepNo": 1, 
						"stepSmallImageUrl": "http://cp1.douguo.net/upload/caiku/1/9/e/140_19fd6b95469ad2dd0e60272abffd504e.jpg"
					}, 
					{
						"stepContent": "水开后将五花肉焯水，肉变色即可", 
						"stepLargeImageUrl": "http://cp1.douguo.net/upload/caiku/6/b/6/600_6bbb392655a270358ac39b14b423aea6.jpg", 
						"stepNo": 2, 
						"stepSmallImageUrl": "http://cp1.douguo.net/upload/caiku/6/b/6/140_6bbb392655a270358ac39b14b423aea6.jpg"
					}
				], 
				"learnCnt": 6748, 
				"likeCnt": 0, 
				"majorVec": [
					{
						"strName": "五花肉", 
						"strNote": "500g"
					}
				], 
				"minorVec": [
					{
						"strName": "姜片", 
						"strNote": "5"
					}, 
					{
						"strName": "葱段", 
						"strNote": "少许"
					}
				], 
				"strCookDifficulty": "切墩(初级)", 
				"strCookTime": "30-45分钟", 
				"strTips": "1、我没有特别炒糖色 怕肉柴 怕炒糊了 所以就简单地上了个色\
2、炖肉没必要放太多的香料 八角 桂皮即可 放小茴香有点多余 大家可以自己试试\
3、酱油如果放的多就没必要放盐了\
4、我放蚝油是为了提鲜", 
				"strVideoUrl": "", 
				"viewCnt": 4372499
			}, 
			"textContent": "", 
			"title": "红烧肉"
		}
	]
}
```

