chatgpt-on-wechat
│
├── .github  # GitHub 相关的配置文件，例如 issue 模板和 GitHub Actions 工作流文件
│
├── .git  # Git 版本控制相关的文件
│
├── .gitignore  # 指定 Git 忽略的文件和目录
│
├── .pre-commit-config.yaml  # Pre-commit 工具的配置文件，用于在提交之前自动运行某些操作，例如格式检查
│
├── .flake8  # Flake8 工具的配置文件，用于 Python 代码风格检查
│
├── Dockerfile  # Docker 构建文件，用于创建 Docker 镜像
│
├── LICENSE  # 开源许可证文件
│
├── README.md  # 项目的 README 文件，通常包含项目介绍、安装步骤等信息
│
├── app.py  # 项目的主程序入口
│
├── bot  # 包含各种 bot 的代码，例如 chatgpt，openai 等
│
├── bridge  # 桥接模块，可能用于连接不同的组件或服务
│
├── channel  # 渠道模块，可能用于管理和处理不同的通信渠道，例如微信、终端等
│
├── common  # 通用的辅助代码，例如日志、工具函数等
│
├── config-template.json  # 配置文件的模板
│
├── config.py  # 配置相关的 Python 文件
│
├── docker  # 包含 Docker 相关的文件，例如 Dockerfile 和 docker-compose.yml
│
├── docs  # 包含项目的文档，例如图像文件
│
├── lib  # 包含项目依赖的第三方库，例如 itchat
│
├── nixpacks.toml  # Nix 包管理器的配置文件
│
├── plugins  # 包含插件的代码，例如 banwords，hello，keyword 等
│
├── pyproject.toml  # Python 项目配置文件，通常用于指定项目的依赖库、构建工具等
│
├── requirements.txt  # 项目的 Python 依赖列表
│
├── requirements-optional.txt  # 项目的可选 Python 依赖列表
│
├── scripts  # 包含脚本的目录，例如启动脚本 start.sh，关闭脚本 shutdown.sh
│
├── translate  # 翻译相关的代码，包括各种翻译器，例如 baidu，google 等
│
└── voice  # 语音相关的代码，包括各种语音引擎，例如 azure，openai，baidu 等
