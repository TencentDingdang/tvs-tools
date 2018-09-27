[TOC]

### 领域类别

问答对

### 领域名称

| domain                  | Description  |
| ----------------------- | ------------ |
| world_record            | 世界之最      |
| htwhys                  | 十万个为什么   |
| disease                 | 疾病          |
| common_qa               | 公共问答对     |

### 意图名称
| intent                  | Description  |
| ----------------------- | ------------ |
| qa_pairs                | 问答对        |

### 数据示例

##### 图文模版

| domain                  | Description  |
| ----------------------- | ------------ |
| world_record            | 世界之最      |

```json
/*
 * 图文模版 (1)
 * 语料：世界上最高的山
 * BOT：企鹅智能 (f9c72cf09add11e88372f1de7552b6e4)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": ""
}
// ======================= Json 数据 =======================
{
	"controlInfo": {
    	"audioConsole": "true", 
        "textSpeak": "true", 
        "type": "GRAPHIC", 
        "version": "1.0.0"
    }, 
	"listItems": [
		{
            "htmlView": "http://www.baidu.com/link?url=8PVyrm8xJK4U4c4c7E1oerUZ4kVoK1m8FJA-8_FpWj1UkWyVtNNXi408sSLhIxt5pqF-Xw5N5gCQY1Ue2lsuuK", 
            "image": {
                "contentDescription": "", 
                    "sources": [
                        {
                            "url": "https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3847791850,404995985&fm=58"
                        }
                ]
            }, 
            "textContent": "世界上最高的山是珠穆朗玛峰。位于中国与尼泊尔边界上，海拔8844.43米。", 
            "title": ""
                }
        ]
}
```

##### 图文模版 (2)

| domain                  | Description  |
| ----------------------- | ------------ |
| htwhys                  | 十万个为什么   |

```json
/*
 * 图文模版
 * 语料：天空为什么是蓝色的
 * BOT：企鹅智能 (f9c72cf09add11e88372f1de7552b6e4)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "",
	"strSpeakTipsText": ""
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
    	"audioConsole": "true", 
        "textSpeak": "true", 
        "type": "GRAPHIC", 
        "version": "1.0.0"
    },
    "listItems": [
    	{
            "htmlView": "", 
            "image": {
                "contentDescription": "", 
                 "sources": [
                        {
                            "url": ""
                        }
                    ]
             }, 
            "textContent": "因为大气分子对太阳光里的蓝色光散射最小，蓝色光长驱直入，所以蓝天是蓝色的。", 
            "title": ""
                }
        ]
}
```
### 备注

所有问答对领域返回的数据格式都是一样的，其他问答对领域的返回格式可以参考上面两个示例
