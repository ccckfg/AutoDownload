# AutoDownload

AutoDownload 是一个用于自动批量下载 GitHub 指定 repo 最新 release 下的脚本。使用 AutoDownload，你可以批量、快速、简便地下载自己关注的 repo 最新版本，无需手动操作。

## 使用方法

使用 AutoDownload 非常简单，只需要按照以下步骤进行操作：

1. 克隆本项目到本地</br>```git clone https://github.com/ccckfg/AutoDownload.git``` 
2. 修改目录中repo.txt，设置要下载的 repo 列表和下载目录。<br>配置格式为owner/repo(下载目录)。若目录不存在，则会自动创建。
3. 运行脚本，由于本脚本的下载基于 Python wget库，你可能需要先用 pip 安装 wget。
```pip install wget```

## 注意事项

- 在使用 AutoDownload 之前，你需要确保已经安装了Python3和wget。
- 本脚本仅适用于 GitHub，不支持其他 Git 仓库。
- 如果你想要下载非 release 文件，可以自行修改脚本。
- 如果你在使用过程中遇到任何问题，可以提交 issue 寻求帮助。

## 开源协议

AutoDownload 使用 MIT 开源协议，你可以在遵守协议的前提下自由地使用、修改和分享本项目。详细的协议内容请参见 LICENSE 文件。

## 鸣谢
ChatGPT-3.5
