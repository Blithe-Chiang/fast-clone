#!/usr/bin/env python
import subprocess
import sys
import os

# exit code
NO_URL_PROVIDED = 1
URL_FORMAT_ERROR = 2
CLONE_FAILED = 3
REPO_NOT_EXISTS = 4

USAGE_STR = """
fasterclone 
=================
usage: 
  fasterclone <github-repo-url>
  
how:
  fasterclone <github-repo-url>
      translated to 
    ================> 
  git clone <replaced-repo-url>
      when clone done
    ================> 
  restore <replaced-repo-url> with original <github-repo-url> in `<repo-dir>/.git/config`
"""

def usage():
  print(USAGE_STR)

# get repo url from args
def get_repo_url():
  try:
    github_repo_url = sys.argv[1]
  except IndexError:
    usage()
    exit(NO_URL_PROVIDED)
  return github_repo_url

# get replaced url 
def get_replaced_url(github_repo_url):
  try:
    idx = github_repo_url.index('github.com')
    replaced_repo_url = github_repo_url[:idx]+'gitclone.com/'+github_repo_url[idx:]
  except ValueError:
    print('github repo url format error')
    exit(URL_FORMAT_ERROR)
  return replaced_repo_url

# perform clone 
def clone(url):
  ret = subprocess.run(["git", "clone", url])

  if ret.returncode != 0:
    exit(CLONE_FAILED)

# restore original url in .git/config file
def restore(url, original_url):
  # get repo name
  # e.g. parse `breakfast` from  https://github.com/Blithe-Chiang/breakfast.git 
  repo_dir = original_url[original_url.rindex('/')+1:-4]

  if not os.path.isdir(repo_dir):
    exit(REPO_NOT_EXISTS)

  filename = f'{repo_dir}/.git/config'

  with open(filename, 'r') as f:
    lines = f.readlines()
  
  # restoring original url
  lines = list(map(lambda line: line.replace(url, original_url), lines))

  with open(filename, 'w') as f:
    f.writelines(lines)


def main():
  repo_url = get_repo_url()
  replaced_url = get_replaced_url(repo_url)
  clone(replaced_url)

  print('restoring...')
  restore(replaced_url, repo_url)

if __name__ == '__main__':
  main()
