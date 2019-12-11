from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def hello(request):
    return render(request, "hello.html")

def login(request):
    '''实现登录功能'''
    if request.method == 'GET':
        #返回登录页面
        return render(request, "index.html")

    else:
        #处理登录的请求
        my_username = request.POST.get('username', '')
        my_password = request.POST.get('password', '')
        if my_username == ''  and my_password == '':
            return render(request, 'index.html', {'error': 'username or password can not empty！'})

        user = auth.authenticate(username = my_username,password = my_password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/manage')
           # response.set_cookie('user', my_username, 3600) #将cookie添加到浏览器
            request.session['user'] = my_username #添加session
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error！'})

@login_required
def manage(request):
    #cookie_user = request.COOKIES.get('user') #读取浏览器cookie
    session_user = request.session.get('user')
    event_list = Event.objects.all()
    return render(request, "event_manage.html", {'welcome_user':session_user,
                  'events':event_list})
@login_required
def guest(request):
    #cookie_user = request.COOKIES.get('user') #读取浏览器cookie
    session_user = request.session.get('user')
    guest_list = Guest.objects.all()
    p = Paginator(guest_list, 3)
    page = request.GET.get("page",'')
    try:
        guest_page = p.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        guest_page = p.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        guest_page = p.page(p.num_pages)
    return render(request, "guest_manage.html", {'welcome_user':session_user,
                  'guests':guest_page})

@login_required
def event_search(request):
    """发布会查询"""
    #cookie_user = request.COOKIES.get('user') #读取浏览器cookie
    if request.method == "GET":
        event_name = request.GET.get("name", "")
        event_list = Event.objects.filter(name__contains=event_name)
        return render(request, "event_manage.html", {
                      'events':event_list})
    else:
        response = HttpResponseRedirect('/manage')
        return response

@login_required
def sign_index(request, event_id):
    """嘉宾签到"""

    event = get_object_or_404(Event, id=event_id)
    if request.method == "GET":
        # event_list = Event.objects.filter(id = event_id)

        return render(request, "sign_index.html", {
                      'event':event})
    else:
        phone = request.POST.get("phone", "")
        print(phone)
        guest = Guest.objects.filter(phone=phone)
        if len(guest) == 0:
            return render(request, "sign_index.html", {
                'hint': "手机号不存在",'event':event })
        guest = Guest.objects.filter(event_id = event_id, phone=phone)
        if len(guest) == 0:
            return render(request, "sign_index.html", {
                'hint': "该手机号未参加本次活动！",'event':event})

        guest = Guest.objects.get(event_id=event_id, phone=phone)
        if guest.sign is False:
            guest.sign = True
            guest.save()
            return render(request, "sign_index.html", {
                'hint': "签到成功！",'event':event})
        else:
            return render(request, "sign_index.html", {
                'hint': "用户已签到！",'event':event})

def logout(request):
    """登出"""
    auth.logout(request)
    return HttpResponseRedirect('/login')




