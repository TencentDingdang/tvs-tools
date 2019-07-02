# Java示例项目说明

Java示例为maven项目

# 使用步骤

## 1. 修改JavaApiDemo\src\main\java\Common.java，填写appkey、accessToken

请在JavaApiDemo\src\main\java\Common.java的代码中修改自己的appkey， accessToken。否则云端会返回403错误。
```
	// 应用appkey
    public static String appkey = "XXX";
    // 应用accessToken
    public static String accessToken = "XXX";

```


## 2. 运行

运行三个示例：
/JavaApiDemo/src/main/java/TTSSample.java：tts示例
/JavaApiDemo/src/main/java/RichAnswerSample.java：richanswer示例
/JavaApiDemo/src/main/java/AsrSample.java：asr示例
