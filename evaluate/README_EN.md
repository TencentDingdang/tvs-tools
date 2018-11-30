# Evaluation Tool Description of Tencent Cloud Dingding  

## 1 Background
Evaluation tools are used to meet the following requirements:：
- Product managers, business from external vendors experience services, including full link experience and basic capabilities (ASR, NLP, TTS) experience.
- Engineers from external vendors evaluated Tencent's capabilities, including batch evaluation of basic capabilities (ASR, NLP, TTS).

## 2 Experience
### 2.1 Full Link Experience
 Please use the official app of Tencent Cloud Dingdang for the full link experience。Mobile phone users can download  "腾讯叮当" on Tencent MyApp or Apple AppStore and   install the app to experience.

 "腾讯叮当" App includes  experience of the full  link of ASR, NLP, Service, and TTS, as well as music, news, and other domains supported by  Tencent Cloud Dingdang.

### 2.2 TTS Experience
To experience TTS, please visit the following address: http://betashow.html5.qq.com/player.html

Note:

- Select the body content on the page to edit the text you want to synthesize.
- Tap the Title "beta" at the top of the page to switch between different speakers.
- Click the play button at the bottom of the page to start playing the synthesized voice.

## 3 Technical evaluation
### 3.1 ASR, NLP, TTS capability evaluation
### 3.1.1 ASRNLU_demo Tool
The app/ASRNLU_demo_xxxx.apk tool supports the Android  environment and provides ASR and NLP batch data evaluation. The WAV and PCM files are received as input, and the test report including ASR text and NLP result.

The usage process is as follows:

- Install ASRNLU_demo.apk.
- Place the entire tsr directory in `/sdcard/tencent/dingdang/res/` directory.
- Place the audio files in `/sdcard/tencent/test/tsr/wav/` directory.
- Run the app and click the "Test" button to start the test.
- After the test is completed, the test report is stored in the `/sdcard/tencent/test/tsr/out/` directory.

### 3.1.2 HTTP API basic capability evaluation script
- `script/richanswerV1.py` script supports access to NLP capability based on HTTP API.

- `script/tts.py` script supports access to TTS capability based on HTTP API.

- `script/asr.py` script supports access to ASR capability based on HTTP API.

     **Note:  requires Python version  3.6.4 and above**

### 3.2 Media format of Tencent Cloud Dingdang
The formats of media data that Tencent Cloud Dingdang will return to the terminal device  are shown in the following table:

* Audio

| Domain | format               | description                              | sample file                              | note                               |
| ------ | -------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------- |
| TTS    | mp3                  | MPEG ADTS, layer III, v2,  64 kbps, 16 kHz, Monaural | [tts_stream2.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/tts_stream2.mp3 "tts_stream2.mp3") |                                    |
| TTS    | wav                  | RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 16000 Hz | [tts_stream1.wav](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/tts_stream1.wav "tts_stream1.wav") |                                    |
| joke   | mp3                  | Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, JntStereo | [joke_demo.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/joke_demo.mp3 "joke_demo.mp3") |                                    |
| sound  | mp3                  | MPEG ADTS, layer III, v2,  64 kbps, 22.05 kHz, JntStereo | [sound_demo.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/sound_demo.mp3 "sound_demo.mp3") |                                    |
| new    | mp3                  | Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, JntStereo | [news_demo2.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/news_demo2.mp3 "news_demo2.mp3") |                                    |
| new    | wav                  | RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 16000 Hz | [news_demo1.wav](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/news_demo1.wav "news_demo1.wav") |                                    |
| fm     | m4a                  | ISO Media, MPEG v4 system, version 2     | [fm_demo.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/fm_demo.m4a "fm_demo.m4a") |                                    |
| fm     | m3u8                 | M3U playlist text                        | [fm_demo.m3u8](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/fm_demo.m3u8 "fm_demo.m3u8") |                                    |
| music  | mp3                  | Audio file with ID3 version 2.3.0, contains: MPEG ADTS, layer III, v1, 128 kbps, 44.1 kHz, JntStereo | [music_demo2.mp3](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo2.mp3 "music_demo2.mp3") |                                    |
| music  | m4a                  | ISO Media, MPEG v4 system, version 2     | [music_piano_demo1.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_piano_demo1.m4a "music_piano_demo1.m4a") | Is there a buzz?                   |
| music  | m4a Fluency Quality  | ISO Media, MPEG v4 system, version 2     | [music_demo3_smooth.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_smooth.m4a "music_demo3_smooth.m4a") | Is there any noise in the prelude? |
| music  | m4a Standard Quality | ISO Media, MPEG v4 system, version 2     | [music_demo3_stardard.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_stardard.m4a "music_demo3_stardard.m4a") |                                    |
| music  | m4a High Quality     | ISO Media, MPEG v4 system, version 2     | [music_demo3_high.m4a](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_high.m4a "music_demo3_high.m4a") |                                    |
| HQ     | flac                 | FLAC audio bitstream data, 16 bit, stereo, 44.1 kHz, 12470158 samples | [music_demo3_pretect.flac](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_demo3_pretect.flac "music_demo3_pretect.flac") |                                    |

* Video (for device with screen)

| Domain | format      | description                          |                                          | note |
| ------ | ----------- | ------------------------------------ | ---------------------------------------- | ---- |
| music  | MV Vidio    | ISO Media, MPEG v4 system, version 1 | [music_mv.mp4](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/music_mv.mp4 "music_mv.mp4") |      |
| baike  | Baike Video | ISO Media, MPEG v4 system, version 1 | [baike_video.mp4](https://github.com/TencentDingdang/tvs-tools/blob/master/evaluate/media/data/baike_video.mp4 "baike_video.mp4") |      |

The vendor needs to first evaluate the capabilities of the media player to ensure that the sample files can be played normally. There should be no such phenomenon as jamming or noise during playback.

If the format is not supported, you need to consider upgrading the decoder of the terminal.