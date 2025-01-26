conan install . --output-folder=conan --build=missing --profile:all=vs2022-debug
conan install . --output-folder=conan --build=missing --profile:all=vs2022-release

mkdir build-x64
cd build-x64
cmake .. -DCMAKE_TOOLCHAIN_FILE=conan/conan_toolchain.cmake
cmake --build . --config=debug