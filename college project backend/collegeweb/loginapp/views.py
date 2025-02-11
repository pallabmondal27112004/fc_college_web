from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import customeruser
from .manager import usermanager
from .forms import userform
from django.contrib import messages
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Replace 'home' with the name of your home URL
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

@method_decorator(unauthenticated_user, name='dispatch')
class registerView(View):
    def get(self,request):
        form=userform()
        context={}
        context['form']=form
        return render(request,'loginView/register.html',context)
    
    def post(self,request):
        cpassword=request.POST.get('cpassword')
        result=userform(request.POST,request.FILES)

        if result.is_valid():
            password = result.cleaned_data['password']
            if cpassword==password:
                
                user= result.save(commit=False)
                user.set_password(password)
                user.save()
                return redirect("login")
            else:
                messages.error(request, 'password is not match')

                return redirect("register")
        else:
            messages.error(request, 'Something went wrong')

            return redirect("register")

@method_decorator(unauthenticated_user, name='dispatch')
class loginview(View):  
    
    def get(self,request):
        # print("Session Keys:", request.session.keys())
        # print("Session Data:", dict(request.session.items()))
        return render(request,'loginView/login.html')    
    def post(self,request):
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate user
        # user = authenticate(request, email=email, password=password)
        try:
            
            user =customeruser.objects.get(email=email)
        except Exception:
            user =None
        # try:
        #     userpassword =customeruser.objects.filter(password=password)
        # except:
        #     userpassword=None
        print(user.password,password)   
        if user is not None:
            if check_password(password,user.password):
                login(request, user)  # Log in the user
                if user.is_superuser:
                    # return redirect('superuser_dashboard')  # Replace with your superuser dashboard URL name
                    return redirect("home")
                else:
                    # return redirect('user_dashboard')  # Replace with your regular user dashboard URL name
                    return redirect("home")
            else:
                messages.error(request, 'password is incorrect')

                return render(request,'loginView/login.html',{'value':user}) 
        else:
            messages.error(request, 'user not exsist')

            return redirect('login')  # Replace with the path to your login template

class logoutViewuser(View):
    def get(self,request):
        logout(request)
        return redirect("login")
    
