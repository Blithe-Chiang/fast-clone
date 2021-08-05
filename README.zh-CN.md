# fasterclone

让 `git clone` 变得更快一些


## 用法

fasterclone GITHUB-REPO-URL


## 要求

* python 3.6+


## 例子

$ ./fasterclone.py https://github.com/Blithe-Chiang/breakfast.git  

### 原理

这行命令会执行 `git clone` https://github.com.cnpmjs.org/Blithe-Chiang/breakfast.git  

将下载源从github.com换成github.com.cnpmjs.org，因为第三方源下载速度会快很多。

当`git clone`完成之后，直接修改仓库配置文件中的配置信息，恢复项目原来的源。

