import requests
import json
import os
import threading
import subprocess
import logging

# 读取 repos.txt 文件并检查格式
with open('repos.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split('/')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error: Invalid format in line: {line}")
            exit(1)
        owner, repo = parts
        if ' ' in repo:
            dir_name = repo.split(' ', 1)[1]
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)


# 设置要下载的 GitHub repo 列表和下载目录
print('Start to download,please wait for a little while...')
repos_file = "repos.txt"
repos = []
with open(repos_file, "r") as f:
    for line in f:
        line = line.strip()
        if line:
            owner_repo, download_dir = line.split("(")
            owner, repo = owner_repo.split("/")
            download_dir = download_dir.strip(")").strip()
            repos.append({"owner": owner, "repo": repo, "dir": download_dir})

# 定义下载函数
def download_assets(asset_url, download_dir):
    filename = os.path.basename(asset_url)
    filepath = os.path.join(download_dir, filename)
    subprocess.run(['wget', '-O', filepath, asset_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 获取所有 GitHub repo 的最新 Release 和 pre-release 信息
releases_info = []
for repo in repos:
    url = f"https://api.github.com/repos/{repo['owner']}/{repo['repo']}/releases"
    response = requests.get(url)
    releases = json.loads(response.text)
    if releases:
        releases_info.append(releases)

# 遍历所有 GitHub repo 的 Release 和 pre-release，获取每个 Release 的所有 assets 文件的下载链接
asset_urls = []
for i, releases in enumerate(releases_info):
    release = releases[0] # 最新的 release
    pre_release = releases[1] if len(releases) > 1 else None # 最新的 pre-release
    if release and pre_release and pre_release["published_at"] > release["published_at"]:
        release = pre_release
    for asset in release['assets']:
        asset_urls.append((asset['browser_download_url'], repos[i]['dir']))

# 多线程下载所有 assets 文件
threads = []
for asset_url in asset_urls:
    thread = threading.Thread(target=download_assets, args=asset_url)
    threads.append(thread)
    thread.start()

# 等待所有下载线程结束
for thread in threads:
    thread.join()

# 添加 logging，输出下载完成信息
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('All assets files downloaded.')
