#!/usr/bin/bash

## python标准库zipapp打包python项目源码

set -e

Help() {
cat <<EOF

    help information:
        -s|--source    source code path.
        -e|--entry     main entry point.
        -o|--output    bundled file.

    pip install -r requirements.txt -t libs

    The project structure is as follows:
        .
        ├── buildpy.sh
        ├── libs
        ├── requirements.txt
        └── src
        └── example
            ├── api
            │   └── test.py
            ├── __init__.py
            └── __main__.py
    example:
        $0 -s src -e example.__main__:main -o example

EOF
    exit -1
}

# 使用 getopt 解析长选项
TEMP=$(getopt -o s:e:o:v --long source:,entry:,output:,verbose -n 'buildpy.sh' -- "$@")
eval set -- "$TEMP"

# 默认值
src=""
lib=""
entry=""
output=""
verbose=0

# 处理参数
while true; do
    case "$1" in
        -s|--source)
            src="$2"
            shift 2
            ;;
	-e|--entry)
	    entry="$2"
	    shift 2
	    ;;
        -o|--output)
            output="$2"
            shift 2
            ;;
        -v|--verbose)
            verbose=1
            shift
            ;;
        --)
            shift
            break
            ;;
        *)
	    Help
            ;;
    esac
done

if [ $verbose -eq 1 ];then
    set -x
fi

if [ ! -f "requirements.txt" ];then
    echo "  source .venv/bin/activate"
    echo "  python -m pip freeze >requirements.txt"
    exit
fi

# 输出解析结果
#echo "Verbose: $verbose"
#echo "Source: $src"
#echo "Modules: $lib"
#echo "Output file: $output"

if [ "$src" == "" ] || [ "$entry" == "" ] || [ "$output" == "" ];then
    Help
else
    tmp="build"
    if [ ! -d $tmp ];then
        mkdir $tmp
    fi
    python -V >/dev/null && [ $? -ne 0 ] && echo "Not found python interpreter" && exit
    python -m pip install -r requirements.txt -t libs && cp -r ${src}/* libs/* $tmp
    if [ -d $src ] && [ -d "libs" ];then
        python -m zipapp $tmp -o ${output}.pyz -m $entry --compress && rm -fr $tmp libs
    fi
fi


