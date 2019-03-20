### HTTP头部
    1. TvsSettings
        * 必选:否
        * 格式: Key1=Value;Key2=Value2;...;KeyN=ValueN
            * 沙箱模式:
                env=sandbox

    2. Q-UA
        * 必选:否
        * 格式: Key1=Value&Key2=Value2&...&KeyN=ValueN
        * 默认Q-UA:
            QV=3&PL=ADR&PR=TVS&VE=GA&VN=1.0.0.0001&PP=com.tencent.ai.tvs&DE=SPEAKER
        * 说明:
            * VN
                终端版本号，必须 >= 1.0.0.0001