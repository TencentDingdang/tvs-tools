[TOC]

### 领域名称

智能家居

### 意图列表

| Intent                      | Description  |  示例  |
| --------------------------- | ------------ |-------|
| turn_on                     | 打开设备      | 开灯  |
| turn_off                    | 关闭设备      | 关灯  |
| color                       | 设置设备的颜色 | 把灯设置为蓝色 |
| color_temperature           | 设置设备的色温 | 灯的色温调高一点 |
| mode                        | 设置设备模式   | 空调设置为除湿模式 |
| state                       | 工作状态查询   | 客厅的灯开着吗  |
| fan_speed                   | 风量控制      |  风扇的风速调高  |
| brightness                  | 亮度控制      |  灯的亮度调高    |
| temperature                 | 温度控制      |  空调的温度设置为25度 |
| device_query                | 设备属性查询   |  空调的温度是多少  |

### 数据示例

##### 纯文本模版

| Intent                      | Description  |
| --------------------------- | ------------ |
| turn_on                     | 打开设备       |
| turn_off                    | 关闭设备       |
| color                       | 设置设备的颜色  |
| color_temperature           | 设置设备的色温  |
| mode                        | 设置设备模式    |
| state                       | 工作状态查询     |
| fan_speed                   | 风量控制     |
| brightness                  | 亮度控制      |
| temperature                 | 温度控制      |
| device_query                | 设备属性查询 |

```json
/*
 * 无模版
*/ 
{
    "controlInfo": {
        "audioConsole": "true", 
        "textSpeak": "false", 
        "titleSpeak": "false", 
        "version": "1.0.0"
    }
}
```