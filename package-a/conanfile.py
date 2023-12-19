from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.layout import basic_layout


class PackageAConan(ConanFile):
    name = "package-a"
    version = "0.0.0"
    package_type = "shared-library"
    settings = "os", "compiler", "arch", "build_type"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualBuildEnv"
    exports_sources = ["CMakeLists.txt", "pkg-a.c", "pkg-a.h"]

    def layout(self):
        basic_layout(self)

    def requirements(self):
        # The implicit run=True causes buildenv vars from mock-gcc to be propagated to current and downstream host context
        self.requires("mock-gcc/0.0.0", headers=False, libs=True, transitive_libs=True)
        # Setting run=False fixes the issue
        # self.requires("mock-gcc/0.0.0", headers=False, libs=True, transitive_libs=True, run=False)
        return

    def build_requirements(self):
        self.tool_requires("mock-gcc/0.0.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["pkg-a"]
