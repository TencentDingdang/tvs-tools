package bean.richanswer;

import bean.ReqPayload;

public class RichAnswerReqPayload extends ReqPayload {
	
	public RichAnswerReqPayload(String query) {
		this.query = query;
	}
	String query;

}
