from conan import ConanFile
from conan.tools.layout import basic_layout


class MockGccConan(ConanFile):
    name = "mock-gcc"
    version = "0.0.0"
    package_type = "application"
    settings = "os", "compiler", "arch", "build_type"

    def package_id(self):
        del self.info.settings.compiler

    def layout(self):
        basic_layout(self, src_folder="src")

    def package_info(self):
        # Export runtime library directories and libraries...
        # e.g. self.cpp_info.libs = ["gfortran", "quadmath"]
        self.cpp_info.libs = ["dl", "pthread"]

        self.buildenv_info.define_path("CC", "mock-gcc")
        self.buildenv_info.define_path("CXX", "mock-gcc")
        self.buildenv_info.define_path("FC", "mock-gcc")
        self.buildenv_info.define_path("AR", "mock-gcc")
        self.buildenv_info.define_path("NM", "mock-gcc")
        self.buildenv_info.define_path("RANLIB", "mock-gcc")
