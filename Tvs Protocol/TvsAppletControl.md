### 小程序控制指令
```json
{
    "directive": {
        "header": {
            "namespace": "AppletControl",
            "name": "Control",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "data": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                        |    Type        |    必选    |    描述                        |
|    :-------------------------------    |    :--------    |    :-----    |    :------------------------    |
|    data                                |    string    |    Yes    |    数据                        |