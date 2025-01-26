cmake_minimum_required(VERSION 3.20)
project(yolov9-bytetrack-trt)

find_package(CUDA REQUIRED)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
add_definitions(-DAPI_EXPORTS)

# Include CUDA directories
include_directories(${CUDA_INCLUDE_DIRS})
include_directories(src/)
include_directories(bytetrack/)


# Add source files
set(SOURCES
    main.cpp
    src/yolov9.cpp
    bytetrack/BYTETracker.cpp
    bytetrack/KalmanFilter.cpp
    bytetrack/lapjv.cpp
    bytetrack/Object.cpp
    bytetrack/Rect.cpp
    bytetrack/STrack.cpp    
)

# Add CUDA source files
set(CUDA_SOURCES src/preprocess.cu)

# Add headers
set(HEADERS
    src/yolov9.h
    src/macros.h
    src/logging.h
    src/cuda_utils.h
    src/preprocess.h
)

file(GLOB BYTETRACK_HEADERS "bytetrack/*.h")

# Set TensorRT path if not set in environment variables
set(TENSORRT_DIR "${PROJECT_SOURCE_DIR}/../../TensorRT-10.8.0.43")

# Include TensorRT
include_directories(${TENSORRT_DIR}/include)
link_directories(${TENSORRT_DIR}/lib)
set(TENSORRT_LIBS nvinfer nvinfer_plugin nvparsers nvonnxparser)

# Create an executable
cuda_add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS} ${CUDA_SOURCES} ${BYTETRACK_HEADERS})

find_package(OpenCV)
target_link_libraries(${PROJECT_NAME} opencv::opencv)

find_package(Eigen3 REQUIRED)
target_link_libraries(${PROJECT_NAME} Eigen3::Eigen)