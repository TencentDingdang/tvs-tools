## 声音百科

### 控制类型

循环控制		E_CHILD_SOUND_PLAY_TYPE

播放时长		sDurationTime



### 数据类型

前置回复语	strSpeakText

后置回复语	sResText

资源URL数组	vUrlInfo



### 协议

```c++
// 结构体定义

enum E_CHILD_SOUND_PLAY_TYPE{
  E_CHILD_SOUND_PLAY_ONCE		=	0;			//普通播放
  E_CHILD_SOUND_PLAY_CYCLE		=	1;			//循环播放
  E_CHILD_SOUND_PLAY_DURATION	=	2;			//控制播放时长 联合 sDurationTime 使用
};
struct SourceUrl{
  0 optional string sName;						//资源名称
  1 optional string sUrl;						//资源播放链接
  2 optional string sUrlId;						//资源ID
};
// json结构
struct ChildSoundResponseRsp{
  0 optional string sResText;					//后置回复语
  1 optional vector<SourceUrl> vUrlInfo;		//资源Url
  2 optional E_CHILD_SOUND_PLAY_TYPE eType;		//控制类型
  3 optional string sDurationTime;				//播放时长  eType == E_CHILD_SOUND_PLAY_DURATION 有效
};
```



### 示例

```json
strSpeakText: "我是前置回复语，需要在播放资源url前播放我",
ChildSoundResponseRsp:{
  sResText: "我是后置回复语，播放完资源url后播放我",
  vUrlInfo: [
  	{
  	  sName: "吃苹果",
      sUrl: "http://softfile.3g.qq.com/myapp/soft_imtt/smartChildVoice/eatApple.mp3"
	},
    {
    	sName: "风声",
      	sUrl: "http://softfile.3g.qq.com/myapp/soft_imtt/smartChildVoice/wind.mp3"
	}
  ],
  eType: 2,
  sDurationTime: 1800										// 单位 秒
}
```

