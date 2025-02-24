import sys
import os
import subprocess

def run_cmake(build_type, program_name):
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    # Set build directory and CMAKE_BUILD_TYPE based on argument
    build_dir = "out/debug" if build_type.lower() == 'd' else "out/release"
    cmake_build_type = "Debug" if build_type.lower() == 'd' else "Release"
    
    # Construct cmake configure command
    cmake_cmd = [
        "cmake",
        "-B", build_dir,
        "-S", ".",
        f"-DEXECUTABLE_OUTPUT_PATH={current_dir}/{build_dir}/bin",
        f"-DLIBRARY_OUTPUT_PATH={current_dir}/{build_dir}/lib",
        f"-DCMAKE_BUILD_TYPE={cmake_build_type}",
    ]
    
    # Configure
    subprocess.run(cmake_cmd, check=True)
    print(f"CMAKE build configured successfully in {build_dir}")
    
    # Build
    build_cmd = ["cmake", "--build", build_dir]
    subprocess.run(build_cmd, check=True)
    print(f"CMAKE build completed successfully in {build_dir}")
    
    # Run
    run_cmd = [f"./{build_dir}/bin/{program_name}"]
    subprocess.run(run_cmd, check=True)
    print(f"Program executed successfully from {build_dir}/bin/{program_name}")

if __name__ == "__main__":
    run_cmake(sys.argv[1], sys.argv[2])