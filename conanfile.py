from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class yolov9recipe(ConanFile):
    name = "yolov9recipe"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Omkar Nadkarni"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "yolov9 with bytetrack and tensorrt"
    topics = ("yolov9", "bytetrack", "tensorrt")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    
    def requirements(self):
        self.requires("opencv/4.10.0")
        self.requires("eigen/3.4.0")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
    
