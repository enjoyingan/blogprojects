from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST': #POST 방식으로 요청을 받았는지 확인
        if request.POST['password1'] == request.POST['password2']: 
            #비밀번호 input값과 비밀번호 확인 input이 같은지
            try: # try 안에서 오류가 나지 않는 경우 계송 실행
                user = User.objects.get(username = request.POST['username'])
                #회원가입할때 이름과 같은 이름의 회원 불러오기, 없으면 에러
                return render(request, 'signup.html', {'error' : '이미 사용하고 있는 이름입니다!'})
            except User.DoesNotExist: #try 안에서 User.DoesNotExist 에러가 났을 경우 실행

                user = User.objects.create_user(
                    request.POST['username'], password = request.POST['password1']
                )
                auth.login(request, user) #접속 상태를 로그인 상태로 바꾼다
                return redirect('/')
    return render(request, 'signup.html') #회원가입 페이지 보여주기

def login(request):
    if request.method == 'POST': # POST 요청을 받은 경우
        username = request.POST['username']
        password = request.POST['password']
        #로그인에서 받은 정보를 가진 회원이 있는지 확인하기
        user =auth.authenticate(request, username=username, password=password)
        if user is not None: #User가 존재할 경우
            auth.login(request, user) #로그인 상태로 바꾸기
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디나 비밀번호를 확인해주세요'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request) #로그아웃 상태로 바꾸기
    return render(request, 'login.html')
    