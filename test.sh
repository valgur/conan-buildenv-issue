#!/bin/bash
set -e

(cd mock-gcc && conan create .)
(cd package-a && conan create .)
(cd package-b && conan create .)
