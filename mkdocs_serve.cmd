#!/bin/bash
export PATH="/home/xiaopch/miniconda3/bin:$PATH"
start http://127.0.0.1/
cmd /k mkdocs serve --dev-addr=0.0.0.0:80
sleep 3