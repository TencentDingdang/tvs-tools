//
// Created by kangrong on 2019/7/2.
//

#include "HttpUtil.h"
#include <time.h>
#include <stdio.h>
#include <iostream>
#include "Base64.h"
#include <string>
#include "json/json.h"
#include "hmac.h"
#include "sha256.h"
#include <stdlib.h>
#include <curl/curl.h>
//#include <curl/types.h>
#include <curl/easy.h>
#include <sstream>

string tm2str(const struct tm &stTm, const string &sFormat) {
    char sTimeString[255] = "\0";

    strftime(sTimeString, sizeof(sTimeString), sFormat.c_str(), &stTm);

    return string(sTimeString);
}


string generateAuthorization(const string &appkey, const string &accessToken, const string& body) {
    time_t t = time(NULL);
    struct tm tt;
    localtime_r(&t, &tt);
    string timeStr = tm2str(tt, "%Y%m%dT%H%M%SZ");
    string signature = hmac<SHA256>(body+timeStr, accessToken);
    //TVS-HMAC-SHA256-BASIC CredentialKey = 39ba87a1-2we3-4345-8d26-e632646e54b1, Datetime=20170720T193559Z, Signature=d8612ab1ff0301e1016d817c02350a2b76ea62e0
    ostringstream oss;
    oss<<"TVS-HMAC-SHA256-BASIC CredentialKey = "
        <<appkey<<", Datetime="<<timeStr<<", Signature="<<signature;

    return oss.str();

}

struct MemoryStruct {
    char *memory;
    size_t size;

    MemoryStruct() {
        memory = (char *) malloc(1);
        size = 0;
    }

    ~MemoryStruct() {
        free(memory);
        memory = NULL;
        size = 0;
    }
};

size_t WriteMemoryCallback(void *ptr, size_t size, size_t nmemb, void *data) {
    size_t realsize = size * nmemb;
    struct MemoryStruct *mem = (struct MemoryStruct *) data;

    mem->memory = (char *) realloc(mem->memory, mem->size + realsize + 1);
    if (mem->memory) {
        memcpy(&(mem->memory[mem->size]), ptr, realsize);
        mem->size += realsize;
        mem->memory[mem->size] = 0;
    }
    return realsize;
}

int sendPostReq(const string &appkey,
                const string &accessToken,
                const string &url,
                const string &body,
                int &status,
                string &response) {

    string authorizationHeader = generateAuthorization(appkey, accessToken, body);
    cout<< authorizationHeader<<endl;
    CURLcode res = curl_global_init(CURL_GLOBAL_ALL);
    if (CURLE_OK != res) {
        cout << "curl init failed" << endl;
        return 1;
    }

    CURL *pCurl;
    pCurl = curl_easy_init();

    if (NULL == pCurl) {
        cout << "Init CURL failed..." << endl;
        return -1;
    }

//    string url = "https://aiwx.html5.qq.com/api/v1/richanswer";
    string filename = "result.json";

    curl_slist *pList = NULL;
    pList = curl_slist_append(pList, "Content-Type: application/json; charset=UTF-8");
    pList = curl_slist_append(pList, ("Authorization: "+ authorizationHeader).c_str());

    // 设置头部
    curl_easy_setopt(pCurl, CURLOPT_HTTPHEADER, pList);
    // 设置url
    curl_easy_setopt(pCurl, CURLOPT_URL, url.c_str());

    curl_easy_setopt(pCurl, CURLOPT_HEADER, 0L);  //启用时会将头文件的信息作为数据流输
    curl_easy_setopt(pCurl, CURLOPT_FOLLOWLOCATION, 1L);//允许重定向
    curl_easy_setopt(pCurl, CURLOPT_NOSIGNAL, 1L);

    //将返回结果通过回调函数写到自定义的对象中
    MemoryStruct oDataChunk;
    curl_easy_setopt(pCurl, CURLOPT_WRITEDATA, &oDataChunk);
    curl_easy_setopt(pCurl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);

    //curl_easy_setopt(pCurl, CURLOPT_VERBOSE, 1L); //启用时会汇报所有的信息
    // 设置使用POST方式
    curl_easy_setopt(pCurl, CURLOPT_POST, 1L);
    curl_easy_setopt(pCurl, CURLOPT_POSTFIELDS, body.c_str());
    curl_easy_setopt(pCurl, CURLOPT_POSTFIELDSIZE, body.size());


    res = curl_easy_perform(pCurl);

    long res_code = 0;
    res = curl_easy_getinfo(pCurl, CURLINFO_RESPONSE_CODE, &res_code);

    if (res == CURLE_OK) {
        status  = res_code;
        response = string(oDataChunk.memory, oDataChunk.size);
//        FILE *fTmpMem = (FILE *) oDataChunk.memory;
//        if (!fTmpMem) {
//
//        }
//        FILE *fp = fopen(filename.c_str(), "wb");
//        if (!fp) {
//            cout << "open file failed";
//            return -1;
//        }
//
//        fwrite(fTmpMem, 1, oDataChunk.size, fp);
//        fclose(fp);
//        return ;
    }

    curl_slist_free_all(pList);
    curl_easy_cleanup(pCurl);
    curl_global_cleanup();
    return 0;
}


