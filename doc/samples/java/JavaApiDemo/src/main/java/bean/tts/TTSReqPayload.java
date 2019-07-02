package bean.tts;

import bean.ReqPayload;

/**
 * 
 * 
        "speech_meta": {
            "compress": "MP3",
            "person": "LIBAI",
            "volume": 50,
            "speed": 50,
            "pitch": 50
        },
        "session_id": "{{STRING}}",
        "index": 0,
        "single_request": false,
        "content": {
            "text": "{{STRING}}"
        }

 * @author kangrong
 *
 */
public class TTSReqPayload extends ReqPayload {
	public TTSReqPayload(String text) {
		content.text = text;
	}
	public String session_id = "";
	public int index = 0;

	public boolean single_request = false;
	public TTSSpeechMeta speech_meta = new TTSSpeechMeta();
	public TTSPayloadContent content = new TTSPayloadContent();


}
