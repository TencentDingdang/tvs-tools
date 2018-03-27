# 股票
### stock.*
#### 问法
腾讯今天的开盘价是多少
#### JSON
```json
{
    "answer": "腾讯控股最新交易日收盘价为318.80港元，下跌5.20港元，降幅1.60%", //回复语
    "funddataObjs": [ ], //基金数据 目前无数据
    "sGuid": "", //sGuid 
    "stockdataObjs": [//股票数据
        {
            "dividendYield": "0.19", 
            "eps": "", //每股收益，美股特有
            "genTime": "2017/08/15 16:09:39", //生成时间
            "highestPrice": "330.40", //最高价
            "lowestPrice": "318.80", //最低价
            "market": "港股", //市场类型
            "marketStat": "已收盘", //市场状态
            "marketValue": "3.03万亿港元", 
            "peRatio": "65.45", //市盈率
            "priceChange": "-5.20港元", //价格涨跌    
            "priceChangeRatio": "-1.60%", //涨跌幅
            "quantiryRatio": "", //量比，A股特有s
            "recentPrice": "318.80港元", //最新价格
            "status": "", //股票状态 没有值是正常的
            "stockCode": "00700", //股票代码
            "stockName": "腾讯控股", //股票名称
            "tOpenPrice": "328.00港元", //今开盘价
            "tradeVol": "2392.61万股", //成交量
            "turnOver": "77.73亿港元", //成交额
            "turnRatio": "", //换手率
            "yClosePrice": "324.00港元" //昨收盘价
        }
    ]
}
```