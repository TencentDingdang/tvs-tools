### 应用控制指令
```json
{
    "directive": {
        "header": {
            "namespace": "ApplicationControl",
            "name": "Control",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
			"id": "{{STRING}}",
			"data": {
				"type": "{{STRING}}",
				"uri": "{{STRING}}"
			}
		}
    }
}
```

***Header Paramters***

|    Parameter            	|    Type    	|    必选	|    描述                         	|
|    :-----------------------   	|    :-------- 	|    :-----	|    :-------------------------------- 	|
|    messageId     		|    string  	|    Yes 	|    消息ID                        	|
|    dialogRequestId    	|    string  	|    No 	|    对话ID                         	|

***Payload Paramters***

|    Parameter                    			|    Type    	|    必选	|    描述                           	|
|    :--------------------------------------- 	|    :--------	|    :-----	|    :-------------------------------- 	|
|    id                                    		|    string 	|    Yes 	|    ID                     			|
|    data                                   	|    object 	|    No   	|    数据                           	|
|    data.type                     			|    string  	|    No 	|    服务数据类型             	|
|    data.uri                     			|    string  	|    No 	|    服务数据信息             	|