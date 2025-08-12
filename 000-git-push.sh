#!/bin/bash
git config --global color.ui auto


# 生成提交信息
commit_message="Auto-commit at $(date +"%Y-%m-%d %H:%M:%S") with random ID $RANDOM"

# 输出提示信息
echo "Starting Git push script..."



# 检查当前状态
echo "Checking current Git status..."
git status

# 添加所有文件
echo "Adding all files to the staging area..."
git add -A

# 再次检查状态
echo "Checking Git status after adding files..."
git status

# 提交更改
echo "Committing changes with message: '$commit_message'..."
git commit -m "$commit_message" 

# 推送更改
echo "Pushing changes to remote repository..."
git push 

echo "Git push completed successfully!"



# 等待5秒后退出
echo "Waiting for 15 seconds before exiting..."
sleep 15
echo "Script exited."