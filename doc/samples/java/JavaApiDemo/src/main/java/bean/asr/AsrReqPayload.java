package bean.asr;

import bean.ReqPayload;

/**
 * 
 * 
        "open_vad": true,
        "session_id": "{{STRING}}",
        "index": 0,
        "voice_finished": false,
        "voice_base64": "{{STRING}}"


 * @author kangrong
 *
 */
public class AsrReqPayload extends ReqPayload {
	
	public String session_id = "";
	public int index = 0;
	public boolean open_vad = true;
	public boolean voice_finished = false;
	public String voice_base64 = "";

	public AsrVoiceMeta voice_meta = new AsrVoiceMeta();
	

}
