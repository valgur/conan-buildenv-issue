cmake_minimum_required(VERSION 3.15)
project(pkg-a C)

add_library(pkg-a pkg-a.c)

install(TARGETS pkg-a
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
install(FILES pkg-a.h DESTINATION include)
