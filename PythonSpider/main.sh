#!/usr/bin/env bash

if [ $(($(date "+%H") % 12)) == 0 ]; then
    python ./XunLeiBiZhi.py ./XunLeiBiZhi/$(date "+%Y-%m-%d_%H:%M:%S")
fi

if [ $(($(date "+%H") % 6)) == 0 ]; then
    python ./NeiHanFuLiShe_iOS.py ./NeiHanFuLiShe_iOS/$(date "+%Y-%m-%d_%H:%M:%S")
    cd ../ && sh ./GitHubForLinux.sh
fi
