#!/bin/bash

# === 配置信息 ===
GITHUB_USER="kaxuan112"
REPO_NAME="telegram-bot"
TOKEN=""$kaxuan112""

# === 开始 ===
echo "🔄 正在推送到 GitHub..."

# 初始化仓库（如果已初始化过，会自动跳过）
git init

# 删除旧的远程仓库，重新绑定
git remote remove origin 2>/dev/null
git remote add origin https://$GITHUB_USER:$TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git

# 添加修改过的文件
git add .

# 自动生成 commit 信息（带时间戳，避免重复）
git commit -m "Auto commit on $(date '+%Y-%m-%d %H:%M:%S')" || echo "⚠️ 没有文件变化，跳过 commit"

# 确保分支是 main
git branch -M main

# 推送到 GitHub
git push -u origin main

echo "✅ 已成功推送到 GitHub: https://github.com/$GITHUB_USER/$REPO_NAME"
