[TOC]

### 领域名称
1. cityinfo
2. phone_call

### 意图列表

| Domain    | Intent            | Description                         |
| ----------| ----------------- | ----------------------------------- |
| cityinfo  | yellowpages       | 号码查询                             |
| phone_call| lookup_phone_num  | 号码查询                             |
| phone_call| make_a_phone_call | 打电话                               |

### 数据示例
##### 纯文本模版

```json
/*
 * 纯文本模版
 * @domain: phone_call
 * @intent: lookup_phone_num
 * 语料：中国联通的号码是多少
 * BOT：咕咚x1more iBFree2智能耳机 (7ae9ba0b-3de8-4552-917c-b205b4749338)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "中国联通客服电话是10010",
	"strSpeakTipsText": "中国联通客服电话是10010"
}
// ======================= Json 数据 =======================
{
    "baseInfo": {
        "skillIcon": "", 
        "skillName": "YellowPages"
    }, 
    "controlInfo": {
        "audioConsole": "false", 
        "textSpeak": "false", 
        "type": "TEXT", 
        "version": "1.0.0"
    }, 
    "listItems": [
        {
            "selfData": {
                "department": "客户服务", 
                "phone": "10010", 
                "title": "中国联通客服电话"
            }, 
            "textContent": "客户服务", 
            "title": "中国联通客服电话"
        }, 
        {
            "selfData": {
                "department": "充值服务", 
                "phone": "10011", 
                "title": "中国联通客服电话"
            }, 
            "textContent": "充值服务", 
            "title": "中国联通客服电话"
        }
    ]
}
```