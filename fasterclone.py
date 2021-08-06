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

def get_github_repo_rul(args):
  github_repo_url = ''
  github_repo_urls = [x for x in args if x.startswith('https://github.com/') and x.endswith('.git')]
  try:
    github_repo_url = github_repo_urls[0]
  except IndexError:
    pass
  return github_repo_url

# change source
def change_source(github_repo_url):
  replaced_repo_url = github_repo_url.replace('github.com', 'github.com.cnpmjs.org')
  return replaced_repo_url

# perform clone 
def clone(args):

  proc = subprocess.run(["git", "clone", *args])

  if proc.returncode != 0:
    exit(CLONE_FAILED)

# restore original url in .git/config file
def restore(url, original_url):
  # get repo name
  # e.g. parse `breakfast` from  https://github.com/Blithe-Chiang/breakfast.git 
  repo_dir = original_url[original_url.rindex('/')+1:-4]

  if not os.path.isdir(repo_dir):
    exit(REPO_NOT_EXISTS)

  print('restoring...')

  filename = f'{repo_dir}/.git/config'

  with open(filename, 'r') as f:
    lines = f.readlines()
  
  # restoring original url
  lines = list(map(lambda line: line.replace(url, original_url), lines))

  with open(filename, 'w') as f:
    f.writelines(lines)


def main():
  args = sys.argv[1:]

  github_repo_url = get_github_repo_rul(args)

  if github_repo_url:
    idx = args.index(github_repo_url)
    replaced_url = change_source(github_repo_url)
    args = args[:idx] +  [replaced_url]  + args[idx+1:]

    clone(args)

    # restore
    restore(replaced_url, github_repo_url)
  else:
    clone(args)

if __name__ == '__main__':
  main()
