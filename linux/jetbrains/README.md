### jetbrains

- 激活码
1. [激活工具](https://github.com/lixuanfengs/jetbrains-license)
2. 将步骤1中的激活工具下载到本地打包运行
3. 从官网下载需要激活的idea(如:Goland),并安装
4. 打开Goland设置地区为: 不指定. 然后关闭 (这一步很重要)
5. 打开Goland安装目录下配置文件(Goland为例): goland64.exe.vmoptions, 配置  
   --add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED  
   --add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED  
   -javaagent:C:\path\to\ja-netfilter.jar=jetbrains  
   其中ja-netfilter.jar的路径为下载激活工具到本地的路径(具体路径需要根据实际情况进行修改)  
6. 运行激活工具进行配置获取激活码, 打开Goland进行激活


- vscode字体
1. 'JetBrains Mono', Consolas, 'Courier New', monospace
2. Fira Code Regular
3. 'SF Mono', Consolas, 'Courier New', monospace

- vscode字体配置
```json
{
    "editor.fontFamily": "'JetBrains Mono', Consolas, 'Courier New', monospace",
    "editor.fontSize": 14,
    "editor.fontLigatures": true, // 启用连字功能（可选）
    "editor.fontWeight": "normal"
}
```