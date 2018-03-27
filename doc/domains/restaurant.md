# 美食
### restaurant.*
#### 问法
推荐一下附近的川菜馆
#### JSON
```json
{
    "sCommRspData": {
        "eDataType": 9,
        "mapDataSource": {},
        "strAllUrl": "http://m.dianping.com/shoplist/7/r/0/c/10/s/s_-1",
        "vecCommDataBytes": []
    },
    "strJsonToSemantic": "",
    "strRspJsonData": "{
    "nPage": 0,
    "nPageSize": 0,
    "strAllUrl": "http://m.dianping.com/shoplist/7/r/0/c/10/s/s_-1",
    "vBusinessList": [
        {
            "nAvgPrice": 117,
            "nDistance": 367,
            "nHasCoupon": 0,
            "nHasDeal": 1,
            "nPoiDistance": 635,
            "nReviewCount": 1762,
            "strAddress": "南山区科技中三路海王银河大厦2楼",
            "strAvgRating": "4.5",
            "strBranchName": "海王银河店",
            "strBusinessUrl": "http://m.dianping.com/shop/27527380?utm_source=open&appKey=6400508795",
            "strCategory": "牛肉火锅",
            "strLat": "22.540590000000002",
            "strLng": "113.94159000000001",
            "strName": "原牛道牛肉火锅",
            "strPhone": "0755-22670471",
            "strPhotoUrl": "http://p1.meituan.net/msmerchant/4b1234268092ebf73f23fd034f8315da54977.jpg%40278w_200h_0e_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
        },
        {
            "nAvgPrice": 91,
            "nDistance": 2275,
            "nHasCoupon": 0,
            "nHasDeal": 1,
            "nPoiDistance": 1843,
            "nReviewCount": 5915,
            "strAddress": "南山区南头街279号",
            "strAvgRating": "4.5",
            "strBranchName": "南头店",
            "strBusinessUrl": "http://m.dianping.com/shop/27305282?utm_source=open&appKey=6400508795",
            "strCategory": "牛肉火锅",
            "strLat": "22.535865999999999",
            "strLng": "113.91818000000001",
            "strName": "汕头八合里海记牛肉店",
            "strPhone": "0755-86224670",
            "strPhotoUrl": "https://img.meituan.net/msmerchant/66c7fe7ea84f255afbe95a594cdc349c121140.jpg%40278w_200h_0e_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
        }
    ]
}",
    "strSpeakText": "没有找到你想要的餐馆，附近的餐馆有。原牛道牛肉火锅.海王银河店,人均114元\n汕头八合里海记牛肉店.南头店,人均88元\n汕头八合里海记牛肉店.海德店,人均91元\n",
    "strSpeakTipsText": "",
    "strTipsText": "没有找到你想要的餐馆，附近的餐馆有",
    "vecCandidateSemantic": [],
    "vecRspDataBytes": [],
    "vectRspDataItems": [
        {
            "eDataType": 1,
            "strContentData": "",
            "strContentID": "",
            "strContentURL": "",
            "strDescription": "",
            "strDestURL": "",
            "strDownloadURL": "",
            "strShareURL": "",
            "strTitle": "<a href=\"http://m.dianping.com/shop/27527380?utm_source=open&appKey=6400508795\">原牛道牛肉火锅 (海王银河店)</a>\n4.51615条评价\n牛肉火锅 ￥114/人\t0.5km\n\n<a href=\"http://m.dianping.com/shop/27305282?utm_source=open&appKey=6400508795\">汕头八合里海记牛肉店 (南头店)</a>\n4.55750条评价\n牛肉火锅 ￥88/人\t2.2km\n\n<a href=\"http://m.dianping.com/shop/57443607?utm_source=open&appKey=6400508795\">汕头八合里海记牛肉店 (海德店)</a>\n4.53838条评价\n牛肉火锅 ￥91/人\t3.0km\n\n<a href=\"http://m.dianping.com/shop/23127112?utm_source=open&appKey=6400508795\">云海肴云南菜 (海岸城店)</a>\n4.54880条评价\n云贵菜 ￥89/人\t3.0km\n\n<a href=\"http://m.dianping.com/shop/21167197?utm_source=open&appKey=6400508795\">浅葱小唱 (科技园店)</a>\n42507条评价\n川菜/家常菜 ￥84/人\t0.6km\n\n<a href=\"http://m.dianping.com/shop/21118014?utm_source=open&appKey=6400508795\">同仁四季音乐主题餐厅 (南山LOFT店)</a>\n45762条评价\n火锅 ￥105/人\t1.9km\n\n<a href=\"http://m.dianping.com/shop/32631110?utm_source=open&appKey=6400508795\">姜虎东白丁烤肉 (创业路店)</a>\n4.55053条评价\n韩国料理 ￥117/人\t3.4km\n\n<a href=\"http://m.dianping.com/shop/32529627?utm_source=open&appKey=6400508795\">唐宫小聚 (海岸城店)</a>\n44273条评价\n粤菜馆 ￥93/人\t3.0km\n\n"
        }
    ]
}
```

###字段说明

<pre>
string strName;         //商户名称

int nReviewCount;       //评价条数

int nAvgPrice;          //人均价格

int nDistance;          //商户与参数坐标的距离，单位为米

string strBusinessUrl;  //商户页面链接

string strPhotoUrl;     //小尺寸照片链接，照片最大尺寸278×200

string strAvgRating;    //星级评分，5.0代表五星，4.5代表四星半，依此类推

string strBranchName;   //分店名

string strCategory;     //分类名

string strAddress;      //商户地址

string strPhone;        //电话

string strLat;          //纬度

string strLng;          //经度

int nHasCoupon;         //是否有优惠券，0:没有，1:有

int nHasDeal;           //是否有团购，0:没有，1:有

int nPoiDistance;       //经纬度之间的距离
</pre>