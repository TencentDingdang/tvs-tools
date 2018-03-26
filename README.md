# TVS评测工具说明

## 1 背景
TVS评测工具用于满足以下几种需求：
- 外部厂商的产品、商务同学体验业务，包括完整链路体验及基础能力（ASR、NLP、TTS）体验。
- 外部厂商的技术同学评测TVS能力，包括基础能力（ASR、NLP、TTS）的批量评测。

## 2 产品、商务同学体验
### 2.1 完整链路体验
完整链路体验，请使用腾讯叮当官方App。手机用户在应用宝、AppStore上搜索“腾讯叮当”，下载安装App后即可体验。
腾讯叮当App包括ASR、NLP、Srv、TTS整个链路的完整体验，也覆盖音乐、新闻等当前TVS平台支持的所有领域。
### 2.2 TTS体验
TTS的效果体验，请访问以下地址：http://betashow.html5.qq.com/player.html?m=6

注：
- 选中页面中的正文内容，可对需要合成的文本进行编辑。
- 点击页面顶部的Title“贝塔”，可切换不同发声人。
- 点击页面底部的播放按钮，开始的播放合成后的语音。

## 3 技术评测
### 3.1 ASR、NLP能力评测
### 3.1.1 ASRNLU_demo工具
app/ASRNLU_demo_xxxx.apk工具支持Android运行环境，提供ASR、NLP批量数据的评测能力。接收wav、pcm批量文件作为输入，执行后输出包含：ASR识别文本、NLP结果数据的测试报告。

使用流程如下：
- 安装ASRNLU_demo.apk，
- 将tsr整个目录放到手机/sdcard/tencent/dingdang/res/目录下。
- 测试音频文件，存放到/sdcard/tencent/test/tsr/wav/目录下。
- 运行App，点击“测试”按钮，开始测试。
- 测试完成后，测试报告存放在/sdcard/tencent/test/tsr/out/目录下。

### 3.1.2 HTTP API基础能力评测脚本
script/tvs_hmac_sha256_basic.py脚本支持基于HTTP API访问TVS基础能力（ASR、NLP、TTS）接口的功能，当前支持语义请求接口，后续会添加ASR、TTS的对应请求示例。

注：Python环境需要使用3.6.4及以上版本。