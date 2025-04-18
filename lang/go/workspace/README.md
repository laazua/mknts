### workspace

- 说明  
1. 这是一个用go.work组织项目代码的示例  

- 工作空间
1. 初始化工作空间:  
   mkdir spacename && cd spacename && go work init  

2. 使用工作空间:  
   a. 创建模块:
      mkdir modulename  
      cd modulename  
      go mod init modulename  
      go work use .  (将当前模块添加到工作空间)  
   b. 创建模块:
      mkdir modulename  
      cd modulename  
      go mod init modulename  
      cd .. && go work edit -use modulename  (将创建的模块添加到工作空间)  
   c. 从工作空间移除模块:
      go work edit -dropuse=modulename

3. go work sync  
   将当前工作空间使用的模块同步到各个模块的依赖中去(即: 更新各个模块的go.mod,确保与go.work保持一致)  

