#!/bin/bash

# cut log

[ ! -d "logs/" ] && mkdir "logs"

Time=$(date +%Y-%m-%d)
Path=$(cd "$(dirname $0)" || exit; pwd)
split -b 2M -d "$Path"/logs/app.log "$Path"/logs/"$Time".split-size && \
  cat /dev/null >logs/app.log