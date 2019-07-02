//
// Created by kangrong on 2019/7/2.
//

#ifndef PROJECT_HTTPUTIL_H
#define PROJECT_HTTPUTIL_H

#include <iostream>
#include <string>
using namespace std;
/**
 * 发送请求到云端
 * @param appkey 应用appkey
 * @param accessToken 应用accessToken
 * @param url url
 * @param body post body
 * @param status http状态码
 * @param response 返回数据
 * @return
 */
int sendPostReq(const string &appkey,
                const string &accessToken,
                const string &url,
                const string &body,
                int &status,
                string &response);

#endif //PROJECT_HTTPUTIL_H
