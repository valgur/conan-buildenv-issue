cmake_minimum_required(VERSION 3.15)
project(pkg-b C)

find_package(package-a REQUIRED)

add_executable(pkg-b pkg-b.c)
target_link_libraries(pkg-b PRIVATE package-a::package-a)

install(TARGETS pkg-b)
