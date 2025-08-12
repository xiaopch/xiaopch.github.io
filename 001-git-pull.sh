#!/bin/bash


# 启用 Git 彩色输出
git config --global color.ui auto

# 输出提示信息
echo "Starting Git pull script..."



# 检查当前状态
echo "Checking current Git status..."
git status



# 执行 git pull
echo "Pulling latest changes from remote repository..."
git pull 

echo "Git pull completed successfully!"



# 等待3秒后退出
echo "Waiting for 15 seconds before exiting..."
sleep 15
echo "Script exited."