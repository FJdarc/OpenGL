# CMakeList.txt: 顶层 CMake 项目文件，在此处执行全局配置
# 并包含子项目。
#
cmake_minimum_required (VERSION 3.12)

project ("OpenGL")

add_compile_definitions(GLEW_STATIC)

# 包含子项目。
add_subdirectory("OpenGL")
add_subdirectory("vendor/glfw")
add_subdirectory("vendor/glew/build/cmake")