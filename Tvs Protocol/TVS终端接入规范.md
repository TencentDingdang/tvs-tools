## TVS终端接入规范

### 协议要求

1.	接入TVS必须采用HTTP 2.0协议接入，并且一个终端只能建立一个到TVS的HTTP 2.0连接
2.	只有建立下行通道***(https://tvs.html5.qq.com/v20160207/directives)***的请求才能够创建TCP连接
3.	其他请求如果发现连接有问题，需要重建下行通道

### TVS数据和终端处理逻辑

#### 授权

* 请求：
	
	1. URL

		https://tvs.html5.qq.com/auth/o2/token

	2. 请求方式

		HTTP POST

	3.	请求数据

		```json
		{
			"grant_type":	"authorization_code",
			"code":	"{{STRING}}",
			"redirect_uri": "{{STRING}}",
			"client_id": "{{STRING}}",
			"code_verifier": "{{STRING}}"
		}
		```
		|	Parameter			|	Type		|	必选	|	描述																	|
		|	:-------------------	|	:--------	|	:-----	|	:----------------------------------------------------------------------	|
		|	grant_type			|	string	|	Yes	|	请求类型(必须为authorization_code)					|
		|	code					|	string	|	Yes	|	获取票据授权Code(如果手机端没有传递，空白)	|
		|	redirect_uri		|	string	|	Yes	|	重定向URL(如果手机端没有传递，空白)				|
		|	client_id			|	string	|	Yes	|	设备ID																|
		|	code_verifier		|	string	|	Yes	|	票据校验码(终端生成的随机字符串，最少43个字符，最大128个字符)				|

* 响应

	1. 	响应状态码说明

		(1) HTTP 200且数据完整

			终端授权成功，接下来终端发起建立下行通道请求

		(2) 其他情况(包括无响应)

			终端提示用户重新通过APP登录，并重新发起授权请求

	2.	响应数据

		```json
		{
			"access_token": "{{STRING}}",
			"refresh_token": "{{STRING}}",
			"token_type": "bearer",
			"expires_in": LONG
		}
		```
		|	Parameter			|	Type		|	必选	|	描述								|
		|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
		|	access_token	|	string	|	Yes	|	访问票据						|
		|	refresh_token		|	string	|	Yes	|	刷票票据						|
		|	token_type		|	string	|	Yes	|	访问票据类型					|
		|	expires_in			|	LONG	|	Yes	|	访问票据有效时间			|

#### 刷票

* 请求：

	1. URL

		https://tvs.html5.qq.com/auth/o2/token

	2. 请求方式

		HTTP POST

	3.	请求数据

		```json
		{
			"grant_type":	"refresh_token",
			"client_id": "{{STRING}}",
			"refresh_token": "{{STRING}}"
		}
		```
		|	Parameter			|	Type		|	必选	|	描述											|
		|	:-------------------	|	:--------	|	:-----	|	:-------------------------------------------	|
		|	grant_type			|	string	|	Yes	|	请求类型(必须为refresh_token)	|
		|	client_id			|	string	|	Yes	|	设备ID										|
		|	refresh_token		|	string	|	Yes	|	刷票票据									|

* 响应

	1. 	响应状态码说明

		(1) HTTP 200且数据完整

			终端刷票成功，接下来终端发起建立下行通道请求

		(2) 其他情况(包括无响应)

			终端重试(次数由终端控制)，若重试后仍然不成功，则提示用户重新通过APP登录，并重新发起授权请求

	2.	响应数据

		```json
		{
			"access_token": "{{STRING}}",
			"refresh_token": "{{STRING}}",
			"token_type": "bearer",
			"expires_in": LONG
		}
		```
		|	Parameter			|	Type		|	必选	|	描述								|
		|	:-------------------	|	:--------	|	:-----	|	:--------------------------------	|
		|	access_token	|	string	|	Yes	|	访问票据						|
		|	refresh_token		|	string	|	Yes	|	刷票票据						|
		|	token_type		|	string	|	Yes	|	访问票据类型					|
		|	expires_in			|	LONG	|	Yes	|	访问票据有效时间			|

####	构造HTTP头部Authorization

通过授权/刷票接口获取的access_token,token_type,终端即可自行构造HTTP头部的Authorization字段，Authorization格式如下：
	
	token_type Altz|access_token
	

#### 下行通道

* 请求：

	1. URL

		https://tvs.html5.qq.com/v20160207/directives

	2. 请求方式

		HTTP GET

	3.	HTTP头部

		*	Authorization

			访问凭据，必须携带

* 响应

	1. 响应方式

		(1) HTTP Chunked传输编码且为Multipart形式的数据

	2.	响应状态码说明

		(1) HTTP 200且没有收到完整的Multipart数据

			终端需要保持连接

		(2) 其他情况(包括无响应)

			终端重新发起建立下行通道连接请求

#### 连接探测

* 请求：

	1. URL

		https://tvs.html5.qq.com/ping

	2. 请求方式

		HTTP GET	

	3.	HTTP头部

		*	Authorization

			访问凭据，必须携带

* 响应

	1. 	响应状态码说明

		(1) HTTP 204

			终端无需做任何处理

		(2) 其他情况(包括无响应)

			终端重新发起建立下行通道连接请求

#### 上行通道

* 请求：	

	1. URL

		https://tvs.html5.qq.com/v20160207/events

	2. 请求方式

		HTTP POST

	3. HTTP头部
		
		*	Authorization

			访问凭据，必须携带

		*	Q-UA
			
			终端QUA，可以不携带，如果存在Q-UA2，则忽略

		*	Q-UA2

			终端QUA，可以不携带，如果存在Q-UA2，则忽略Q-UA

* 响应

	1. 响应方式

		(1) 非HTTP Chunked传输编码

		(2) HTTP Chunked传输编码

	2.	响应状态码说明

		(1) HTTP 204

			终端忽略响应

		(2) HTTP 200但是无数据(非HTTP Chunked编码)

			终端忽略响应并上报System:ExceptionEncountered事件

		(3) HTTP 200但是数据不完整(非HTTP Chunked编码)

			终端忽略响应并上报System:ExceptionEncountered事件

		(4) HTTP 200且数据完整(非HTTP Chunked编码)

			终端正常处理指令

		(5) HTTP 200但是无数据(HTTP Chunked编码)

			终端忽略响应并上报System:ExceptionEncountered事件

		(6) HTTP 200但是数据不完整(HTTP Chunked编码)

			终端忽略不完整的指令并上报System:ExceptionEncountered事件并结束处理

		(7) HTTP 200且数据完整(HTTP Chunked编码)

			终端正常处理指令

		(8) 无响应

			终端忽略