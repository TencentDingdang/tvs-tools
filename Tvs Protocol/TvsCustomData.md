### 状态上下文
```json
{
	"header": {
		"namespace": "TvsCustomData",
		"name": "State"
	},
	"payload": {
		"currentState": [
				{
					"type": "{{STRING}}",
					"value": "{{STRING}}"
				},
				{
					"type": "{{STRING}}",
					"value": "{{STRING}}"
				}
		]
	}
}
```

***Payload Paramters***

|	Parameter					|	Type		|	必选	|	描述										|
|	:---------------------------	|	:--------	|	:-----	|	:---------------------------------------	|
|	currentState				|	array		|	Yes	|	状态(不超过1000个字符)			|
|	currentState[].type		|	string	|	Yes	|	业务类型								|
|	currentState[].value	|	string	|	Yes	|	业务数据								|

### 数据指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsCustomData",
            "name": "Data",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "data": [
				{
					"type": "emotion",
					"value": "{{STRING}}"
				},
				{
					"type": "emotion",
					"value": "{{STRING}}"
				}
			]
        }
    }
}
```

***Header Paramters***

|    Parameter          	|    Type    	|    必选	|    描述                         	|
|    :-------------------    	|    :-------- 	|    :-----	|    :-------------------------------- 	|
|    messageId          	|    string   	|    Yes 	|    消息ID                        	|
|    dialogRequestId  	|    string  	|    No  	|    对话ID                        	|


***Payload Paramters***

|    Parameter                    	|    Type    	|    必选	|    描述                                                	|
|    :-------------------------------  	|    :-------- 	|    :----- 	|    :-----------------------------------------------------	|
|    data                            	|    array  	|    Yes	|    数据                        							|
|    data[].type                	|    string  	|    Yes 	|    业务类型:<br>emoton:情感数据,<br>action:动作数据|
|    data[].value                	|    string  	|    Yes 	|    业务数据                          					|