#!/bin/bash

cat code4hk.md | python3 interpolate.py > code4hk.annotated.md

cat begin.html > code4hk.html
markdown code4hk.annotated.md >> code4hk.html
cat end.html >> code4hk.html

