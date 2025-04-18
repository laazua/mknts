# 编译自定义的java项目

TARGET := bin
JARFILE := example.jar

.PHONY: clear,jar,run

jar:
	[ ! -d $(TARGET) ] && mkdir $(TARGET)
	find . -name "*.java" -exec javac --source-path src -d $(TARGET) {} \;
	jar cfe $(JARFILE) org.example.Main -C bin .

run:
	@java -jar $(JARFILE)

clean:
	rm -fr $(TARGET) $(JARFILE)

list:
	@#分析jar包依赖的模块
	@jdeps --ignore-missing-deps --print-module-deps --recursive --multi-release 23 -cp . ./$(JARFILE)

##### 根据list的得到的依赖模块来生成jre(运行时环境)：
# jlink --module-path $JAVA_HOME/jmods \
#       --add-modules java.base,java.logging,java.xml,java.sql \
#       --strip-debug \
#       --no-header-files \
#       --no-man-pages \
#       --compress=zip-9 \
#       --output jre

##### 手动添加三方包进行编译
# javac -cp "libs/some-library.jar" *.java