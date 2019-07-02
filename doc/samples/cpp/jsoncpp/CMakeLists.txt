CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

PROJECT(jsoncpp)

include_directories(include)
SET(jsoncpp_sources
                src/json_tool.h
                src/json_reader.cpp
                src/json_valueiterator.inl
                src/json_value.cpp
                src/json_writer.cpp
                src/version.h.in)


ADD_LIBRARY(jsoncpp ${PUBLIC_HEADERS} ${jsoncpp_sources})
