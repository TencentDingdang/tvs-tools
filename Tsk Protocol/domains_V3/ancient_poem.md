[TOC]

### 领域名称

古诗

### 意图列表

| Intent                      | Description  |
| --------------------------- | ------------ |
| search_tangshi              | 查询古诗全文       |
| search_tangshi_author       | 查询诗词作者       |
| search_ancientpoemtitle     | 查询诗词的标题      |
| search_ancientpoem_meaning      | 查询诗词全文的含义    |
| search_ancientpoem_dynasty      | 查询诗歌写作朝代     |
| search_ancientpoem_by_tag       | 按标签 查询诗词     |
| search_ancientpoem_appreciation | 查询古诗鉴赏文      |
| search_ancientpoem_chains        | 查询诗句下一句      |
| search_ancientpoem_by_word      | 按诗词中的关键字查询诗词 |
| search_ancientpoem_previous     | 查询诗句的上一句     |

### 数据示例

##### 纯文本模版

| Intent                  | Description |
| ----------------------- | ----------- |
| search_ancientpoem_previous | 查询诗句的上一句    |
| search_ancientpoem_chains    | 查询诗句下一句     |
| search_ancientpoem_dynasty  | 查询诗歌写作朝代    |
| search_tangshipoemtitle | 查询诗词的标题     |
| search_tangshi_author   | 查询诗词作者      |

```json
/*
 * 无模版
 * 语料：离离原上草的下一句
 * BOT：410音箱 (2b82efec-a77c-46cd-a2c2-8df9bbd1d1c3)
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
        "orientation": "portrait", 
        "textSpeak": "true", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "audio": {
                "metadata": {
                    "offsetInMilliseconds": 0, 
                    "totalMilliseconds": 0
                }, 
                "stream": {
                    "url": ""
                }
            }, 
            "htmlView": "https://sdk.sparta.html5.qq.com/dingdang/poem.html?pid=gsww|21818", 
            "mediaId": "gsww|21818", 
            "selfData": {
                "author": "", 
                "dynasty": ""
            }, 
            "textContent": "一岁一枯荣", 
            "title": ""
        }
    ]
}
```

##### 纯文本模版、音频模版

| Intent                      | Description  |
| --------------------------- | ------------ |
| search_tangshi              | 查询古诗全文       |
| search_ancientpoem_meaning      | 查询诗词全文的含义    |
| search_ancientpoem_by_tag       | 按标签 查询诗词     |
| search_ancientpoem_appreciation | 查询古诗鉴赏文      |
| search_ancientpoem_by_word      | 按诗词中的关键字查询诗词 |

```json
/*
 * 纯文本模版、音频模版
 * 语料：静夜思
 * BOT：410音箱 (2b82efec-a77c-46cd-a2c2-8df9bbd1d1c3)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "这是《静夜思》的全文",
	"strSpeakTipsText": "这是《静夜思》的全文"
}
// ======================= Json 数据 =======================
{
    "controlInfo": {
        "audioConsole": "true", 
        "orientation": "portrait", 
        "textSpeak": "false", 
        "type": "AUDIO", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "audio": {
                "metadata": {
                    "offsetInMilliseconds": 0, 
                    "totalMilliseconds": 0
                }, 
                "stream": {
                    "url": "http://softfile.3g.qq.com/myapp/trom_l/dobby/ancient_poem/poem_formal/voice/D/2018/7/20180726/D_P_jingyesi_20180726.mp3"
                }
            }, 
            "htmlView": "https://sdk.sparta.html5.qq.com/dingdang/poem.html?pid=gsww|7816", 
            "mediaId": "gsww|7816", 
            "selfData": {
                "author": "李白", 
                "dynasty": "唐代"
            }, 
            "textContent": "床前明月光，疑是地上霜。
举头望明月，低头思故乡。", 
            "title": "静夜思"
        }
    ]
}

```