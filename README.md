Stupid
======

本来想用这个快速修改 `GOPATH` 的, 后来想起来这个进程结束也就没了, 其实并不起效.

懒得删了, 就留这里吧.

这么做比较简单:

在 .zshrc 或者 .bashrc 什么的加入:

```bash
function gofuck {
    export GOPATH=`pwd`:$GOPATH
    echo 'cwd now in your GOPATH'
}
```
