# GOOS=linux;GOARCH=amd64
target = gokins
flags = -s -w
statik = ~/go/bin/statik

build:
		# @cd ~/codes/vue-admin-template && npm run build:prod
		# @rsync -av ~/codes/vue-admin-template/dist/* ~/codes/gokins/staticfiles/
		@$(statik) -src=staticfiles
		@echo "生成静态资源包$(target)/statik成功..."
		@export GOOS=linux && export GOARCH=amd64 && go build -o $(target) -ldflags="$(flags)"
		@echo "生成$(target)二进制文件成功..."
		@tar -czf $(target).tar.gz $(target) $(target).yml
		@echo "打包成压缩包$(target).tar.gz成功..."

.PBONY: all clean

clean:
		@rm -f $(target) $(target).tar.gz
