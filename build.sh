#!/bin/bash

set -e

[ -f "setup.py" ] && rm setup.py
[ -d "./dist" ] && rm -rf dist
[ -d "./build" ] && rm -rf build

poetry build
