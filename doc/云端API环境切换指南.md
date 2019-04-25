# 设置网络环境

终端设备访问不同的云端API接入地址，即可切换到云小微不同的接入环境。

## 基础API

    正式环境地址：https://aiwx.html5.qq.com/api/
    体验环境地址：https://aiwx..html5.qq.com/apiexp/
    测试环境地址：https://aiwx.sparta.html5.qq.com/api

## TVS API

    正式环境地址：https://tvs.html5.qq.com/
    体验环境地址：https://tvsexp.html5.qq.com/
    测试环境地址：https://tvstest.html5.qq.com/

# 开启/关闭沙箱环境

终端设备通过指定QUA字段的env值，可在语义的沙箱和线上环境间进行切换。

    沙箱环境：QV=3&VE=GA&VN=1.0.1.1000&PP=com.tencent.ai.tvs&env=SANDBOX
    线上环境：QV=3&VE=GA&VN=1.0.1.1000&PP=com.tencent.ai.tvs
