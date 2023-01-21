#!/bin/bash
modified=$(git status | awk '/modified:/ { print $2 }')

untracked=$(git status --porcelain | awk '/^\?\?/ { print $2 }')

gitmessage="Added notes on $untracked. Modified notes $modified."
echo $gitmessage

git add .
git commit -m "$gitmessage"
# git push
