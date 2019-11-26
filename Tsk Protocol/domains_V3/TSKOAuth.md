# 技能账号授权管理

## uniAccess管理接口

依赖于腾讯云小微TVS [unieAccess](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/uniAccess%E6%8E%A5%E5%8F%A3%E8%83%BD%E5%8A%9B.md)通道能力，在使用uniAccess时需要通过设置`payload.domain`和`payload.intent`路由到不同接口，并且需要填充符合叮当规范的账号、设备信息，uniAccess接口可以通过[HTTP的方式（见“特殊能力访问接口”）](https://github.com/TencentDingdang/tvs-tools/blob/master/doc/%E8%85%BE%E8%AE%AF%E5%8F%AE%E5%BD%93HTTP%E6%96%B9%E5%BC%8F%E6%8E%A5%E5%85%A5API%E6%96%87%E6%A1%A3.md#55-%E7%89%B9%E6%AE%8A%E8%83%BD%E5%8A%9B%E8%AE%BF%E9%97%AE)接入，也可以通过DMSDK的uniAccess接口进行访问（[Android文档](https://dingdang.qq.com/doc/page/344)、[iOS文档](https://dingdang.qq.com/doc/page/351)）。账号开放授权管理接口包括：

| domain    |    intent    | 接口说明 |
|-----------|--------------|---------|
| tsk_oauth | get_bind_state | 查询技能的账号绑定状态 |

### get_bind_state
DMSDK查询音箱的账号绑定状态，对于音乐技能会返回当前授权类型：使用微信授权、使用QQ授权、使用QQ音乐授权。

#### request

+ 请求数据示例
```json
{
    "operType": "get_bind_state",
    "skillId": "caabf231-e655-11e7-8130-68cc6ea8c1f8"
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 | 必填 |
|------|-----|----------|----|
| `operType` | 操作类型，值同`payload.intent`，固定为`get_bind_state` | `string` | YES |
| `skillId` | 技能ID，QQ音乐技能填：`caabf231-e655-11e7-8130-68cc6ea8c1f8` | `string` | YES |

#### response

```json
{
    "error": {
        "code": 0,
        "msg": ""
    },
    "accountBaseInfo": {
        "acctId": "1234567890123456",
        "acctType": "QQMusicOpenId",
        "appId": "13214567"
    }
}
```

+ 参数说明

| 参数 | 说明 | 参数类型 |
|------|-----|----------|
| `error` | 业务错误信息 | `object` |
| `error.code` | 业务错误码，请参照[说明](#业务错误码) | `int` |
| `error.msg` | 业务错误信息（Debug） | `string` |
| `accountBaseInfo` | 音箱绑定的账号信息 | `object` |
| `accountBaseInfo.acctType` | 音箱绑定的账号类型，可选值有：`QQOpenId`，`WechatOpenId`，`QQMusicOpenId` | `string` |
| `accountBaseInfo.appId` | 音箱绑定的帐号对应的应用ID | `string` |
| `accountBaseInfo.acctId` | 音箱绑定的帐号唯一ID（一般是OpenId） | `string` |

> 注意：账号类型`QQOpenId`/`WechatOpenId`将逐步替换为`QQMusicOpenId`

#### 如何使用？
1. 查到绑定状态是否说明授权成功？

> 授权的有效性与有效期、权限、用户的变更等相关，查到授权关系仅仅代表用户授权过，授权有效性需要在具体业务场景下使用才能校验是否有效。

2. 如何用来判断当前用户是否已经使用QQ音乐APP授权过？

> 可通过这些组合条件判断：`error.code == 0 && accountBaseInfo.acctType == “QQMusicOpenId”`。

3. 为什么我没用QQ/微信/QQ音乐授权过，却能够查出授权关系？

> 对于已经申请了QQ互联/微信打通的老客户，若用户发起音乐请求会默认进行隐式授权，因此调用该接口查出的`error.code == 0`。

### 业务错误码
业务错误码指的是`error.code`。若通过HTTP方式请求，该字段在`strJsonBlob`解析后json中；若通过DMSDK请求，iOS SDK该字段在回调的第3个`NSDictionary`类型的参数中，Android SDK该字段在TVSCallback<String>的onSuccess中的第1个`String`参数中。

| 错误码 | 描述 |
| ------ | --- |
| `0`    | 成功 |
| `-1`   | 失败 |
| `-2`   | 频率限制 |
| `-101` | 请求端账号信息校验不通过 |
| `-102` | 请求数据不合法 |

### 接口错误码
接口错误码可以作为判断参考。在通过HTTP方式请求，在HTTP Response的数据`header.retCode`字段；若通过DMSDK请求，iOS SDK该字段在回调的第2个`NSInteger`类型的参数中，Android SDK该字段在TVSCallback<String>的onError中的`code`参数中（`0`的时候不会给出）。

| 错误码 | 描述 |
| ------ | --- |
| `0`    | 成功 |
| `3`    | 参数校验失败 |
| `9`    | 登录态失效（校验登录态失败），需要终端重新刷新票据 |
