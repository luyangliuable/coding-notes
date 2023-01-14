# Git

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Git](#git)
    - [git squash](#git-squash)
    - [git bisect](#git-bisect)
    - [change between http2 and http1.1](#change-between-http2-and-http11)
    - [change git buffer size](#change-git-buffer-size)
    - [aggressive git garbage collection](#aggressive-git-garbage-collection)

<!-- markdown-toc end -->


## git squash

## git bisect

## change between http2 and http1.1
```shell
git config --global http.version HTTP/1.1
git push
git config --global http.version HTTP/2
```

## change git buffer size
```shell
git config --global http.postBuffer 524288000

```

## aggressive git garbage collection
```shell
git gc --agressive

```

## Remove all files that are currently being ignored by Git,
```shell
git ls-files -i -c --exclude-standard | grep -v $(FILES_TO_NOT_REMOVE) | xargs git rm -r --cached
```
