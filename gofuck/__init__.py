# coding: utf-8

import os

def fuck_go():
    os.system('export GOPATH=`pwd`:$GOPATH')
    print 'cwd now in GOPATH'
    return 0
