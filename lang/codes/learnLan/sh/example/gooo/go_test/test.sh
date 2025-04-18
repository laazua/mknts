#!/usr/bin/env bash

echo "go run shell scripts"  > test.txt
for((i=0;i<10;i++));do
  echo $i
done