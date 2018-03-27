# 查周边
### surround.search
#### 问法
腾讯大厦附近的停车场
#### JSON
```json
{
    "errorMsg": "",
    "errorNo": 0,
    "moreUrl": "http://apis.map.qq.com/tools/poimarker?type=1&keyword=综合医院&center=22.54049,113.9349&radius=3000&init_view=2&key=3C3BZ-CJDKR-VCWWH-WPXST-GZTYJ-NBFJG&referer=dobby",     // 更多链接
    "spots": [  // 周边地点列表
        {
            "addr": "广东省深圳市南山区南海大道3688号深圳大学",       // 地址
            "category": "医疗保健:综合医院",                        // 类型
            "detailUrl": "http://apis.map.qq.com/uri/v1/marker?marker=coord:22.5323,113.93867;title:深圳大学校医院;addr:广东省深圳市南山区南海大道3688号深圳大学;uid:2222134682728972109&referer=dobby", // 详情页面
            "distance": 990,        // 距离
            "location": {
                "adcode": "440305",
                "city": "深圳市",      // 城市
                "coordType": 5,
                "distict": "南山区",   // 区/县
                "lat": 22.5323,         // 纬度
                "lng": 113.939,         // 精度
                "nation": "",           // 国家
                "province": "广东省",  // 省份
                "street": "南海大道3688号深圳大学",      // 街道
                "streetNum": ""         // 门牌号
            },
            "naviUrl": "http://apis.map.qq.com/uri/v1/routeplan?type=drive&to=深圳大学校医院&tocoord=22.5323,113.93867&policy=0&referer=dobby",        // Web导航地址
            "tel": "",      // 电话
            "title": "深圳大学校医院",     // 名称
            "type": 0
        }
    ],
    "staticMapUrl": "http://apis.map.qq.com/ws/staticmap/v2/?center=22.54049,113.9349&markers=22.5323,113.939&markers=22.5467,113.946&markers=22.5315,113.924&zoom=16&size=800*450&maptype=roadmap&key=3C3BZ-CJDKR-VCWWH-WPXST-GZTYJ-NBFJG&referer=dobby"       // 静态图地址
}
```
