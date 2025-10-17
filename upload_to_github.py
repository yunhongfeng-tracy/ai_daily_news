#!/usr/bin/env python3
"""
GitHub文件上传脚本
将daily_news.json上传到指定的GitHub仓库
"""

import requests
import base64
import json
import os
from datetime import datetime

# 导入配置
try:
    from config import REPO_OWNER, REPO_NAME, GITHUB_TOKEN, FILE_TO_UPLOAD, BRANCH
except ImportError:
    print("错误：找不到配置文件 config.py")
    print("请确保 config.py 文件存在并包含正确的配置信息")
    exit(1)

def upload_to_github():
    FILE_PATH = FILE_TO_UPLOAD
    COMMIT_MESSAGE = f"更新资讯日报数据 - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    # 读取文件内容
    if not os.path.exists(FILE_PATH):
        print(f"错误：文件 {FILE_PATH} 不存在")
        return
    
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查文件是否为有效的JSON
    try:
        json.loads(content)
        print("✓ JSON文件格式验证通过")
    except json.JSONDecodeError as e:
        print(f"错误：JSON文件格式无效 - {e}")
        return
    
    # 编码文件内容为base64
    content_base64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    # GitHub API端点
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    
    # 请求头
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 检查文件是否已存在（获取SHA）
    response = requests.get(url, headers=headers)
    
    sha = None
    if response.status_code == 200:
        sha = response.json().get("sha")
        print("✓ 文件已存在，将进行更新")
    elif response.status_code == 404:
        print("✓ 文件不存在，将创建新文件")
    else:
        print(f"错误：检查文件状态失败 - {response.status_code}")
        print(response.text)
        return
    
    # 准备上传数据
    data = {
        "message": COMMIT_MESSAGE,
        "content": content_base64,
        "branch": BRANCH
    }
    
    if sha:
        data["sha"] = sha
    
    # 上传文件
    response = requests.put(url, headers=headers, data=json.dumps(data))
    
    if response.status_code in [200, 201]:
        print("✓ 文件上传成功！")
        print(f"提交信息：{COMMIT_MESSAGE}")
        print(f"文件链接：{response.json().get('content', {}).get('html_url', 'N/A')}")
    else:
        print(f"错误：上传失败 - {response.status_code}")
        print(response.text)

def main():
    print("GitHub文件上传工具")
    print("=" * 50)
    
    # 检查配置
    if "YOUR_GITHUB_USERNAME" in REPO_OWNER or "YOUR_GITHUB_TOKEN" in GITHUB_TOKEN:
        print("请先配置 config.py 文件中的以下信息：")
        print("1. 将 REPO_OWNER 替换为您的GitHub用户名")
        print("2. 将 GITHUB_TOKEN 替换为您的GitHub个人访问令牌")
        print("\n获取GitHub Token的方法：")
        print("1. 登录GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)")
        print("2. 生成新token，勾选 repo 权限")
        print("3. 复制token并替换 config.py 中的 YOUR_GITHUB_TOKEN")
        return
    
    upload_to_github()

if __name__ == "__main__":
    main()