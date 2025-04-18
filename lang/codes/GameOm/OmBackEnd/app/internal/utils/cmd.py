"""
远程执行的命令
"""

add_cmd = """
[ ! -d {0} ] && mkdir -p {1}
svn --username {2} --password {3} checkout {4} {5} |grep -w revision
"""

con_cmd = """
version=$(svn update --username {0} --password {1} {2} |grep -w revision)
echo "svn version: $version"
"""

opt_cmd = """
cd {0}
sh {1} {2}
"""

node_cmd = """
nodeinfo -dpath {0}
"""
