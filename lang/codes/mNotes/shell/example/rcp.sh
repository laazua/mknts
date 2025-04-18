#!/bin/bash

## remote cp

REMOTE_IP=$1
REMOTE_PA=$2
FILE_NAME=$3

## check cmd args
if [[ "${REMOTE_IP}" == "" ]] && [[ "${REMOTE_PA}" == "" ]] && [[ "${FILE_NAME}" == "" ]]
then
    echo "sh $0 172.16.9.128 /data filename"
    exit 0
fi

ssh -q -tt ${REMOTE_IP} "nc -l 8088 | qpress -dio > ${REMOTE_PA}/${FILE_NAME} &"
if [[ $? -eq 0 ]]
then
    echo "remote nc listen on 8088"
else
    echo "remote nc listen error."
fi

qpress -o ${FILE_NAME} | nc ${REMOTE_IP} 8088
if [[ $? -eq 0 ]]
then
    echo "${FILE_NAME} scp to ${REMOTE_IP}:${REMOTE_PA}/${FILE_NAME} success."
else
    echo "${FILE_NAME} scp to ${REMOTE_IP}:${REMOTE_PA}/${FILE_NAME} failed."
fi
