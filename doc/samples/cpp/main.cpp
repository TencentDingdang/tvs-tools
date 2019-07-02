#include <iostream>
#include "Base64.h"
#include <string>
#include "json/json.h"
#include "hmac.h"
#include "sha256.h"

#include <curl/curl.h>
//#include <curl/types.h>
#include <curl/easy.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "util/HttpUtil.h"
#include <fstream>

using namespace std;
// 应用appkey
string appkey = "xxx";
// 应用accessToken
string accessToken = "xxx";

// 设备序列号
string serial_num = "test_serial";
string qua = "QV=3&VE=GA&VN=1.0.1000&PP=com.tencent.ai.tvs&CHID=10020";
double longitude = 132.56481;
double latitude = 22.36549;
string ip = "9.89.3.3";
/**
 * 加载文件到string
 * @param fullFileName
 * @return
 */
string load2str(const string &fullFileName) {
    ifstream ifs(fullFileName.c_str());

    return string(istreambuf_iterator<char>(ifs), istreambuf_iterator<char>());
}
/**
 * 保存数据到文件
 * @param fullFileName
 * @param fileData
 */
void save2file(const string &fullFileName, const string &fileData) {
    ofstream ofs((fullFileName).c_str());
    ofs << fileData;
    ofs.close();
}

/**
 * richanswerV2接口示例
 */
void runRichanswer() {


    Json::Value root;
    Json::FastWriter writer;
    root["header"]["device"]["serial_num"] = serial_num;
    root["header"]["qua"] = qua;
    // 某些技能需要定位信息
//    root["header"]["lbs"]["longitude"] = longitude;
//    root["header"]["lbs"]["latitude"] = latitude;
    // 云端调用需要填写设备外网ip，设备调用不要填。
//    root["header"]["ip"] =ip;

    root["payload"]["query"] = "北京天气怎么样";

    string postBody = writer.write(root);
    int status;
    string response;
    // 发送请求到云端
    sendPostReq(appkey, accessToken, "https://aiwx.html5.qq.com/api/v1/richanswerV2", postBody, status, response);
    cout << "http status:" << status
         << "\n|response body:\n" << response << endl;

}
/**
 * tts接口示例
 *
 */
void runTTS() {
    // 构造请求参数
    Json::Value root;
    Json::FastWriter writer;
    Json::Reader reader;
    root["header"]["device"]["serial_num"] = serial_num;
    root["header"]["qua"] = qua;
    // 某些技能需要定位信息
//    root["header"]["lbs"]["longitude"] = longitude;
//    root["header"]["lbs"]["latitude"] = latitude;
    // 云端调用需要填写设备外网ip，设备调用不要填。
//    root["header"]["ip"] =ip;

    root["payload"]["content"]["text"] = "你好，今天天气怎么样啊";
    root["payload"]["speech_meta"]["compress"] = "MP3";
    root["payload"]["speech_meta"]["person"] = "WY";
    // 流式请求方式
    root["payload"]["single_request"] = false;


    bool isFinish = false;
    string audioData;
    string session_id = "";
    int index = 0;
    //
    while (!isFinish) {
        root["payload"]["index"] = index;
        root["payload"]["session_id"] = session_id;
        cout << "index:" << index << ", session_id" << session_id << endl;

        string postBody = writer.write(root);
        int status;

        string response;
        // 发送请求到云端
        sendPostReq(appkey, accessToken, "https://aiwx.html5.qq.com/api/tts", postBody, status, response);

        cout << "http status:" << status
             << "\n|response body:\n" << response.size() << endl;
        if (status == 200) {
            Json::Value root;
            if (reader.parse(response, root)) {
                session_id = root["header"]["session"]["session_id"].asString();
                string audioBase64 = root["payload"]["speech_base64"].asString();
                audioData += base64_decode(audioBase64);
                isFinish = root["payload"]["speech_finished"].asBool();
                if (isFinish) {
                    save2file("tts.mp3", audioData);
                }
                index++;

            }
        } else {
            cout << " error happened " << endl;
            break;
        }
    }


}
/**
 * asr接口示例
 * 本示例仅适用串行方式请求。效率不高。
 * 实际接入请使用并行发包的方式
 */
void runAsr() {

    // 构造请求参数
    Json::Value root;
    Json::FastWriter writer;
    Json::Reader reader;
    root["header"]["device"]["serial_num"] = serial_num;
    root["header"]["qua"] = qua;
    // 某些技能需要定位信息
//    root["header"]["lbs"]["longitude"] = longitude;
//    root["header"]["lbs"]["latitude"] = latitude;
    // 云端调用需要填写设备外网ip，设备调用不要填。
//    root["header"]["ip"] =ip;
    root["payload"]["voice_meta"]["compress"] = "MP3";
    root["payload"]["voice_meta"]["sample_rate"] = "16K";
    root["payload"]["voice_meta"]["channel"] = 1;
    root["payload"]["open_vad"] = true;

    // 流式请求方式
    root["payload"]["single_request"] = false;


    bool isFinish = false;
    string audioData = load2str("resources/nihao.mp3");
    // 每次读2000字节
    int segSize = 2000;

    string session_id = "";
    int index = 0;

    //
    while (!isFinish) {
        usleep(100000);
        int oldIndex = index;
        root["payload"]["index"] = index;
        root["payload"]["session_id"] = session_id;
        string audioBase64 = "";
        if (index < audioData.size()) {
            if ((audioData.size() - index) > segSize) {
                // 中间包
                root["payload"]["voice_finished"] = false;
                string sendAudio = audioData.substr(index, segSize);
                audioBase64 = base64_encode((unsigned char const *) sendAudio.c_str(), sendAudio.size());
                index += segSize;
            } else {
                // 文件最后一包
                root["payload"]["voice_finished"] = true;
                string sendAudio = audioData.substr(index, audioData.size() - index);
                audioBase64 = base64_encode((unsigned char const *) sendAudio.c_str(), sendAudio.size());
                index += audioData.size() - segSize;

            }

        } else {
            root["payload"]["voice_finished"] = true;

        }

        root["payload"]["voice_base64"] = audioBase64;

        cout << "index:" << oldIndex << ", session_id" << session_id << ", voice_finished:" << isFinish << endl;

        string postBody = writer.write(root);
        int status;

        string response;
        // 发送请求到云端
        sendPostReq(appkey, accessToken, "https://aiwx.html5.qq.com/api/asr", postBody, status, response);

        cout << "http status:" << status
             << "\n|response body:\n" << response.size() << endl;
        if (status == 200) {

            Json::Value root;
            cout << " response:" << response << endl;
            if (reader.parse(response, root)) {
                session_id = root["header"]["session"]["session_id"].asString();
                isFinish = root["payload"]["final_result"].asBool();
                int ret = root["payload"]["ret"].asInt();

                if (ret != 0) {
                    cout << " error happened" << endl;
                    break;
                }
                if (isFinish) {
                    save2file("tts.mp3", audioData);
                }

            }
        } else {
            cout << " error happened " << endl;
            break;
        }
    }

}

int main(int argc, char *argv[]) {
    while (1) {
        cout << "select sample" << endl;
        cout << "1: richanswerV2" << endl;
        cout << "2: tts" << endl;
        cout << "3: asr" << endl;
        cout << "4: exit" << endl;
        cout << "input:" << endl;

        int i;
        cin >> i;

        if (i == 1) {
            runRichanswer();
        } else if (i == 2) {
            runTTS();
        } else if (i == 3) {
            runAsr();
        } else if (i == 4) {
            break;
        }
        cout << "\n" << endl;

    }


//    cout << generateAuthorization("aa", "bb") << endl;
    return 0;
}