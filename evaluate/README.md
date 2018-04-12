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
TTS的效果体验，请访问以下地址：http://betashow.html5.qq.com/player.html

注：
- 选中页面中的正文内容，可对需要合成的文本进行编辑。
- 点击页面顶部的Title“贝塔”，可切换不同发声人。
- 点击页面底部的播放按钮，开始的播放合成后的语音。

## 3 技术评测
### 3.1 ASR、NLP、TTS能力评测
### 3.1.1 ASRNLU_demo工具
app/ASRNLU_demo_xxxx.apk工具支持Android运行环境，提供ASR、NLP批量数据的评测能力。接收wav、pcm批量文件作为输入，执行后输出包含：ASR识别文本、NLP结果数据的测试报告。

使用流程如下：
- 安装ASRNLU_demo.apk，
- 将tsr整个目录放到手机/sdcard/tencent/dingdang/res/目录下。
- 测试音频文件，存放到/sdcard/tencent/test/tsr/wav/目录下。
- 运行App，点击“测试”按钮，开始测试。
- 测试完成后，测试报告存放在/sdcard/tencent/test/tsr/out/目录下。

### 3.1.2 HTTP API基础能力评测脚本
* script/richanswerV1.py脚本支持基于HTTP API访问TVS基础能力NLP的功能
* script/tts.py脚本支持基于HTTP API访问TVS基础能力TTS的功能
* script/asr.py脚本支持基于HTTP API访问TVS基础能力ASR的功能

	*注：Python环境需要使用3.6.4及以上版本*

### 3.2 媒体播放能力评测
腾讯叮当后台返回给终端设备的媒体数据格式，如下表所示：
厂商在接入腾讯叮当之初，需要先对媒体播放器的能力进行评测，保证以下示例文件能正常播放，播放过程中不出现卡顿、杂音等现象。

如果播放格式不支持，需要考虑升级终端的解码器。

| 领域        | 文件类型   |  格式说明  | 文件下载 | 备注 |
| --------    | -----      |  -----     | -----    | ---- |
| TTS数据     |mp3         |   MPEG ADTS, layer III, v2,  64 kbps, 16 kHz, Monaural                                                 |   [tts_stream2.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/tts_stream2.mp3 "tts_stream2.mp3")     |       |
| TTS数据     |wav         |   RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 16000 Hz                          |   [tts_stream1.wav](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/tts_stream1.wav "tts_stream1.wav")     |       |
| 笑话        |mp3         |  Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, JntStereo  |   [joke_demo.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/joke_demo.mp3 "joke_demo.mp3")           |       |
| 声音百科    |mp3         |  MPEG ADTS, layer III, v2,  64 kbps, 22.05 kHz, JntStereo                                              |   [sound_demo.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/sound_demo.mp3 "sound_demo.mp3")        |       |
| 新闻        |mp3         | Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, JntStereo   |   [news_demo2.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/news_demo2.mp3 "news_demo2.mp3")        |       |
| 新闻        |wav         | RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 16000 Hz                            |   [news_demo1.wav](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/news_demo1.wav "news_demo1.wav")        |       |
| FM          |m4a         | ISO Media, MPEG v4 system, version 2                                                                   |   [fm_demo.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/fm_demo.m4a "fm_demo.m4a")     | |
| 音乐        |mp3标准音质 | Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 128 kbps, 44.1 kHz, JntStereo   |   [music_demo2.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo2.mp3 "music_demo2.mp3")     |       |
| 音乐        |m4a钢琴曲   | ISO Media, MPEG v4 system, version 2                                                                   |   [music_piano_demo1.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_piano_demo1.m4a "music_piano_demo1.m4a")     |是否有吱吱声|
| 音乐        |m4a流畅     | ISO Media, MPEG v4 system, version 2                                                                   |   [music_demo3_smooth.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_smooth.m4a "music_demo3_smooth.m4a")     |前奏是否有杂音|
| 音乐        |m4a标准     | ISO Media, MPEG v4 system, version 2                                                                   |   [music_demo3_stardard.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_stardard.m4a "music_demo3_stardard.m4a")     |       |
| 音乐        |m4a高质     | ISO Media, MPEG v4 system, version 2                                                                   |   [music_demo3_high.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_high.m4a "music_demo3_high.m4a")                 |       |
| 音乐        |flac无损    | FLAC audio bitstream data, 16 bit, stereo, 44.1 kHz, 12470158 samples                                  |   [music_demo3_pretect.flac](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_pretect.flac "music_demo3_pretect.flac")     |       |
