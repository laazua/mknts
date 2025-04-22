```
<a class="action" href="{{ url_for('blog.create') }}">New</a>

这段代码的作用是创建一个带有 "New" 文字的超链接，点击该链接时将跳转到由 'blog.create' 视图函数处理的页面
```
```
<form action="/submit-form" method="post">
  <!-- 表单内容 -->
  <input type="text" name="username" placeholder="请输入用户名">
  <button type="submit">提交</button>
</form>

action 属性是 <form> 元素的一个重要属性，它定义了表单数据提交的目标地址，即服务器接收并处理表单数据的URL
```