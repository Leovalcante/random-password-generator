#!/usr/bin/env bash
command -v python3 >/dev/null 2>&1 || { echo >&2 "python3 required but it's not installed. Aborting."; exit 1; }
python3 setup.py install