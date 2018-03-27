# 号码查询
### cityinfo.zipcode
邮编查询
#### 问法
深圳的邮编是多少
#### JSON
```json
{
    "iCmdType": 1, 
    "vZip": [
        {
            "bInCity": true, 
            "sCity": "深圳市", 
            "sCode": "518000", 
            "sCounty": "", 
            "sProvince": "广东省", 
            "sRoad": ""
        }
    ]
}
```

### cityinfo.phonelocation
手机号归属地查询
#### 问法
13800138000是哪里的手机号
#### JSON
```json
{
    "sCarreier": "移动", 
    "sCity": "北京", 
    "sNumber": "13800138000", 
    "sProvice": "北京"
}
```

#### cityinfo.areacode
区号查询
#### 问法
深圳的区号是多少
#### JSON
```json
{
    "vCode": [
        {
            "sCity": "深圳", 
            "sCode": "0755", 
            "sCounty": "", 
            "sProvince": "广东省"
        }
    ]
}
```
