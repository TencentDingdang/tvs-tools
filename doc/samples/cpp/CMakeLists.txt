cmake_minimum_required(VERSION 2.8)
project(BApiSample)

# 设置输出目录为bin
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin/)
# 设置输出目录为bin
SET(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin/)
OPTION(BUILD_STATIC_LIBS "Build jsoncpp_lib static library." ON)

#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/cmakemedia/)
#set(CMAKE_BUILD_FILES_DIRECTORY ${PROJECT_SOURCE_DIR}/cmakemedia/)
#set(CMAKE_BUILD_DIRECTORY ${PROJECT_SOURCE_DIR}/cmakemedia/)

# 设置链接目录
link_directories(${PROJECT_SOURCE_DIR}/bin/)

include_directories(hash/include)
include_directories(jsoncpp/include)
include_directories(curl-7.65.1/include)
include_directories(util)
include_directories(./)

SET(SOURCE_FILES
        main.cpp
        Base64.cpp
        Base64.h
        util/HttpUtil.cpp
        util/HttpUtil.h
        )

add_subdirectory(hash)
add_subdirectory(jsoncpp)

#add_subdirectory(curl-7.65.1)
add_executable(BApiSample ${SOURCE_FILES})
target_link_libraries(BApiSample jsoncpp hash curl)
