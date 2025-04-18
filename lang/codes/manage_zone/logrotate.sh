#!/bin/bash

# cut log

[ ! -d "logs/" ] && mkdir "logs"

Time=$(date +%Y-%m-%d)

split -b 2M -d app.log logs/"$Time".split-size && \
  cat /dev/null >app.log