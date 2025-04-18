get_ngx_pkg()
{
	cd ${PKG_DIR}
	wget ${SRC_URL}"nginx/nginx-$1.tar.gz"
	curl -O ${SRC_URL}"nginx/nginx-$1.tar.gz"
	echo ${SRC_URL}
	if [ $? -eq 0 ];then
		echo "nginx-$1.tar.gz下载成功" > ${CURDIR}/install_logs/nginx.log
	else
		echo "nginx-$1.tar.gz下载失败" > ${CURDIR}/install_logs/nginx.log
	
	fi
}

get_apa_pkg()
{
	cd ${PKG_DIR}
	wget ${SRC_URL}"nginx/nginx-$1.tar.gz"
	curl -O ${SRC_URL}"apache/httpd-$1.tar.gz"
	if [ $? -eq 0 ];then
		echo "httpd-${version}.tar.gz下载成功" > ${CURDIR}/install_logs/apache.log
	else
		echo "httpd-${version}.tar.gz下载失败" > ${CURDIR}/install_logs/apache.log		
	fi
}

get_php_pkg()
{
	cd ${PKG_DIR}
	wget ${SRC_URL}"nginx/nginx-$1.tar.gz"
	curl -O ${SRC_URL}"php/php-${version}.tar.gz"
	if [ $? -eq 0 ];then
		echo "php-${version}.tar.gz下载成功" > ${CURDIR}/install_logs/php.log
	else
		echo "php-${version}.tar.gz下载失败" > ${CURDIR}/install_logs/php.log
	fi
}

get_mys_pkg()
{
	cd ${PKG_DIR}
	wget ${SRC_URL}"nginx/nginx-$1.tar.gz"
	curl -O ${SRC_URL}"mysql/mysql-$1.tar.gz"
	if [ $? -eq 0 ];then
		echo "mysql-$1.tar.gz下载成功" > ${CURDIR}/install_logs/mysql.log
	else
		echo "mysql-$1.tar.gz下载失败" > ${CURDIR}/install_logs/mysql.log
	fi
}

get_pcre_pkg()
{
	cd ${PKG_DIR}
	curl -O ${SRC_URL}"other/pcre-$1.tar.gz"
	[ $? -ne 0 ] && echo "aa"
}

get_zend_pkg()
{
	cd ${PKG_DIR}
	wget ${SRC_URL}"zend/zendopcache-${version}.tgz"
	curl ${SRC_URL}"nginx/nginx-$1.tar.gz"
}

get_pma_pkg()
{
	cd ${PKG_DIR}
	wget ${SRC_URL}"php/phpmyadmin4.tar.gz"
}
