# GitHub文件上传工具

这是一个简单的Python脚本，用于将JSON文件上传到GitHub仓库。

## 使用方法

### 1. 安装依赖
```bash
pip install requests
```

### 2. 配置信息
编辑 `config.py` 文件，设置以下信息：
- `REPO_OWNER`: 您的GitHub用户名
- `GITHUB_TOKEN`: 您的GitHub个人访问令牌

### 3. 运行脚本
```bash
python upload_to_github.py
```

## 获取GitHub Token

1. 登录GitHub
2. 进入 Settings → Developer settings → Personal access tokens → Tokens (classic)
3. 点击 "Generate new token"
4. 选择 "classic" token
5. 设置过期时间（建议选择较长时间）
6. 勾选 "repo" 权限
7. 生成并复制token

## 功能特点

- 自动检测文件是否存在，支持创建新文件或更新现有文件
- JSON格式验证
- 详细的错误信息提示
- 自动生成提交信息

## 文件结构

```
.
├── upload_to_github.py  # 主上传脚本
├── config.py            # 配置文件
├── daily_news.json      # 要上传的JSON文件
└── README.md           # 说明文档
```

## 注意事项

- 请确保GitHub仓库 `ai_daily_news` 已存在
- 确保GitHub Token具有仓库的写入权限
- 脚本默认使用main分支