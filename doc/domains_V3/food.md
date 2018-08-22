

### 领域名称
food


### 意图列表

| Intent    | Description |
| --------- | ----------- |
| qa_foodnutrition_weight       |    食物热量判断  |
|qa_foodnutrition_compare|食物营养成分比较|
|qa_foodnutrition_content|食物营养含量查询|
|qa_foodnutrition_judge|食物营养成分查询|
### 数据示例

##### 纯文本模版

```json
/*
 * 所有意图仅有回复语 无 Json 数据
 * 语料：苹果有蛋白质吗？
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 

    {
        "controlInfo": {
            "textSpeak": "true", 
            "type": "TEXT", 
            "version": "1.0.0"
            }, 
        "listItems": [
            {
                "textContent": "我查了一下，苹果中有蛋白质。"
            }
            ]
        }
    }