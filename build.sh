#!/bin/bash

[ -d "./dist" ] && rm -rf "./dist"
[ -d "./build" ] && rm -rf "./build"
[ -d "./cython_build" ] && rm -rf "./cython_build"
[ -f "./setup.py" ] && rm "./setup.py"
poetry build --format wheel
find . -name "*.so" -type f -delete
