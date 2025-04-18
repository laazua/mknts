#!/bin/bash


func1(){
    echo "$name"
}

func2() {
    echo $option
}

while true 
do
  case $1 in
    -n|--name)
        name=$2
        shift 2
        continue
        ;;
    -o|--option)
        option=$2
        shift 2
        continue
        ;;
    -h|--help)
        echo "sh $0 --name aa --option target"
        shift 2
        break
        ;;
     *)
        if [ "${name}" == "" ] && [ "${option}" == "" ];then
            exit
        fi
        func1
        func2
        break
        ;;
  esac
done
