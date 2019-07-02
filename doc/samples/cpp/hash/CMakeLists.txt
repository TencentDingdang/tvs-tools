
cmake_minimum_required(VERSION 2.8)
project(hash)

SET(SOURCE_FILES
        src/sha256.cpp
        )
add_library(hash ${SOURCE_FILES})
