
# 总体结构


```json
{
  "skill_vedio":{
      "qqvedio_session_info":{
          "session_id":"session_id",
          "session_data":"session_data"
      }
  }
}
```

| 参数名                        |   类型   | 是否必选 | 描述                                                         |
| ----------------------------- | :------: | :------: | ------------------------------------------------------------ |
| `skill_vedio`                 |         |    否    | 视频技能所需信息                                                     |
| `skill_vedio.qqvedio_session_info`    | `string` |    -     | 腾讯视频session信息，由视频技能下发   |
| `skill_vedio.qqvedio_session_info.session_id`    | `string` |    -     | 腾讯视频session id     |
| `skill_vedio.qqvedio_session_info.session_data`    | `string` |    -     | 腾讯视频session data       |
