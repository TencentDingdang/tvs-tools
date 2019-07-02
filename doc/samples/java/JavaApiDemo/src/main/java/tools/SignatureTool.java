package tools;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

public class SignatureTool {

	public static String getAuthorization(String appkey, String accessToken, String body) throws Exception {
		// 第一步：取时间戳
		Date date = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd'T'HHmmss'Z'");
		// 设置时区为0区
		sdf.setTimeZone(TimeZone.getTimeZone("Etc/GMT"));
		String dateStr = sdf.format(date);
		System.out.println("签名时间戳：" + dateStr);

		// 第二步：拼接签名串

		String signContent = body + dateStr;
		// 第三步：计算签名信息

		String signature = HMacSha256.HMACSHA256(signContent, accessToken);

		// 第四部：拼接Authorization串

		String authorization = "TVS-HMAC-SHA256-BASIC CredentialKey=" + appkey + ", Datetime=" + dateStr
				+ ", Signature=" + signature;

		return authorization;
	}

	public static String getContentType() {
		return "Content-Type: application/json; charset=UTF-8";
	}
}
