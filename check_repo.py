#!/usr/bin/env python3
"""
检查GitHub仓库状态
"""

import requests

def check_repo_status():
    # 配置信息
    REPO_OWNER = "yunhongfeng-tracy"
    REPO_NAME = "ai_daily_news"
    
    # GitHub API端点
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
    
    # 发送请求
    response = requests.get(url)
    
    print("GitHub仓库状态检查")
    print("=" * 50)
    print(f"仓库: {REPO_OWNER}/{REPO_NAME}")
    print(f"状态码: {response.status_code}")
    
    if response.status_code == 200:
        repo_info = response.json()
        print("✓ 仓库存在")
        print(f"仓库描述: {repo_info.get('description', '无描述')}")
        print(f"是否公开: {'是' if repo_info.get('private') == False else '否'}")
        print(f"创建时间: {repo_info.get('created_at')}")
        print(f"最后更新: {repo_info.get('updated_at')}")
    elif response.status_code == 404:
        print("✗ 仓库不存在")
        print("请先在GitHub上创建仓库: ai_daily_news")
    else:
        print(f"✗ 检查失败: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    check_repo_status()