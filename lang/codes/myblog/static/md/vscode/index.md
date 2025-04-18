### ***VScode配置***


* *配置JetBranins字体*
```
    - 下载字体：https://www.jetbrains.com/lp/mono/#support-languages
    - windows下解压后到fonts/ttf目录下全选文件右键选择为所有用户安装
    - linux下解压到/usr/share/fonts目录下运行命令：fc-cache -f -v
    - vscode设置：文件->首选项->编辑器->字体，设置为：JetBrains Mono, Consolas, 'Courier New', monospace
    - 如果是vscode远程开发，则设置中的用户下: 文本编辑器和远程下: 文本编辑器的字体都要设置为：JetBrains Mono, Consolas, 'Courier New', monospace
      建议将static/resource/vscode/settings.json的内容覆盖掉vscode中的settings.json中的内容
    - 重启vscode
```