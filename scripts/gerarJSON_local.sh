#!/usr/bin/env bash
cat $1 | awk '{print $1,$3}' | sed -n '1,1000p' | sed 's/ /\":\"/g' | sed 's/$/\"/g' |sed 's/ˆ/\"/g' | tr '\n' ',' | sed 's/\",/\",\"/g' | sed 's/,\"$/}/g' | sed 's/^/{\"/'
