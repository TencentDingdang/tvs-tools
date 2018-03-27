# 彩票
### lottery.*
#### 问法
查下今天大乐透的开奖信息
#### JSON
```json
{
   
   "dataVec": [
        {
            "codeVec": [   //开奖的号码
                    "07", 
                    "11", 
                    "18", 
                    "26", 
                    "28", 
                    "04", 
                    "05"
            ], 
            "colorCodeCnt": 2, //彩色球格式
            "strDate": "10-25 12:30:00", //开奖时间
            "strName": "大乐透",         //彩票类型
            "strPeriod": "17125",        //该类彩票的开奖期数
            "strUrl": "https://qs.888.qq.com/m_qq/mqq2.local.html?vb2ctag=4_2013_3_1780_1#lot.info=getIssue&lotteryId=dlt" //更多链接
         }
    ], 
            "retCode": 0,     //返回状态
            "strJumpUrl": "", //跳转链接
            "strTips": ""     //提示
        
}
```