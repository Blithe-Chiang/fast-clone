# fasterclone 

make `git clone` faster in **China Mainland** by changing source.

[中文文档](./README.zh-CN.md)


## usage

fasterclone GITHUB-REPO-URL


## requirements

* python 3.6+


## example

$ ./fasterclone.py https://github.com/Blithe-Chiang/breakfast.git     

Perform `git clone` https://github.com.cnpmjs.org/Blithe-Chiang/breakfast.git since using this URL will be faster than the original URL in China Mainland. 

When clone done, replace https://github.com.cnpmjs.org/Blithe-Chiang/breakfast.git with https://github.com/Blithe-Chiang/breakfast.git in `breakfast/.git/config`

