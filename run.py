import sys
import os
import subprocess

def print_help():
    help_text = """
Usage: python run.py [build_type] [program_name]

Options:
  build_type    'd' for debug (default), 'r' for release
  program_name  Name of the program to run (default: current directory name)
"""
    print(help_text)

def run_cmake(build_type='d', program_name=None):
    current_dir = os.getcwd()
    if program_name is None:
        program_name = os.path.basename(current_dir)
    print(f"Current directory: {current_dir}")
    print(f"Program name: {program_name}")
    
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
    if '-h' or '--help' in sys.argv:
        print_help()
        sys.exit(0)
    
    build_type = sys.argv[1] if len(sys.argv) > 1 else 'd'
    program_name = sys.argv[2] if len(sys.argv) > 2 else None
    run_cmake(build_type, program_name)