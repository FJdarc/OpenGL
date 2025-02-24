@echo off
setlocal enabledelayedexpansion

:: 初始化默认值
set BUILD_TYPE=d
set PROGRAM_NAME=
set SCRIPT_NAME=%~n0

:: 参数解析逻辑
if "%~1"=="" goto :validate_args
if /i "%~1"=="d" (set BUILD_TYPE=d & shift)
if /i "%~1"=="r" (set BUILD_TYPE=r & shift)
if "%~1"=="" goto :validate_args

:: 处理程序名参数
if "%PROGRAM_NAME%"=="" (
    set "PROGRAM_NAME=%~1"
    shift
)

:: 检查多余参数
:check_extra_args
if not "%~1"=="" (
    echo ERROR: 多余的参数 [%1]
    echo 用法: %SCRIPT_NAME% [d|r] [程序名]
    exit /b 1
)

:validate_args
if "%BUILD_TYPE%" neq "d" if "%BUILD_TYPE%" neq "r" (
    echo ERROR: 无效的构建类型 [%BUILD_TYPE%]
    exit /b 1
)

:: 设置构建参数
if "%BUILD_TYPE%"=="d" (
    set CMAKE_BUILD_TYPE=Debug
    set BUILD_DIR=out\debug
) else (
    set CMAKE_BUILD_TYPE=Release
    set BUILD_DIR=out\release
)

:: 获取默认程序名
if "%PROGRAM_NAME%"=="" (
    for %%i in ("%CD%") do set "PROGRAM_NAME=%%~nxi"
)
set EXEC_PATH="%BUILD_DIR%\bin\%PROGRAM_NAME%.exe"

:: 打印构建信息
echo.
echo [构建配置]
echo 当前目录:   %CD%
echo 构建类型:   %CMAKE_BUILD_TYPE%
echo 输出目录:   %BUILD_DIR%
echo 目标程序:   %PROGRAM_NAME%.exe
echo.

:: 配置CMake
echo [1/3] 配置CMake工程...
cmake -B "%BUILD_DIR%" -S . ^
    -G "MinGW Makefiles" ^
    -DCMAKE_BUILD_TYPE=%CMAKE_BUILD_TYPE% ^
    -DEXECUTABLE_OUTPUT_PATH="%BUILD_DIR%\bin" ^
    -DLIBRARY_OUTPUT_PATH="%BUILD_DIR%\lib"
if %errorlevel% neq 0 (
    echo ERROR: CMake配置失败
    exit /b 1
)

:: 构建项目
echo [2/3] 编译项目...
cmake --build "%BUILD_DIR%"
if %errorlevel% neq 0 (
    echo ERROR: 项目编译失败
    exit /b 1
)

:: 运行程序
echo [3/3] 运行目标程序...
if not exist %EXEC_PATH% (
    echo ERROR: 可执行文件不存在
    echo 路径: %EXEC_PATH%
    exit /b 1
)

%EXEC_PATH%
if %errorlevel% neq 0 (
    echo ERROR: 程序返回错误码 [!errorlevel!]
    exit /b 1
)

endlocal
exit /b 0