#include <sstream>
#include <string>

std::string
helloworld() {
    return "Hello, world!";
}

#include <igloo/igloo_alt.h>

using namespace igloo;

Describe(hello_world) {
    It(only_print_hello) {
        Assert::That(helloworld(), Equals("Hello, world!"));
    }
};

int
main(int argc, const char *argv[]) {
    return TestRunner::RunAllTests(argc, argv);
}