#!/usr/bin/env bash

if [ $(($(date "+%H") % 12)) == 0 ]; then
    python ./XunLeiBiZhi.py > ./XunLeiBiZhi/$(date "+%Y-%m-%d_%H:%M:%S").txt
fi

if [ $(($(date "+%H") % 12)) == 0 ]; then
    python3 ./BaiSiBuDeJie.py > ./BaiSiBuDeJie/$(date "+%Y-%m-%d_%H:%M:%S").txt
fi

if [ $(($(date "+%H") % 12)) == 0 ]; then
    python ./LoveBiZhi.py > ./LoveBiZhi/$(date "+%Y-%m-%d_%H:%M:%S").txt
fi

if [ $(($(date "+%H") % 6)) == 0 ]; then
    python ./NeiHanFuLiShe_iOS.py > ./NeiHanFuLiShe_iOS/$(date "+%Y-%m-%d_%H:%M:%S").txt
    cd ../ && sh ./GitHubForLinux.sh
fi
