## nginx编译安装
nginx()
{
	echo "##########NGINX INSTALL##########" >> ${CURDIR}/install_logs/nginx.log
	echo -e "\e[32mnginx版本选择: [${NGX_VER[@]}]\e[0m"
	read -p "> " version
	echo "install nginx-${version}"
	sleep 2

	get_ngx_pkg ${version}
	[ ! -d /usr/local/nginx ] && mkdir /usr/local/nginx
	[ "${NNUM}" = "" ] && useradd ${NUSER} -s /sbin/nologin
	
	tar -zxf nginx-${version}.tar.gz && cd nginx-${version}
	./configure --user=www --group=www \
        	    --prefix=/usr/local/nginx \
	 			--with-http_stub_status_module \
			 	--with-ipv6 \
				--with-http_gzip_static_module \
				--with-http_realip_module \
        		--with-http_ssl_module >> ${CURDIR}/install_logs/nginx.log  2>&1
	[ $? -ne 0 ] && echo "nginx configure error." >> ${CURDIR}/install_logs/nginx.log && exit
	make && make -j ${CORE} install
	[ $? -ne 0 ] && echo "nginx install error." >> ${CURDIR}/install_logs/nginx.log && exit 
	echo "nginx install successful." >> ${CURDIR}/install_logs/nginx.log
	
}

## apache编译安装
apache()
{
	echo "#########APACHE INSTALL##########" >> ${CURDIR}/install_logs/apache.log
	echo -e "\e[32mapache版本选择: [$APA_VER[@]}]\e[0m"
	read -p "> " version
	get_apa_pkg
	[ ! -d /usr/local/apache ] && mkdir /usr/local/apache
	
	tar -zxf httpd-${version}.tar.gz && cd httpd-${version}
	./configure --prefix=/usr/local/apache \
				--with-mpm=prefork 		\	
        		--enable-rewrite --enable-deflate \
        		--disable-userdir --enable-so \
        		--enable-expires --enable-headers \
        		--with-included-apr --enable-ssl \
				--enable-mime-magic --enable-ssl --with-crypto \
        		--with-ssl --enable-static-support >> ${CURDIR}/install_logs/apache.log 2>&1
	[ $? -ne 0 ] && echo "apache configure error." >> ${CURDIR}/install_logs/apache.log && exit
	make && make -j ${CORE} install
	[ $? -ne 0 ] && echo "apache install error." >> ${CURDIR}/install_logs/apache.log && exit
	echo "apache install successful." >> ${CURDIR}/install_logs/apache.log
}

## php编译安装
php()
{
	echo "###########PHP INSTALL###########" >> ${CURDIR}/install_logs/php.log
	echo -e "\e[32mphp版本选择: [${PHP_VER[@]}]\e[0m"
	read -p "> " version
	echo "install php-${version}..."
	sleep 2

	get_php_pkg
	[ ! -d /usr/local/php ] && mkdir /usr/local/php
	pwd
	tar -zxf php-${version}.tar.gz && cd php-${version}
	
}

## mysql编译安装
mysql()
{
	echo "##########MYSQL INSTALL##########" >> ${CURDIR}/install_logs/mysql.log
	echo -e "\e[32mmysql版本选择: [${MYS_VER[@]}]\e[0m"
	read -p "> " version
	echo "install mysql-${version}"
	sleep 2
	
	get_mys_pkg ${version}
	[ ! -d /usr/local/mysql ] && mkdir /usr/local/mysql && [ ! -d /data/mysql ] && mkdir -p /data/mysql	
	[ "${MNUM}" == "" ] && useradd ${MUSER} -s /sbin/nologin

	tar -zxf mysql-${version}.tar.gz && cd mysql-${version}
	cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
	-DMYSQL_DATADIR=/data/mysql \
	-DSYSCONFDIR=/data/mysql \
	-DWITH_INNOBASE_STORAGE_ENGINE=1 \
	-DWITH_PARTITION_STORAGE_ENGINE=1 \
	-DWITH_FEDERATED_STORAGE_ENGINE=1 \
	-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
	-DWITH_MYISAM_STORAGE_ENGINE=1 \
	-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
	-DWITH_READLINE=1 \
	-DENABLED_LOCAL_INFILE=1 \
	-DENABLE_DTRACE=0 \
	-DDEFAULT_CHARSET=utf8mb4 \
	-DDEFAULT_COLLATION=utf8mb4_general_ci \
	-DWITH_EMBEDDED_SERVER=1 >> ${CURDIR}/install_logs/mysql.log 2>&1
	[ $? -ne 0 ] && echo "mysql configure error." >> ${CURDIR}/install_logs/mysql.log && exit
	make && make -j ${CORE} install
	[ $? -ne 0 ] && echo "mysql install error." >> ${CURDIR}/install_logs/mysql.log && exit
	echo "mysql install successful." >> ${CURDIR}/install_logs/mysql.log && chown -R mysql:mysql /data/www
}

pcre()
{
	echo -e "\e[32mpcre版本选择: [${PCR_VER[@]}]\e[0m"
	read -p "> " version
	echo "install prce-${version}..."
	sleep 2

	get_pcre_pkg ${version}	
	tar -zxf pcre-${version}.tar.gz && cd pcre-${version}
	./configure --prefix=/usr/local >> ${CURDIR}/install_logs/pcre.log 2>&1
	[ $? -ne 0 ] && echo "pcre configure error." >> ${CURDIR}/install_logs/pcre.log && exit
	make && make -j ${CORE} install
	[ $? -ne 0 ] && echo "pcre install error." >> ${CURDIR}/install_logs/pcre.log && exit
	echo "pcre install successful." >> ${CURDIR}/install_logs/pcre.log
	
}


## 依赖
libs_install()
{
	echo "dependent libs install..."
	sleep 2
	yum -y install yum-fastestmirror gcc gcc-c++ gcc-g77 flex bison tar libtool libtool-libs kernel-devel autoconf libjpeg libjpeg-devel libpng libpng-devel libtiff libtiff-devel gettext gettext-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel file glib2 glib2-devel bzip2 diff* openldap-devel bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel libidn libidn-devel openssl openssl-devel vim-minimal unzip > /dev/null 2>&1
}
