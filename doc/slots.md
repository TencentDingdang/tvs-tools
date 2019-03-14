# richanswer语义slots说明

## 1. slots结构

```json
"slots":[
    {
        "name":"{{STRING}}",
        "value":"{{STRING}}",
        "country":"{{STRING}}",
        "province":"{{STRING}}",
        "city":"{{STRING}}",
        "district":"{{STRING}}",
        "town":"{{STRING}}",
        "village":"{{STRING}}",
        "residual":"{{STRING}}"
    }
]

```



| 参数名                                | 类型       | 描述                                       |
| ---------------------------------- | -------- | ---------------------------------------- |
| `name`      |`string`| 语义槽名称，对于以`__complex`结尾的（循环日期），`value`数据特殊的解析规则 |
| `value`     |`string` | 语义槽的值|
| `country`     |`string` | 国家，比如“中国”。只有地址实体的槽位才有|
| `province`     |`string` | 省，比如“四川省”。只有地址实体的槽位才有|
| `city`     |`string` | 市，比如“成都市”。只有地址实体的槽位才有|
| `district`     |`string` |区、县，比如“高新区”。只有地址实体的槽位才有|
| `town`     |`string` | 镇，比如“中和镇”。只有地址实体的槽位才有|
| `village`     |`string` | 村，比如“中和村”。只有地址实体的槽位才有|
| `residual`     |`string` | 剩余字段，原串即去掉行政区域后的剩余字段，可能表示poi，比如“腾讯大厦”，或是一些无意义的词。只有地址实体的槽位才有|


如果不是地址实体，只需要解析`name`和`value`。

## 2. `__complex`结尾槽位

`__complex`是当key/value形式无法解释语义时定义的结构，目前支持循环日期时间的数据。

对于循环日期时间的数据 `value`的结构如下：

```json


{
    "type":{{INT}},
    "data":{
        "repeat_type":{{INT}},
        "start_date":"{{STRING}}",
        "start_time":"{{STRING}}"
    }
}
```


| 参数名                                | 类型       | 描述                                       |
| ---------------------------------- | -------- | ---------------------------------------- |
| `type`      |`string`| 日期类型。 |固定4|
| `data`     |`object` | 语义槽的值|
| `data.repeat_type`     |`string` | 重复类型，<br>1：按年重复<br> 2：按月重复<br> 3：按周重复<br> 4：按天重复<br> 5：按小时重复<br> 6：按分钟重复<br> 7：按工作日重复<br> 8：按周末重复|
| `data.start_date`     |`string` | 开始日期，YYYY-MM-DD，比如“2018-07-30”|
| `data.start_time`     |`string` | 开始时刻，HH:MM:SS，比如“10:00:00”|





