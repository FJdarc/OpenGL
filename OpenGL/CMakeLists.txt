# CMakeList.txt: OpenGL 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#

# 将源代码添加到此项目的可执行文件。
add_executable (OpenGL "OpenGL.cpp" "OpenGL.h")

target_include_directories(OpenGL PRIVATE "${CMAKE_SOURCE_DIR}/vendor/glew/include")

if(WIN32)
    target_link_libraries(OpenGL PRIVATE glew glfw opengl32)
else()
    find_package(OpenGL REQUIRED)
    target_link_libraries(OpenGL PRIVATE glew glfw OpenGL::OpenGL)
endif()

# TODO: 如有需要，请添加测试并安装目标。
