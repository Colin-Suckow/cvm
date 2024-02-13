cmake_minimum_required(VERSION 3.15)

project(CVM)
add_executable(CVM src/cvm.cpp)

set_property(TARGET CVM PROPERTY CXX_STANDARD 20)

add_subdirectory(deps/fmt)

target_link_libraries(CVM fmt::fmt)
