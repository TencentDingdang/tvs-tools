import java.util.HashMap;
import com.google.gson.Gson;

import bean.AIRequest;
import bean.ReqHeader;
import bean.richanswer.RichAnswerReqPayload;
import tools.HttpUtil;
import tools.SignatureTool;

 

public class RichAnswerSample {
	
    static String url = "https://aiwx.html5.qq.com/api/v1/richanswerV2";
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
		req.payload = new RichAnswerReqPayload("你好");
        Gson gson = new Gson();
        String body = gson.toJson(req);
        
        System.out.println(body);
        
        String authorization = SignatureTool.getAuthorization(Common.appkey, Common.accessToken, body);
        System.out.println("authorization:"+authorization);
        String contentType = SignatureTool.getContentType();
        // 添加头部
        HashMap<String, String> customHeaders= new HashMap<String, String>();
        customHeaders.put("Authorization", authorization);
        customHeaders.put("Content-Type", contentType);
        // 发送请求
        String response = HttpUtil.sendPost(url, body, customHeaders);
        // 回包数据
        System.out.println(response);

			
	}
	public static void main(String[] args) throws Exception {
		request();
        
        	
	}

}
