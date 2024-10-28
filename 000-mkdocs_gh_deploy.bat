::#!/bin/bash
::export PATH="/home/xiaopch/miniconda3/bin:$PATH"
mkdocs gh-deploy
start https://xiaopch.github.io/
cmd /k cd .
sleep 80