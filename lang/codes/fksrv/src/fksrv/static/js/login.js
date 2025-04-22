function getLoginForm(){
    $(document).ready(function () {
        $("formId").submit(function (event) {
            // 阻止表单默认提交行为
            event.preventDefault();

            // 获取表单数据
            var formData = $(this).serializeArray();
            // 发送 AJAX 请求
            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:8884/auth/login',  // 替换为你的后端接口地址
                data: formData,
                success: function (response) {
                    // 请求成功的回调函数
                    console.log('Data sent successfully!');
                    console.log(response); // 可选：打印服务器返回的数据
                    // 可以在这里处理后续的逻辑，比如显示成功信息，重定向等
                },
                error: function (error) {
                    // 请求失败的回调函数
                    console.error('Error sending data:', error);
                    // 可以在这里处理错误情况，比如显示错误信息
                }
            });
        })
    })
}