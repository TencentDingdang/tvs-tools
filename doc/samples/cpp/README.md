# CPP示例依赖

cmake
libcurl(需要支持https)

# 使用步骤

## 1. 修改main.cpp，填写appkey、accessToken

请在main.cpp的代码中修改自己的appkey， accessToken。否则云端会返回403错误。
```
// 应用appkey
string appkey = "xxx";
// 应用accessToken
string accessToken = "xxx";

```

## 2. 编译

```
# 编译
cmake .

make

```

## 运行


```
./main
```