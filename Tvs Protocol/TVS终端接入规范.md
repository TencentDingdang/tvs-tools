##TVS终端接入规范

### 协议要求

	接入TVS必须采用HTTP 2.0协议接入，并且一个终端只能建立一个到TVS的HTTP 2.0连接

### TVS数据和终端处理逻辑

### #授权
	* 请求：	
		1. URL
			https://tvs.html5.qq.com/auth/o2/token
		2. 请求方式
			HTTP POST
	* 响应
		1. 	响应数据
			(1) HTTP 200且数据完整
				终端授权成功，接下来终端发起建立下行通道请求
			(2) 其他情况(包括无响应)
				终端提示用户重新通过APP登录，并重新发起授权请求

### #刷票
	* 请求：	
		1. URL
			https://tvs.html5.qq.com/auth/o2/token
		2. 请求方式
			HTTP POST
	* 响应
		1. 	响应数据
			(1) HTTP 200且数据完整
				终端刷票成功，接下来终端发起建立下行通道请求
			(2) 其他情况(包括无响应)
				终端重试(次数由终端控制)，若重试后仍然不成功，则提示用户重新通过APP登录，并重新发起授权请求

### #下行通道
	* 请求：	
		1. URL
			https://tvs.html5.qq.com/v20160207/directives
		2. 请求方式
			HTTP GET
	* 响应
		1. 响应方式
			(1) HTTP Chunked传输编码且为Multipart形式的数据
		2.	响应数据
			(1) HTTP 200且没有收到完整的Multipart数据
				终端需要保持连接
			(2) 其他情况(包括无响应)
				终端重新发起建立下行通道连接请求

### #连接探测
	* 请求：	
		1. URL
			https://tvs.html5.qq.com/ping
		2. 请求方式
			HTTP GET
	* 响应
		1. 	响应数据
			(1) HTTP 204
				终端无需做任何处理
			(2) 其他情况(包括无响应)
				终端重新发起建立下行通道连接请求

### #上行通道
	* 请求：	
		1. URL
			https://tvs.html5.qq.com/v20160207/events
		2. 请求方式
			HTTP POST
	* 响应
		1. 响应方式
			(1) 非HTTP Chunked传输编码
			(2) HTTP Chunked传输编码
		2.	响应数据
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
				
			
