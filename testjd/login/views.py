from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        # 这里可以处理登录表单提交的逻辑
        # 假设你要在这里验证用户名和密码，并完成登录过程
        # 然后重定向到'navi'页面
        return redirect('/mian')

    return render(request, 'login/login.html')