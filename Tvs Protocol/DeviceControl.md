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
                "parameters": [
                    {
                        "name": "{{STRING}}",
                        "valueList": [
                            "{{STRING}}", "{{STRING}}", "{{STRING}}"
                        ]
                    },
                    {
                        "name": "{{STRING}}",
                        "valueList": [
                            "{{STRING}}", "{{STRING}}", "{{STRING}}"
                        ]
                    }
                ]
            }
		}
	}
}
```

***Header Paramters***

|	Parameter			|	Type		|	必选	|	描述								|
|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	messageId			|	string	|	Yes	|	消息ID							|
|	dialogRequestId	|	string	|	Yes	|	对话ID							|

***Payload Paramters***

|	Parameter								|	Type		|	必选	|	描述								|
|	:---------------------------------------	|	:--------	|	:-----	|	:--------------------------------	|
|	nlpInfo									|	object	|	Yes	|	NLP信息						|
|	nlpInfo.domain						|	string	|	Yes	|	NLP领域信息					|
|	nlpInfo.intent							|	string	|	Yes	|	NLP意图信息					|
|	nlpInfo.parameters					|	array		|	Yes	|	NLP参数信息					|
|	nlpInfo.parameters[].name		|	string	|	Yes	|	NLP参数名称					|
|	nlpInfo.parameters[].valueList	|	array		|	Yes	|	NLP参数值					|