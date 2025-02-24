# CMakeList.txt: OpenGL 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#

# 将源代码添加到此项目的可执行文件。
add_executable (OpenGL "OpenGL.cpp" "OpenGL.h")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET OpenGL PROPERTY CXX_STANDARD 20)
endif()

target_include_directories(OpenGL PRIVATE
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/Dependencies/GLFW/include  # GLFW 的头文件目录
)

if(WIN32)
    set(GLFW_LIB64_DIR ${CMAKE_SOURCE_DIR}/Dependencies/GLFW/WIN64/lib-vc2022)
    set(GLFW_LIB32_DIR ${CMAKE_SOURCE_DIR}/Dependencies/GLFW/WIN64/lib-vc2022)
    if (CMAKE_SIZEOF_VOID_P EQUAL 8)  # 64 位
        set(GLFW_LIBRARY ${GLFW_LIB64_DIR}/glfw3.lib)
    else()  # 32 位
        set(GLFW_LIBRARY ${GLFW_LIB32_DIR}/glfw3.lib)
    endif()
    target_link_libraries(OpenGL PRIVATE ${GLFW_LIBRARY} opengl32)
else()
    set(OpenGL_GL_PREFERENCE GLVND)
    find_package(glfw3 REQUIRED)
    find_package(OpenGL REQUIRED)
    target_link_libraries(OpenGL PRIVATE glfw OpenGL::OpenGL)
endif()

# TODO: 如有需要，请添加测试并安装目标。
