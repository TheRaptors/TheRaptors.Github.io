#!/usr/bin/env bash

egrep '<DT><A HREF=' bookmarks_*.html | sed -e 's/ICON=.*"//g; s/ADD_DATE=".*"//g; s/^ *//g; s/ >/>/g' | sort | uniq > bookmarks_$(date +%Y-%m-%d).html
