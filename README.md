# python-ai-learning
我的Python和AI学习记录
git config --global user.name "您的名字"
git config --global user.email "您的邮箱"
git config --list
克隆仓库到本地
# 1. 创建工作目录
cd ~/Desktop
mkdir ai-projects
cd ai-projects

# 2. 克隆仓库（使用HTTPS方式）
git clone https://github.com/您的用户名/python-ai-learning.git

# 3. 进入仓库目录
cd python-ai-learning

# 4. 查看仓库状态
git status
# 1. 查看当前状态（应显示hello.py为未跟踪文件）
git status

# 2. 添加文件到暂存区
git add hello.py

# 或添加所有文件
git add .

# 3. 查看暂存区状态（文件变绿）
git status

# 4. 提交到本地仓库
git commit -m "添加第一个Python程序Untitled-1.py"

# 5. 推送到GitHub
git push origin main
git push origin master

# 6. 输入GitHub用户名和密码（或使用Personal Access Token）
# Python AI学习仓库

## 项目介绍
这是我学习Python和人工智能的代码仓库，记录学习过程和项目代码。

## 学习进度
- [x] 第1周：Python基础入门
- [ ] 第2周：控制流和数据结构
- [ ] 第3周：面向对象编程
- [ ] 第4周：AI基础概念

## 目录结构
python-ai-learning/ ├── README.md # 项目说明 ├── week1/ # 第1周学习内容 │ ├── hello.py # 第一个程序 │ ├── variables.py # 变量练习 │ └── functions.py # 函数练习 ├── week2/ # 第2周学习内容 └── notes/ # 学习笔记 └── ai_history.md # AI历史笔记
## 学习资源
- [Python官方文档](https://docs.python.org/3/)
- [GitHub官方教程](https://docs.github.com/cn)
- [VS Code Python教程](https://code.visualstudio.com/docs/python/python-tutorial)

## 联系方式
- Email: your-email@example.com
- GitHub: @your-username

---
*最后更新：2024-01-01*
