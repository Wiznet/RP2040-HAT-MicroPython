#CMake minimum required version
cmake_minimum_required(VERSION 3.12)
set(PROJECT_NAME RP2040-HAT-MicroPython)
PROJECT(${PROJECT_NAME} LANGUAGE Micropython VERSION 1.7)
MESSAGE(ProJect Name : ${CMAKE_PROJECT_NAME})
# Pull in MicroPython (must be confirm before prokject begin)
if(NOT DEFINED MICROPYTHON)
    set(MICROPYTHON_PATH ${CMAKE_SOURCE_DIR}/libraries)
    message(STATUS "MICROPYTHON_PATH = ${MICROPYTHON_PATH}")
endif()


include(rp2_net_patch.cmake)


add_compile_options(
        -Wall
        -Wno-format          # int != int32_t as far as the compiler is concerned because gcc has int32_t as long int
        -Wno-unused-function # we have some for the docs that aren't called
        -Wno-maybe-uninitialized
        )