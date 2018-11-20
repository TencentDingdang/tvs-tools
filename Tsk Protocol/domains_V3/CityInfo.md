[TOC]

### 领域名称

号码查询服务

### 意图列表

| Intent                         | Description                    | 语料示例                    |
| :----------------------------- | ------------------------------ | --------------------------- |
| zipcode                        | 查邮编                         |山东潍坊市邮编               |
| areacode                       | 查区号                         |	安徽阜阳区号多少            |
| phoneLocation                  | 换归属地                       |13022421599是哪的电话        |




### 数据示例 
 
 ```json
{
    "jsonData": {
        "controlInfo": {
            "audioConsole": "",
            "textSpeak": "true",
            "type": "TEXT",
            "version": ""
        },
        "listItems": [
            {
                "selfData": {
                    "gasPrice": {
                        "fPrice1": 0,
                        "fPrice2": 0,
                        "fPrice3": 0,
                        "fPrice4": 0,
                        "sDistrict": "",
                        "vecGasPriceDesc": []
                    },
                    "phoneAreaCodeVec": {
                        "vCode": [
                            {
                                "sCity": "济南",
                                "sCode": "0531",
                                "sCounty": "",
                                "sProvince": "山东省"
                            }
                        ]
                    },
                    "phoneLocation": {
                        "sCarreier": "",
                        "sCity": "",
                        "sNumber": "",
                        "sProvice": ""
                    },
                    "zipCodes": {
                        "iCmdType": 0,
                        "vZip": []
                    }
                }
            }
        ]
    }
}
```