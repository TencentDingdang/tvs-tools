# 计算器
### science.calculator
#### 问法
一加一等于多少
#### JSON
```json
{
    "domain": "science", 
    "intent": "calculator", 
    
    //*******************终端只关心strSpeakText就可以
    "strSpeakText": "1+1=2", 
    "strTipsText": "(deprecated 弃用字段)", 
    "Description": "0 未知类型; 1 文本类型; 6 图文类型; 11 媒体文本", 
    "VectResponseData": [
        {
            "eDataType": 1, 
            "strTitle": "1+1=2", 
            "strDescription": "", 
            "strContentURL": "", 
            "strDestURL": "", 
            "strDownloadURL": "", 
            "strContentData": "", 
            "strContentID": "", 
            "strShareURL": "", 
            "_classname": "SmartService.AIResponseDataItem"
        }
    ], 
    "CommRspData": {
        "AIDataType": 0, 
        "commRspVec": [ ], 
        "strAllUrl": "", 
        "mapDataSource": { }
    }, 
    "jsonData": {
        "jsonData": {
            "iRet": 0, 
            "sFormula": "2", 
            "sResult": "2"
        }
    }
}
```