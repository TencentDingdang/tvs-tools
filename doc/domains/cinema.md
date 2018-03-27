# 院线
### cinama.film_search
#### 问法
最近电影
#### JSON
```json
{
    "sLink": "http://m.maoyan.com/", //电影列表H5页面
    "sMessage": "为你找到以下电影", //提示语
    "vecMovies": [
    {
        "iBuyFlag": 1, //是否可买
        "iID": 249894, //id
        "sActor": "克里斯·海姆斯沃斯,凯特·布兰切特,汤姆·希德勒斯顿", //主演
        "sBuyLink": "http://m.maoyan.com/cinema/movie/249894?_v_=yes&lat=22.54043&lng=113.93454", //购买H5页面链接
        "sDetail": "本片讲述了雷神托尔（克里斯·海姆斯沃斯 饰）残酷无情的海拉（凯特·布兰切特 饰）...",//电影简介 
        "sDirector": "塔伊加·维迪提", //导演
        "sLink": "http://m.maoyan.com/movie/249894?_v_=yes", //电影详情H5页面链接
        "sLongs": "130分钟",  //电影时长
        "sName": "雷神3：诸神黄昏",  //电影名称
        "sPostUrl": "http://p1.meituan.net/100.100/movie/579a0919e926a80ad14c717c8d8a8394259181.jpg", //电影封面
        "sScore": "8.9", //得分
        "sTime": "正在上映", //上映描述，其他形式如：2017.11.17上映
        "sType": "动作,冒险,奇幻" //电影类型
    }
     ...
    ]
}	
### cinama.cinema_search
#### 问法
附近电影院
#### JSON
```json
{
    "sLink": "http://m.maoyan.com/?type=cinema&_v_=yes&lat=22.54043&lng=113.93454", //电影院列表H5页面
    "sMessage": "为你找到以下电影院",  //提示语
    "vecCinemas": [
    {
            "dLatitude": 22.5425,  //纬度
            "dLongitude": 113.928, //经度
            "iID": 16597,   //id号
            "sAddr": "南头街道艺园东路缤纷年华家园商业裙楼301A-2号", //地址信息
            "sDistance": "0.67km",  //和当前位置的距离
            "sLink": "http://m.maoyan.com/shows/16597?_v_=yes",//电影院购买H5页面 
            "sName": "中影德金影城(南山店)", //电影院名称
    }
	....
	]
}

 
```