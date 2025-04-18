#!/bin/bash

>/tmp/platform
>/tmp/memm

ps aux|grep -v "grep" |grep "javapro" > /tmp/javamen
while read line;do
	echo $line | awk '{print $NF}'|awk -F'/' '{print $4}' >> /tmp/platform 
	echo $line | awk '{print $27}' >> /tmp/memm
done < /tmp/javamen
paste /tmp/platform /tmp/memm
rm -rf /tmp/platform
rm -rf /tmp/memm
