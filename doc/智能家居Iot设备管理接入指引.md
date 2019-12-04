# 智能家居设备管理接入指引

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [智能家居设备管理接口](#智能家居设备管理接口)
	- [query_skills接口](#queryskills接口)
		- [request](#request)
		- [response](#response)
	- [query_devices接口](#querydevices接口)
		- [request](#request)
		- [response](#response)
	- [discover_devices接口](#discoverdevices接口)
		- [request](#request)
		- [response](#response)
	- [manage_devices接口](#managedevices接口)
		- [request](#request)
		- [response](#response)
	- [get_device_rename_info接口](#getdevicerenameinfo接口)
		- [request](#request)
		- [response](#response)
	- [disable_skill接口](#disableskill接口)
		- [request](#request)
		- [response](#response)
	- [公共参数](#公共参数)
		- [ErrorInfo](#errorinfo)

<!-- /TOC -->

## 智能家居设备管理接口

智能家居设备管理依赖于腾讯云叮当TVS [unieAccess](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/uniAccess%E6%8E%A5%E5%8F%A3%E8%83%BD%E5%8A%9B.md)通道能力，在使用uniAccess时需要通过设置`payload.domain`和`payload.intent`路由到不同的智能家居设备管理接口，并且需要填充符合叮当规范的账号、设备信息。智能家居设备管理接口包括：

| domain    |    intent    | 接口说明 |
|-----------|--------------|---------|
| smarthome | query_skills | 查询平台所有的智能家居技能信息 |
| smarthome | query_devices| 查询指定技能的所有已绑定的设备列表 |
| smarthome | discover_devices | 查询指定技能的所有未关联的设备列表 |
| smarthome | manage_devices | 提供两种设备管理能力：<br>1. 绑定设备并命名；<br>2. 解绑指定设备；|
| smarthome | get_device_rename_info | 获取指定设备可用的命名信息 |
| smarthome | disable_skill | 停止使用指定技能，解除账号关联 |

### query_skills接口
用于查询平台所有的智能家居技能信息。

#### request

+ 请求数据示例
```json
{
    "operType": "query_skills",
    "get_account_state": true
}
```

+ 参数说明

| 参数 | 说明 | 参数说明 |
|------|-----|---------|
| `operType` | 操作类型，值同`intent`，固定为`query_skills`| `string` |
| `get_account_state` | 是否需要返回技能的账号关联状态，若需要设为`true`，设置之后需要更长的接口耗时 | `bool` |

#### response

+ 响应数据示例

```json
{
    "sError": ErrorInfo,
    "vSkills": [ {
      "strDescription": "绑定BroadLink账号后，可以语音控制家中的BroadLink智能设备，比如：“叮当叮当，打开灯”",
      "strSkillIcon": "https://softimtt.myapp.com/browser/smart_service/smarthome/skill_icons/broadlink.png",
      "strSkillId": "140bde24-57e4-11e8-8130-68cc6ea8c1f8",
      "strSkillName": "BroadLink",
      "strSkillType": "NORMAL",
      "eAccountState": 1
    } ]
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `sError` | 错误信息，见[ErrorInfo](./#errorinfo) | `object` |
| `vSkills` | 技能列表 | `array` |
| `vSkills.strSkillId` | 技能ID | `string` |
| `vSkills.strSkillName` | 技能名称 | `string` |
| `vSkills.strSkillIcon` | 技能图标 | `string` |
| `vSkills.strDescription` | 技能描述 | `string` |
| `vSkills.strSkillType` | 技能类型，目前有：<br> `NORMAL`：普通智能家居技能；<br> `MIOT`：MIOT技能，需要终端特殊支持； | `string` |
| `vSkills.eAccountState` | 技能的账号绑定状态<br> `0`：未绑定；<br> `1`：已绑定； | `int` |


### query_devices接口
查询指定技能的所有已绑定的设备列表。

#### request

+ 请求数据示例
```json
{
    "operType": "query_devices",
    "skill_id": "..."
}
```

+ 参数说明

| 参数 | 说明 | 参数说明 |
|------|-----|---------|
| `operType` | 操作类型，值同`intent`，固定为`query_devices`| `string` |
| `skill_id` | 技能ID | `string` |

#### response

+ 响应数据示例

```json
{
    "sError": ErrorInfo,
    "vDevices": [ {
      "strDeviceId": "....",
      "strDeviceName": "....",
      "strDeviceIcon": "...",
      "eDeviceState": 1,
      "eConnectState": 1,
      "strRoom": "...",
      "strType": "..."
    } ]
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `sError` | 错误信息，见[ErrorInfo](./#errorinfo) | `object` |
| `vSkills` | 技能列表 | `array` |
| `vSkills.strDeviceId` | 设备ID | `string` |
| `vSkills.strDeviceName` | 设备名称 | `string` |
| `vSkills.strDeviceIcon` | 设备图标 | `string` |
| `vSkills.strRoom` | 设备所在房间 | `string` |
| `vSkills.strType` | 设备名称/设备类型名 | `string` |
| `vSkills.eDeviceState` | 设备状态：<br> `0`：离线；<br> `1`：在线； | `int` |
| `vSkills.eConnectState` | 设备绑定状态：<br> `0`：未绑定；<br> `1`：已绑定； | `int` |

### discover_devices接口
查询指定技能的所有未绑定的设备列表。

#### request

+ 请求数据示例
```json
{
    "operType": "discover_devices",
    "skill_id": "..."
}
```

+ 参数说明

| 参数 | 说明 | 参数说明 |
|------|-----|---------|
| `operType` | 操作类型，值同`intent`，固定为`discover_devices`| `string` |
| `skill_id` | 技能ID | `string` |

#### response

+ 响应数据示例

```json
{
    "sError": ErrorInfo,
    "vDevices": [ {
      "strDeviceId": "....",
      "strDeviceName": "....",
      "strDeviceIcon": "...",
      "eDeviceState": 1,
      "eConnectState": 1,
      "strRoom": "...",
      "strType": "..."
    } ]
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `sError` | 错误信息，见[ErrorInfo](./#errorinfo) | `object` |
| `vSkills` | 技能列表 | `array` |
| `vSkills.strDeviceId` | 设备ID | `string` |
| `vSkills.strDeviceName` | 设备名称 | `string` |
| `vSkills.strDeviceIcon` | 设备图标 | `string` |
| `vSkills.strRoom` | 设备所在房间 | `string` |
| `vSkills.strType` | 设备名称/设备类型名 | `string` |
| `vSkills.eDeviceState` | 设备状态：<br> `0`：离线；<br> `1`：在线； | `int` |
| `vSkills.eConnectState` | 设备绑定状态：<br> `0`：未绑定；<br> `1`：已绑定； | `int` |

### manage_devices接口
提供两种设备管理能力：
1. 绑定设备并命名；
2. 解绑指定设备。

#### request

+ 请求数据示例
```json
{
    "operType": "manage_devices",
    "skill_id": "...",
    "devices": [{
        "device_id": "...",
        "room": "...",
        "type": "...",
        "selected": true
    }]
}
```

+ 参数说明

| 参数 | 说明 | 参数说明 |
|------|-----|---------|
| `operType` | 操作类型，值同`intent`，固定为`manage_devices`| `string` |
| `skill_id` | 技能ID | `string` |
| `devices` | 设备列表 | `array` |
| `devices[].device_id` | 设备ID | `string` |
| `devices[].room` | 设备所在房间 | `string` |
| `devices[].type` | 设备名称/设备类型名 | `string` |
| `devices[].selected` | 设备设备是否绑定 | `bool` |

#### response

+ 响应数据示例

```json
{
    "sError": ErrorInfo
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `sError` | 错误信息，见[ErrorInfo](./#errorinfo) | `object` |


### get_device_rename_info接口
获取指定设备可用的命名信息

#### request

+ 请求数据示例
```json
{
    "operType": "get_device_rename_info",
    "skill_id": "...",
    "device_id": "..."
}
```

+ 参数说明

| 参数 | 说明 | 参数说明 |
|------|-----|---------|
| `operType` | 操作类型，值同`intent`，固定为`get_device_rename_info`| `string` |
| `skill_id` | 技能ID | `string` |
| `device_id` | 设备ID | `string` |

#### response

+ 响应数据示例

```json
{
    "sError": ErrorInfo,
    "vRooms": ["客厅", "卧室"],
    "vAvailableNames": [{
        "strGroup": "灯",
        "vNames": ["台灯", "吸顶灯"]
    }]
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `sError` | 错误信息，见[ErrorInfo](./#errorinfo) | `object` |
| `vRooms` | 房间名列表 | `array` |
| `vRooms` | 可用名称 | `array` |
| `vRooms[].strGroup` | 分类 | `string` |
| `vRooms[].vNames` | 设备名列表 | `array` |

### disable_skill接口
停止使用指定技能，解除账号关联。

#### request

+ 请求数据示例
```json
{
    "operType": "disable_skill",
    "skill_id": "..."
}
```

+ 参数说明

| 参数 | 说明 | 参数说明 |
|------|-----|---------|
| `operType` | 操作类型，值同`intent`，固定为`disable_skill`| `string` |
| `skill_id` | 技能ID | `string` |

#### response

+ 响应数据示例

```json
{
    "sError": ErrorInfo,
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `sError` | 错误信息，见[ErrorInfo](./#errorinfo) | `object` |


### 公共参数
#### ErrorInfo

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|---------|
| `iRet` | 错误码，包含：<br> `0`：成功；<br> `-1`：请求失败/异常；<br> `101`：授权信息过期或不存在，需要重新授权； | `int` |
| `strMsg` | 错误信息 | `string` |
| `strAuthUrl` | 重新授权地址，当`iRet`为`101`时返回 | `string` |
