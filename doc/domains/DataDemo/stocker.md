[TOC]

### 领域名称

股票服务

### 意图列表

| Intent                         | Description                    |
| :----------------------------- | ------------------------------ |
| price                          | 查股价                         |
| marketindex                    | 大盘指数                         |




### 数据示例

```json
/*
 * 语料：腾讯股价
*/ 
// ======================= Json 数据 =======================
 {
            "controlInfo": {
                "audioConsole": "", 
                "textSpeak": "true", 
                "type": "TEXT", 
                "version": ""
            }, 
            "globalInfo": {
                "selfData": {
                    "sGuid": ""
                }
            }, 
            "listItems": [
                {
                    "selfData": {
                        "stockdataObj": {
                            "dividendYield": "0.24", 
                            "dstUrl": "http://finance.qq.com/wxzixuangu/index.htm#/stock/hk00700", 
                            "eps": "", 
                            "genTime": "2018/07/27 16:08:26", 
                            "highestPrice": "374.00", 
                            "lowestPrice": "369.80", 
                            "market": "港股", 
                            "marketStat": "已休市", 
                            "marketValue": "3.55万亿", 
                            "peRatio": "0", 
                            "priceChange": "-1.80", 
                            "priceChangeRatio": "-0.48%", 
                            "quantiryRatio": "", 
                            "recentPrice": "373.00", 
                            "status": "", 
                            "stockCode": "00700", 
                            "stockName": "腾讯控股", 
                            "tOpenPrice": "371.00", 
                            "tradeVol": "1446.29万股", 
                            "turnOver": "53.81亿", 
                            "turnRatio": "", 
                            "unit": "港元", 
                            "yClosePrice": "374.80"
                        }
                    }, 
                    "textContent": "腾讯控股最新交易日的收盘价是373.00，下跌了1.80，降幅0.48%", 
                    "title": ""
                }
            ]
        }
  

```

