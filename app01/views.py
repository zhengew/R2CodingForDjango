from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print(request.method)

    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username == 'zew' and password == '123':
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')

def year_month_books(request, year, month):
    print(year, month)
    return HttpResponse((year, month))

def year_books(request, year):
    print(year)
    return HttpResponse(year)

def pages(request, pageSize=10):
    print(pageSize)
    return HttpResponse(pageSize)