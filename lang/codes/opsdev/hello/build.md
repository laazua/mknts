### 构建

- pom.xml
```xml
<build>
    <plugins>
      <!-- 打包源码jar -->
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.2.0</version>
          <configuration>
              <archive>
                  <manifest>
                      <addClasspath>true</addClasspath>
                      <!-- 依赖包放在lib目录下 -->
                      <classpathPrefix>lib/</classpathPrefix>
                      <!-- 指定主类 -->
                      <mainClass>com.example.App</mainClass>
                  </manifest>
              </archive>
          </configuration>
      </plugin>

      <!-- 添加以下插件配置 -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <version>3.2.0</version>
        <executions>
            <execution>
                <id>copy-dependencies</id>
                <phase>package</phase>
                <goals>
                    <goal>copy-dependencies</goal>
                </goals>
                <configuration>
                    <outputDirectory>${project.build.directory}/lib</outputDirectory>
                    <includeScope>compile</includeScope>
                </configuration>
            </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
```