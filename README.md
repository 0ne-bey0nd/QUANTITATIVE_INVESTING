# ***QIS*** v0.2.0

[TOC]

---

## 1. 项目简介

QIS(Quantitative Investing System)是一个量化投资系统，主要用于股票、期货、期权等金融产品的量化交易。

## 2. 项目结构

- [ ] 数据获取模块
    - [x] 交易日数据
    - [x] 股票分时成交数据（3s tick）
    - [ ] 股票盘口数据

## 3. 本地部署过程

## 本地部署过程

### Linux

#### 最低配置

[//]: # (TODO: 添加最低配置)

#### 推荐配置

| 配置项  | 推荐配置             |
|------|------------------|
| CPU  | 4核以上             |
| 内存   | 8G以上             |
| 硬盘   | 100G 以上          |
| 操作系统 | Ubuntu 22.04 LTS |

查看ubuntu版本

```bash
lsb_release -a
```

#### 下载项目

```bash
git clone --recursive https://github.com/0ne-bey0nd/QUANTITATIVE_INVESTING.git
cd QUANTITATIVE_INVESTING
export QIS_PROJECT_ROOT_PATH=$(pwd)
export FDA_PROJECT_ROOT_PATH=$(pwd)/FinanceDataAPI

```

#### 安装依赖

##### 安装和配置miniconda

> https://docs.anaconda.com/free/miniconda/

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  # 下载miniconda安装包
sha256sum Miniconda3-latest-Linux-x86_64.sh # 检查sha256值
bash Miniconda3-latest-Linux-x86_64.sh # 安装miniconda
conda init bash # 初始化conda
# conda init zsh # 初始化conda

conda --version # 查看conda版本 # 开发环境 conda 24.3.0

# 换源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

##### 创建虚拟环境

```bash
cd $QIS_PROJECT_ROOT_PATH
# 创建python 3.9虚拟环境
conda create -n qis python=3.9
# 激活虚拟环境
conda activate qis
# pip换源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 安装依赖
pip install virtualenv
# 创建虚拟环境
python -m venv qis_venv
export QIS_VENV_ROOT=$QIS_PROJECT_ROOT_PATH/qis_venv
# 将相关环境写入到初始化脚本
sed -i.bak "s#PYTHONPATH=.*#PYTHONPATH=$PWD/python:$PWD/FinanceDataAPI/python#g" bin/init_env.sh
sed -i.bak "s#venv_path=.*#venv_path=${QIS_VENV_ROOT}#g" bin/init_env.sh

# 激活虚拟环境
source bin/init_env.sh
# 安装依赖库
pip install -r requirements.txt
```

##### 使用docker部署mysql数据库

```bash
netstat -anp|grep 3306
docker pull mysql
docker run --name qis-mysql -p 3307:3306 -v /home/mysql_data:/var/lib/mysql --restart=always -e MYSQL_ROOT_PASSWORD={your_password} -d mysql
mysql -h 127.0.0.1 -P 3307 -u root -p 
```

##### 数据库具体配置

```mysql
CREATE DATABASE market_data;
-- 按照数据库部署文档配置数据库
```

##


