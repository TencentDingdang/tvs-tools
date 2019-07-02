package tools;
import java.io.IOException;
import java.util.HashMap;
import org.apache.http.Consts;
import org.apache.http.HttpEntity;
import org.apache.http.ParseException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class HttpUtil {
 
    private static final CloseableHttpClient httpClient = HttpClients.createDefault();
 
//    /**
//     * 发送HttpGet请求
//     * @param url
//     * @return
//     */
//    public static String sendGet(String url) {
// 
//        HttpGet httpget = new HttpGet(url);
//        CloseableHttpResponse response = null;
//        try {
//            response = httpclient.execute(httpget);
//        } catch (IOException e1) {
//            e1.printStackTrace();
//        }
//        String result = null;
//        try {
//            HttpEntity entity = response.getEntity();
//            if (entity != null) {
//                result = EntityUtils.toString(entity);
//            }
//        } catch (ParseException | IOException e) {
//            e.printStackTrace();
//        } finally {
//            try {
//                response.close();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//        }
//        return result;
//    }

    
    /**
     * 发送HttpPost请求
     * @param url 请求链接
     * @param body post 数据
     * @param headers 自定义头
     * @return
     */
    public static String sendPost(String url, String body, HashMap<String, String> headers) {
        StringEntity entity = new StringEntity(body, Consts.UTF_8);
        HttpPost httpPost = new HttpPost(url);
        
        for(String key:headers.keySet()) {
        	httpPost.addHeader(key, headers.get(key));
        }
        httpPost.setEntity(entity);
        CloseableHttpResponse response = null;
        try {
            response = httpClient.execute(httpPost);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(response.getStatusLine().getStatusCode());
        HttpEntity entity1 = response.getEntity();
        String result = null;
        try {
            result = EntityUtils.toString(entity1);
        } catch (ParseException | IOException e) {
            e.printStackTrace();
        }
        return result;
    }

   
 
}