#!/usr/bin/env bash

if [ ! -d .git -a ! -f manage.py ];then
    echo 'Warning:The Work Directory Is Wrong. Please Check It And Retry!'
    exit
else
    git add -A .
    git commit -m "$(date +%Y-%m-%d\ %H:%M:%S)"
    git push $(basename `pwd`) master
fi
