#!/usr/bin/env bash

set -e

echo "Seting up add plugin code $PWD"

pip install -e .

reentry scan

verdi code setup \
    --non-interactive \
    --label add \
    --on-computer \
    --computer localhost \
    --remote-abs-path $PWD/bin/add \
    --input-plugin add.calculation
