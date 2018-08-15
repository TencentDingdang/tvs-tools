[TOC]

### 领域名称

音乐

### 意图列表

| Intent              | Description                         |
| ------------------  | ----------------------------------- |
| play                | 来点音乐                            |
| play_album          | 听七里香专辑                        |
| play_songid         | 明确语义，歌曲ID拉歌曲详情          |
| play_in_times       | 播放5遍冰雨                         |
| play_favorite       | 播放我的收藏                        |
| play_chorus         | 播冰雨的副歌                        |
| play_more           | 拉取更多                            |
| play_albumid        | 明确语义，专辑ID拉取专辑详情        |
| change_version      | 换个版本                            |
| prev                | 上一个                              |
| next                | 下一个                              |
| ------------------  | ----------------------------------- |
| play_mv             | 下一个                              |
| play_mvid           | 明确语义，MV ID拉MV详情             |
| ------------------  | ----------------------------------- |
| search_song         | 刘德华唱过什么歌                    |
| search_album        | 冰雨是哪张专辑的                    |
| search_singer       | 冰雨是谁唱的                        |
| search_song_property| 冰雨的作词是谁                      |
| delete_favorite     | 删除我的收藏                        |
| add_favorite        | 把这首歌添加到收藏                  |
| search_song_qq      | 明确语义                            |
| pay                 | 开通音乐会员                        |
| search_cur_song_remind | 明确语义                         |
| search_cur_song     | 这首歌叫什么名字                    |
| search_prev_song    | 上首歌叫什么名字                    |

### 数据示例

##### play play_album 等意图，音频类模版

```json
/*
 * play play_album 等意图，音频类模版
 * 语料：来点音乐
 * BOT：TVS音箱 (c76f35f0-37f3-4f91-bf40-2bce9211e9b5)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "好的，那就先听周杰伦的不爱我就拉倒吧。",
	"strSpeakTipsText": "好的，那就先听周杰伦的不爱我就拉倒吧。"
}
// ======================= Json 数据 =======================
{
	"baseInfo": {
		"skillName": "QQ音乐"
	},
	"controlInfo": {
		"textSpeak": "false",
		"type": "AUDIO"
	},
	"listItems": [{
		"audio": {
			"metadata": {
				"totalMilliseconds": 250
			},
			"stream": {
				"url": "http://isure.stream.qqmusic.qq.com/C200003ovdJ13t6YIs.m4a?guid=2000001810&vkey=1EE1BAC8F2827F0BE27AE4086D6272976EDF2E28D7BAFB562E94460FC3A5B376E6DDDA8B6F10EE870725056CA0D1705D19457D12AF0E8339&uin=&fromtag=50"
			}
		},
		"htmlView": "",
		"image": {
			"sources": [{
				"url": "http://imgcache.qq.com/music/photo_new/T002R500x500M000001RsOK33No4Sz.jpg"
			}]
		},
		"mediaId": "213473236",
		"selfData": {
			"album": "南方有乔木 电视剧原声带",
			"albumId": "3976784",
			"albumPubTime": "",
			"hot": 0,
			"lyrics": "",
			"mvId": "",
			"singer": "金池",
			"song": "有没有这样一种关系",
			"songId": "213473236",
			"tryBegin": 0,
			"tryEnd": 0,
			"tvfilm": ""
		},
		"textContent": "QQ音乐 - 南方有乔木 电视剧原声带",
		"title": "有没有这样一种关系 - 金池",
		"video": {
			"metadata": {
				"totalMilliseconds": 0
			},
			"sources": []
		}
	}]
}
```
##### play_mvid play_mv 视频模版

```json
/*
 * play_mvid play_mv 视频模版
 * 语料：播首周杰伦的mv
 * BOT：dobby大脑 (0decaf62-5296-4e23-9214-12840b01cedd)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "好的",
	"strSpeakTipsText": "好的"
}
// ======================= Json 数据 =======================
{
	"baseInfo": {
		"skillName": "QQ音乐"
	},
	"controlInfo": {
		"textSpeak": "false",
		"type": "VIDEO"
	},
	"listItems": [{
		"audio": {
			"metadata": {
				"totalMilliseconds": 0
			},
			"stream": {
				"url": ""
			}
		},
		"htmlView": "http://y.qq.com/w/mv.html?vid=j0026ob1xbs",
		"image": {
			"sources": [{
				"url": "http://puui.qpic.cn/qqvideo_ori/0/j0026ob1xbs_496_280/0"
			}]
		},
		"mediaId": "1463760",
		"selfData": {
			"album": "",
			"albumId": "",
			"albumPubTime": "2018-5-15",
			"hot": 0,
			"lyrics": "",
			"mvId": "1463760",
			"singer": "周杰伦",
			"song": "不爱我就拉倒",
			"songId": "",
			"tryBegin": 0,
			"tryEnd": 0,
			"tvfilm": ""
		},
		"textContent": "QQ音乐",
		"title": "不爱我就拉倒 - 周杰伦",
		"video": {
			"metadata": {
				"totalMilliseconds": 250
			},
			"sources": [{
				"url": "https://aiwx.sparta.html5.qq.com/resource/search?id=10005&slots=pm=dNAPhgJ0ncgGroLvGLImx6ABSgpjlGL1;mvid=1463760"
			}]
		}
	}]
}
```

##### search_song search_album 纯文本模版

```json
/*
 * search_song search_album 纯文本模版
 * 语料：刘德华唱过什么歌
 * BOT：腾讯叮当App (ad415e3e-643c-489a-88ca-3fda41f976c1)
*/ 
// ======================= 回复语 =======================
{
	"strTipsText": "刘德华唱过如果你是我的传说,慢慢习惯等歌曲",
	"strSpeakTipsText": "刘德华唱过如果你是我的传说,慢慢习惯等歌曲"
}
// ======================= Json 数据 =======================
{
	"baseInfo": {
		"skillName": "QQ音乐"
	},
	"controlInfo": {
		"textSpeak": "false",
		"type": "TEXT"
	},
	"listItems": [{
		"audio": {
			"metadata": {
				"totalMilliseconds": 0
			},
			"stream": {
				"url": ""
			}
		},
		"htmlView": "",
		"image": {
			"sources": []
		},
		"mediaId": "",
		"selfData": {
			"album": "",
			"albumId": "",
			"albumPubTime": "",
			"hot": 0,
			"lyrics": "",
			"mvId": "",
			"singer": "",
			"song": "",
			"songId": "",
			"tryBegin": 0,
			"tryEnd": 0,
			"tvfilm": ""
		},
		"textContent": "",
		"title": "刘德华唱过不少歌，如果你是我的传说和慢慢习惯都很好听",
		"video": {
			"metadata": {
				"totalMilliseconds": 0
			},
			"sources": []
		}
	}]
}
```
