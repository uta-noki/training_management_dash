# syntax=docker/dockerfile:1
# FROM node:19
# FROM httpd:latest
# FROM python:3.9.18-slim
FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
# # インタラクティブモードにならないようにする
# ARG DEBIAN_FRONTEND=noninteractive

# # タイムゾーンを日本に設定
# ENV TZ=Asia/Tokyo

WORKDIR /app
# COPY ./html /usr/local/apache2/htdocs/

# 起動シェルをshからbashに変更
SHELL ["/bin/bash", "-c"]

# パッケージなど
RUN apt update && \
    apt install -y \
    time \
    tzdata \
    tree \
    git \
    # curl \
    # gcc-9 \
    # g++-9 \
    # gdb \
    python3\
    python3-pip \
    vim\
    mysql-server\
    systemd
#     pytorch
# C++でAtCoder Library(ACL)を使えるようにする
# RUN git clone https://github.com/atcoder/ac-library.git /lib/ac-library
# ENV CPLUS_INCLUDE_PATH /lib/ac-library

# atcoder-cliのインストール
# RUN npm install -g atcoder-cli@2.2.0

# ユーザー名を指定
# ARG USERNAME=user
# ARG GROUPNAME=user

# UID, GIDはidコマンドで確認し，ログインユーザーのUID, GIDを指定する
# ARG UID=1000
# ARG GID=1000

# ユーザーを作成
# RUN groupadd -g $GID $GROUPNAME && \ 
# RUN useradd -m -u $UID -g $GID -s /bin/bash $USERNAME

# 初期ユーザーの変更
# USER $USERNAME

# コンテスト補助アプリケーションをインストール



# パッケージの追加とタイムゾーンの設定
# 必要に応じてインストールするパッケージを追加してください
RUN apt-get update && apt-get install -y \
    tzdata \
&&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/*

RUN useradd -m shinozaki

ENV TZ=Asia/Tokyo

# JupyterLab関連のパッケージ（いくつかの拡張機能を含む）
# 必要に応じて、JupyterLabの拡張機能などを追加してください
# RUN python -m pip install --upgrade pip \
# &&  pip install --no-cache-dir \
#     black \
#     jupyterlab \
#     jupyterlab_code_formatter \
#     jupyterlab-git \
#     lckr-jupyterlab-variableinspector \
#     jupyterlab_widgets \
#     ipywidgets \
#     import-ipynb

# 基本パッケージ
# Pythonでよく利用する基本的なパッケージです
# JupyterLabの動作には影響しないので、必要に応じてカスタマイズしてください
RUN pip install --no-cache-dir \
    dash==2.15.0\
    dash_bootstrap_components\
    dash_auth\
    dash_daq\
    pandas\
    scikit-learn\
    schedule\
    openpyxl\
    numpy\
    jupyterlab\
    mysql-connector-python\
    mod_wsgi-httpd



# 追加パッケージ（必要に応じて）
# 各環境に特化したパッケージがある場合、この部分に追加します
# RUN pip install --no-cache-dir \
#     pydeps \
#     graphviz \
#     pandas_profiling \
#     shap \
#     umap \
#     xgboost \
#     lightgbm
    
# RUN python -m pip install jupyter notebook -U