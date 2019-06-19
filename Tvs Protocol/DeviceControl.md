### 优必选设备控制指令
```json
{
    "directive": {
        "header": {
            "namespace": "DeviceControl",
            "name": "Control",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "nlpInfo" {
                "domain": "{{STRING}}",
                "intent": "{{STRING}}",
                "parameters": [
                    {
                        "name": "{{STRING}}",
                        "valueList": [
                            "{{STRING}}", "{{STRING}}", "{{STRING}}"
                        ],
                        "objectValueList": [
                            "{{STRING}}", "{{STRING}}", "{{STRING}}"
                        ]
						
                    },
                    {
                        "name": "{{STRING}}",
                        "valueList": [
                            "{{STRING}}", "{{STRING}}", "{{STRING}}"
                        ],
                        "objectValueList": [
                            "{{STRING}}", "{{STRING}}", "{{STRING}}"
                        ]
                    }
                ],
                "originalParameters": [
                    {
                        ...
                    },
                    {
                        ...
                    }
                ]
            },
            "data": {
                "jsonData": "{{STRING}}"
            }
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId    |    string    |    No    |    对话ID                            |

***Payload Paramters***

|    Parameter                                |    Type        |    必选    |    描述                                |
|    :---------------------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    nlpInfo                                    |    object    |    Yes    |    NLP信息                        |
|    nlpInfo.domain                        |    string    |    Yes    |    NLP领域信息                    |
|    nlpInfo.intent                            |    string    |    Yes    |    NLP意图信息                    |
|    nlpInfo.parameters                    |    array        |    Yes    |    NLP参数信息                    |
|    nlpInfo.parameters[].name        |    string    |    Yes    |    NLP参数名称                    |
|    nlpInfo.parameters[].valueList    |    array        |    Yes    |    NLP参数值                    |
|    nlpInfo.parameters[].objectValueList    |    array        |    Yes    |    NLP对象参数值                    |
|    nlpInfo.originalparameters        |    array        |    Yes    |    NLP原始参数信息            |
|    data                                        |    object    |    No    |    数据                                |
|    data.jsonData                        |    string    |    No    |    服务数据信息                    |

### 设备控制指令
```json
{
    "directive": {
        "header": {
            "namespace": "DeviceControl",
            "name": "Control",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "nlpInfo" {
                "domain": "{{STRING}}",
                "intent": "{{STRING}}",
            },
            "data": {
                "controlData": "{{STRING}}"
            }
        }
    }
}
```

***Header Paramters***

|    Parameter        		|    Type    	|    必选	|    描述                            	|
|    :------------------- 		|    :-------- 	|    :----- 	|    :-------------------------------- 	|
|    messageId       	 	|    string  	|    Yes 	|    消息ID                        	|
|    dialogRequestId    |    string  	|    No 	|    对话ID                       	|

***Payload Paramters***

|    Parameter                        		|    Type 	|    必选	|    描述                          	|
|    :---------------------------------------	|    :-------- 	|    :-----	|    :-------------------------------- 	|
|    nlpInfo                              	|    object	|    Yes 	|    NLP信息                     	|
|    nlpInfo.domain                	 	|    string  	|    Yes 	|    NLP领域信息               	|
|    nlpInfo.intent                       	|    string  	|    Yes 	|    NLP意图信息               	|
|    data                                    	|    object 	|    Yes  |    数据                           	|
|    data.controlData                 	|    string  	|    Yes  |    服务数据                   	|