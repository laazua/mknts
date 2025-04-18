#!/bin/bash

# svn 服务搭建
cat >/etc/yum.repos.d/wandisco-svn.repo <<-'EOF'
[WandiscoSVN]
name=Wandisco SVN Repo
baseurl=http://opensource.wandisco.com/centos/7/svn-1.10/RPMS/$basearch/
enabled=1
gpgcheck=0
EOF

yum clean all
yum install -y subversion mod_dav_svn httpd

cat >/etc/httpd/conf.d/svn.conf <<- 'EOF'
<Location /svn>
  DAV svn
  #SVNPath /data/backendrepo
  SVNParentPath /data/backendrepo/
    AuthType Basic
    AuthName "Authorization Realm"
    AuthUserFile /data/backendrepo/syfdata/conf/passwd
    AuthzSVNAccessFile /data/backendrepo/syfdata/conf/authz
    Satisfy all
    Require valid-user
</Location>
EOF
# 如果使用SVNPath指令,则<Location /projectname>      http://ip:port/projectname
# 如果使用SVNParentPath指令则,<Location /svn>, /svn是http访问的跟路径    http://ip:port/svn/projectname

mkdir -p /data/svndata && cd /data/svndata && svnadmin create projectname && chown -R apache:apache projectname
sed -i 's/#anon-access = none/anon-access = none/' projectname/conf/svnserve.conf
sed -i 's/#auth-access = write/auth-access = write/' projectname/conf/svnserve.conf
sed -i 's/#password-db = passwd/password-db = passwd/' projectname/conf/svnserve.conf
sed -i 's/#authz-db = authz/authz-db = authz/' projectname/conf/svnserve.conf

mv projectname/conf/passwd projectname/conf/passwd.default

htpasswd -cm conf/passwd test
# htpasswd -m conf/passwd username

# cat projectname/conf/authz 
# [groups]
# yunwei = test   定义一个组,并包含一个用户test
# [/]
# @test = rw      为一个组指定相关权限

svnserve -d -r /data/svndata
# svn 重启执行一下命令
# chcon -R -h -t httpd_sys_content_t /data/backendrepo/
