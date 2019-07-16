### HTTP头部
* Authorization
	* 必选:

		是

	* 格式:

		token_type Altz|access_token

		* access_token:

			通过authorize/refresh接口获取的票据

		* token_type:

			通过authorize/refresh接口获取的票据类型


* TvsSettings
	* 必选:

		否

	* 格式:

		 Key1=Value1;Key2=Value2;...;KeyN=ValueN

		* 沙箱模式:

			env=sandbox

* Q-UA
	* 必选:

		否

	* 格式: 

		Key1=Value&Key2=Value2&...&KeyN=ValueN

		* VN:

			终端版本号，必须 >= 1.0.0.0001

	* 默认值(终端不传递,服务端自动填写):

		QV=3&PL=ADR&PR=TVS&VE=GA&VN=1.0.0.0001&PP=com.tencent.ai.tvs&DE=SPEAKER