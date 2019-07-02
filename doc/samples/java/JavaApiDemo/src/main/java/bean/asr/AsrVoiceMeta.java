package bean.asr;

/**
        "voice_meta": {
            "compress": "PCM",
            "sample_rate": "8K",
            "channel": 1,
            "language": "{{STRING}}",
            "model":10
            "offset":0
        },
        "open_vad": true,
        "session_id": "{{STRING}}",
        "index": 0,
        "voice_finished": false,
        "voice_base64": "{{STRING}}"
 * @author kangrong
 *
 */
public class AsrVoiceMeta {
	public String compress = "PCM";
	public String sample_rate = "16K";
	public int channel = 1;

}
