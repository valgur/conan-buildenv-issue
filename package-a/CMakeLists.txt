cmake_minimum_required(VERSION 3.15)
project(hello C)

add_library(hello hello.c)

install(TARGETS hello
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
install(FILES hello.h DESTINATION include)
