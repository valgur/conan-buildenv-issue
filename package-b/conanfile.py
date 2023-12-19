from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.layout import basic_layout


class PackageBConan(ConanFile):
    name = "package-b"
    version = "0.0.0"
    package_type = "shared-library"
    settings = "os", "compiler", "arch", "build_type"
    generators = "VirtualBuildEnv", "CMakeToolchain", "CMakeDeps"
    exports_sources = ["test.sh", "CMakeLists.txt", "pkg-b.c"]

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires("package-a/0.0.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self.run("./test.sh", cwd=self.source_folder)

    def package(self):
        cmake = CMake(self)
        cmake.install()
