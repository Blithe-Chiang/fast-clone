# fasterclone 
make `git clone` faster in **China Mainland** by changing source.



## usage

  fasterclone GITHUB-REPO-URL

## requirements

* python 3.6+

---

## example


$ ./fasterclone.py https://github.com/Blithe-Chiang/breakfast.git     

Perform `git clone` https://gitclone.com/github.com/Blithe-Chiang/breakfast.git since using this URL will be faster than the original URL in China Mainland. 

When clone done, replace https://gitclone.com/github.com/Blithe-Chiang/breakfast.git with https://github.com/Blithe-Chiang/breakfast.git in `breakfast/.git/config`

