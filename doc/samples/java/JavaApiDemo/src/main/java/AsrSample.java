import java.io.File;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.HashMap;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import bean.AIRequest;
import bean.ReqHeader;
import bean.asr.AsrReqPayload;
import tools.Base64Util;
import tools.HttpUtil;
import tools.SignatureTool;

public class AsrSample {
	static String url = "https://aiwx.html5.qq.com/api/asr";

	static void request() throws Exception {
		// 封装请求格式。
		AIRequest req = new AIRequest();
		ReqHeader header = new ReqHeader();
		// 设备序列号
		header.device.serial_num = "abcedfg";
		header.qua = "QV=3&VE=GA&VN=1.0.0.1000&PP=com.tencent.ai.tvs&CHID=10020";
		// 对于通过云端调用的，需要将终端的ip地址填进去。
//		header.ip = "1.2.3.4";

		// 如果勾选了需要LBS信息的技能，如导航，终端LBS是必填的。
//		header.lbs = new LBSInfo();
//		header.lbs.latitude = 3.0;
//		header.lbs.longitude = 3.0;

		req.header = header;

		AsrReqPayload payload = new AsrReqPayload();
		payload.voice_meta.compress = "MP3";
		boolean isFinish = false;
		String sessionId = "";
		int index = 0;
			
		FileInputStream fileInput = new FileInputStream(new File("nihao.mp3"));
		int segSize = 2048;
		byte[] buffer = new byte[segSize];
		String result = "";
		while (!isFinish) {
			System.out.println("索引："+index);
			payload.session_id = sessionId;
			payload.index = index;
			int len= fileInput.read(buffer);
			
			if(len<segSize ){
				isFinish = true;
				payload.voice_finished = true;
			}
			if(len >0) {
				byte[] bufferCopy = Arrays.copyOf(buffer, len);
				String data = Base64Util.encode(bufferCopy);
				payload.voice_base64 = data;
			}
			
			
			

			
			
			req.payload = payload;
			
			Gson gson = new Gson();
			String body = gson.toJson(req);

			System.out.println(body);

			String authorization = SignatureTool.getAuthorization(Common.appkey, Common.accessToken, body);
			System.out.println("authorization:" + authorization);
			String contentType = SignatureTool.getContentType();
			// 添加头部
			HashMap<String, String> customHeaders = new HashMap<String, String>();
			customHeaders.put("Authorization", authorization);
			customHeaders.put("Content-Type", contentType);
			// 发送请求
			String response = HttpUtil.sendPost(url, body, customHeaders);
			// 回包数据
			System.out.println(response);

			JsonObject obj = new JsonParser().parse(response).getAsJsonObject();
			
			isFinish = obj.get("payload").getAsJsonObject().get("final_result").getAsBoolean();
			result = obj.get("payload").getAsJsonObject().get("result").getAsString();
			sessionId = obj.get("header").getAsJsonObject().get("session").getAsJsonObject().get("session_id").getAsString();
			index+=len;
			System.out.println("result：" + result+", isFinish:"+isFinish);
			Thread.sleep(200);

		}
		fileInput.close();
		
		System.out.println("最终结果"+result);
	}

	public static void main(String[] args) throws Exception {
		request();

	}

}
