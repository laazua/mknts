#!/bin/bash
java=/usr/local/jdk17/bin/java

# Jenkins CLI 客户端的路径
JENKINS_CLI=./jenkins-cli.jar
JENKINSCLI="$java -jar $JENKINS_CLI -s $JENKINS_URL -auth $JENKINS_USER:$JENKINS_TOKEN"
# Jenkins URL 和用户名
JENKINS_URL=http://172.16.5.108:8082/
JENKINS_USER=admin

# API Token
JENKINS_TOKEN=11989fb125a0640799409326072ce1e7fa

# 获取正在运行的所有任务的列表
RUNNING_JOBS=$($JENKINSCLI list-builds)

# 从列表中删除最新任务
LATEST_JOB=$($JENKINSCLI last-build <test>)
echo "${LATEST_JOB}"
RUNNING_JOBS=$(echo "$RUNNING_JOBS" | grep -v "$LATEST_JOB")

# 遍历列表中的任务，并终止它们
for JOB in $RUNNING_JOBS
do
  JENKINSCLI stop-build $JOB
done
