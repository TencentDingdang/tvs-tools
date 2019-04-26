### 下载指令
```json
{
    "directive": {
        "header": {
            "namespace": "TvsMediaControl",
            "name": "Download",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "url": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            	|    Type    	|    必选 	|    描述              				|
|    :----------------------    	|    :-------- 	|    :-------  	|    :-------------------------------- 	|
|    messageId 			|    string  	|    Yes    	|    消息ID                        	|
|    dialogRequestId    	|    string	|    No    	|    对话ID                         	|

***Payload Paramters***

|    Parameter            		|    Type    	|    必选  	|    描述             	|
|    :---------------------------  	|    :-------- 	|    :-----    	|    :-------------------- 	|
|    type                         |    string   	|    Yes   	|    类型<br>CURRENT_RESOURCE,当前资源;<br>REMOTE_RESOURCE,远程资源	|
|    url                        	|    string  	|    No    	|    资源URL,type为CURRENT_RESOURCE时url不存在				|

```json
{
    "event": {
        "header": {
            "namespace": "TvsMediaControl",
            "name": "DownloadSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "url": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            	|    Type    	|    必选 	|    描述              				|
|    :----------------------    	|    :-------- 	|    :-------  	|    :-------------------------------- 	|
|    messageId 			|    string  	|    Yes    	|    消息ID                        	|

***Payload Paramters***

|    Parameter            		|    Type    	|    必选  	|    描述             	|
|    :---------------------------  	|    :-------- 	|    :-----    	|    :-------------------- 	|
|    type                         |    string   	|    Yes   	|    类型<br>CURRENT_RESOURCE,当前资源;<br>REMOTE_RESOURCE,远程资源	|
|    url                        	|    string  	|    No    	|    资源URL,type为CURRENT_RESOURCE时url不存在				|

```json
{
    "event": {
        "header": {
            "namespace": "TvsMediaControl",
            "name": "DownloadFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "url": "{{STRING}}"
        }
    }
}    
```

***Header Paramters***

|    Parameter            	|    Type    	|    必选 	|    描述              				|
|    :----------------------    	|    :-------- 	|    :-------  	|    :-------------------------------- 	|
|    messageId 			|    string  	|    Yes    	|    消息ID                        	|

***Payload Paramters***

|    Parameter            		|    Type    	|    必选  	|    描述             	|
|    :---------------------------  	|    :-------- 	|    :-----    	|    :-------------------- 	|
|    type                         |    string   	|    Yes   	|    类型<br>CURRENT_RESOURCE,当前资源;<br>REMOTE_RESOURCE,远程资源	|
|    url                        	|    string  	|    No    	|    资源URL,type为CURRENT_RESOURCE时url不存在				|

