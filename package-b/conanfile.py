from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.layout import basic_layout


class PackageBConan(ConanFile):
    name = "package-b"
    version = "0.0.0"
    package_type = "shared-library"
    settings = "os", "compiler", "arch", "build_type"
    generators = "VirtualBuildEnv"
    exports_sources = ["test.sh"]

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires("package-a/0.0.0")

    def build(self):
        self.run("./test.sh", cwd=self.source_folder)
