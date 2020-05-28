from conans import ConanFile, CMake, tools
from os import path


class IglooConan(ConanFile):
    name = "igloo"
    version = "1.1.1"
    license = "BSL-1.0"
    author = "Julien Graziano julien@graziano.fr"
    url = "https://github.com/khdkhd/conan-igloo"
    description = "A framework for unit testing in C++"
    topics = ("C++", "Test", "BDD", "TDD")
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/joakimkarlsson/igloo.git")
        self.run("cd igloo && git checkout igloo.1.1.1")
        self.run("cd igloo && git submodule init")
        self.run("cd igloo && git submodule update")

    def package(self):
        self.copy("*.h", dst="include", src="igloo", excludes="tests")
