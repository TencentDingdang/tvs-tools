### 呼叫指令
```json
{
    "directive": {
        "header": {
            "namespace": "Communication",
            "name": "Call",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}",
            "type": "Phone",
            "contacts": [
                {
                    "name": "{{STRING}}",
                    "number": "{{STRING}}"
                }
            ]
        }
    }
}
```

***Header Paramters***

|    Parameter            	|    Type    	|    必选	|    描述                          	|
|    :-------------------    	|    :--------	|    :-----	|    :-------------------------------- 	|
|    messageId          	|    string  	|    Yes 	|    消息ID                         	|
|    dialogRequestId   	|    string  	|    No 	|    对话ID                         	|

***Payload Paramters***

|    Parameter               	|    Type    	|    必选	|    描述                       	|
|    :---------------------------  	|    :-------- 	|    :----- 	|    :---------------------------  	|
|    token                      	|    string  	|    Yes 	|    token                      	|
|    type                        	|    string  	|    Yes	|    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    contacts                 	|    array   	|    Yes	|    联系人列表                |
|    contacts[].name       	|    string  	|    Yes 	|    联系人名称                |
|    contacts[].number   	|    string  	|    Yes 	|    联系人号码                |

### 开始呼叫事件
    在开始呼叫前，上报即将开始呼叫事件
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "CallWillStart",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    token                        |    string    |    Yes    |    token                        |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |

### 呼叫结束事件
    呼叫完成后，上报呼叫完成事件
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "CallFinished",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "Phone",
            "token": "{{STRING}}",
            "timeInMilliSeconds": {{LONG}}
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter              	|    Type   	|    必选    	|    描述                            |
|    :--------------------------- 	|    :-------- 	|    :-----		|    :---------------------------    |
|    token                     	|    string  	|    Yes 		|    token                        |
|    type                       	|    string  	|    Yes    	|    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    timeInMilliSeconds	|    long   	|    Yes    	|    通话时长                    |

### 未找到联系人事件
    如果有联系人未找到，终端上报联系人未找到事件，并带上未找到的联系人列表
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "ContactNotFound",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "token": "{{STRING}}",
            "contacts": [
                {
                    "name": "{{STRING}}",
                    "number": "{{STRING}}"
                }
            ]
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    token                        |    string    |    Yes    |    token                        |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    contacts                    |    array        |    Yes    |    联系人列表                |
|    contacts[].name            |    string    |    Yes    |    联系人名称                |
|    contacts[].number        |    string    |    Yes    |    联系人号码                |

### 找到多个号码事件
    如果找到多个号码，则发送该事件给TVS
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "MultiNumberFound",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "token": "{{STRING}}",
            "contacts": [
                {
                    "name": "{{STRING}}",
                    "number": "{{STRING}}"
                }
            ]
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    token                        |    string    |    Yes    |    token                        |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    contacts                    |    array        |    Yes    |    联系人列表                |
|    contacts[].name            |    string    |    Yes    |    联系人名称                |
|    contacts[].number        |    string    |    Yes    |    联系人号码                |

### 收到呼叫事件
    收到呼叫时触发该事件
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "CallComingUp",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "contact": {
                "name": "{{STRING}}",
                "number": "{{STRING}}"
            }
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    contacts                    |    array        |    Yes    |    联系人列表                |
|    contacts[].name            |    string    |    Yes    |    联系人名称                |
|    contacts[].number        |    string    |    Yes    |    联系人号码                |

### 接听指令
```json
{
    "directive": {
        "header": {
            "namespace": "Communication",
            "name": "Answer",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId   	|    string  	|    No 	|    对话ID                         	|

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    token                        |    string    |    Yes    |    token                        |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |

### 接听成功事件
    收到呼叫时触发该事件
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "AnswerSucceeded",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "contact": {
                "name": "{{STRING}}",
                "number": "{{STRING}}"
            }
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    contacts                    |    array        |    Yes    |    联系人列表                |
|    contacts[].name            |    string    |    Yes    |    联系人名称                |
|    contacts[].number        |    string    |    Yes    |    联系人号码                |

### 接听失败事件
    收到呼叫时触发该事件
```json
{
    "event": {
        "header": {
            "namespace": "Communication",
            "name": "AnswerFailed",
            "messageId": "{{STRING}}"
        },
        "payload": {
            "type": "{{STRING}}",
            "contact": {
                "name": "{{STRING}}",
                "number": "{{STRING}}"
            }
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |
|    contacts                    |    array        |    Yes    |    联系人列表                |
|    contacts[].name            |    string    |    Yes    |    联系人名称                |
|    contacts[].number        |    string    |    Yes    |    联系人号码                |

### 挂断指令
```json
{
    "directive": {
        "header": {
            "namespace": "Communication",
            "name": "HangUp",
            "messageId": "{{STRING}}",
            "dialogRequestId": "{{STRING}}"
        },
        "payload": {
            "token": "{{STRING}}"
        }
    }
}
```

***Header Paramters***

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |
|    dialogRequestId   	|    string  	|    No 	|    对话ID                         	|

***Payload Paramters***

|    Parameter                    |    Type        |    必选    |    描述                            |
|    :---------------------------    |    :--------    |    :-----    |    :---------------------------    |
|    token                        |    string    |    Yes    |    token                        |
|    type                            |    string    |    Yes    |    类型<br>Phone,电话;<br>VideoCall,视频通话    |

### 通话参数指令
```json
{
    "directive": {
        "header": {
            "namespace": "Communication",
            "name": "CallingInput",
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

|    Parameter            |    Type        |    必选    |    描述                                |
|    :-------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    messageId            |    string    |    Yes    |    消息ID                            |

***Payload Paramters***

|    Parameter                                |    Type        |    必选    |    描述                                |
|    :---------------------------------------    |    :--------    |    :-----    |    :--------------------------------    |
|    nlpInfo                                    |    object    |    Yes    |    NLP信息                        |
|    nlpInfo.domain                        |    string    |    Yes    |    NLP领域信息                    |
|    nlpInfo.intent                            |    string    |    Yes    |    NLP意图信息                    |
|    nlpInfo.parameters                    |    array        |    Yes    |    NLP参数信息                    |
|    nlpInfo.parameters[].name        |    string    |    Yes    |    NLP参数名称                    |
|    nlpInfo.parameters[].valueList    |    array        |    Yes    |    NLP参数值                    |