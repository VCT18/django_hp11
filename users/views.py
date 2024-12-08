from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm

def signin (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Đã có lỗi xảy ra, mời bạn đăng nhập lại")
            return redirect('signin')
    else:
        form = LoginForm()
        context={
        'form': form
        }   
    return render(request, 'users/signin.html',context=context)
def signup(request):  
    if request.method == 'POST':  
        form = RegisterForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Đăng ký thành công! Bạn có thể đăng nhập ngay bây giờ.")  
            return redirect('signin')  
        else:  
            print(form.errors)  # Print errors for debugging  
            messages.error(request, "Đã có lỗi xảy ra, mời bạn đăng ký lại")  
    else:  
        form = RegisterForm()  
    
    return render(request, 'users/signup.html', {'form': form})  
    
def signout(request):
    logout(request)
    return redirect('/')