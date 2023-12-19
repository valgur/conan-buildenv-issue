cmake_minimum_required(VERSION 3.15)
project(mock-gcc C)

# Build a mock libgcc.so runtime
add_library(mock-gcc SHARED mock-gcc.c)

install(TARGETS mock-gcc
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
