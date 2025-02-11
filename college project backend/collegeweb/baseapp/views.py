from django.shortcuts import render,HttpResponse, redirect
from .forms import studentForm,courceForm,testiForm
from django.views import View
from .models import students,cources,testimonial
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import students
# Create your views here.

@method_decorator(login_required(login_url="/"), name='dispatch')
class studentsayView(View):
    # @login_required(login_url="/")
    def get(self,request):
        user=request.user
        data=studentForm(initial={'student_id': user})
        studenter =students.objects.all()
        users=request.user
        print(users)

        return render(request, 'intructor.html' ,{"form": data,"student":studenter})

    def post(self, request):
        value=studentForm(request.POST, request.FILES)
        if value.is_valid():
            
            print(value)
            value.save()
           
            messages.success(request, "Successfully submited")
            return redirect("studentsay")
        else:
            messages.error(request, "Some exception occur")

            return HttpResponse("not ")


# cource view 
@method_decorator(login_required(login_url="/"), name='dispatch')
class courceView(View):
    def get(self,request):
        cource=cources.objects.all()
        cform=courceForm()
        return render(request, 'cource.html',{'cource':cource,'form':cform})
    

    def post(self, request):
        form=courceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cource")
        else:
            return redirect("cource")

@method_decorator(login_required(login_url="/"), name='dispatch')
class testimonialView(View):
    def get(self,request):
        testimonials=testimonial.objects.all()
        testiForms=testiForm()
        return  render(request,'testimonical.html',{'testi':testimonials,'form':testiForms})
    

    def post(self,request):
        result=testiForm(request.POST,request.FILES)
        if result.is_valid():
            result.save()
            return redirect("testimonial")
        else:
            return HttpResponse("Not success")

# @method_decorator(login_required(login_url="/"), name='dispatch')
class indexView(View):
    def get(self,request):
        data=studentForm()
        studenter =students.objects.all()
        cource=cources.objects.all()
        cform=courceForm()
        try:

            student=students.objects.get(student_id=request.user)
            # print(student.student_id.password)
        except:
            print("not found the dadta")

        return render(request, 'index.html' ,{"studentform": data,"student":studenter,'cource':cource,'courceform':cform})
    

    def post(self, request):
        form=courceForm(request.POST,request.FILES)
        value=studentForm(request.POST, request.FILES)
        form_type = request.POST.get('form_type')
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return redirect("home")
        # if form_type == 'form2':
        #     if form.is_valid():
        #         form.save()
        #         return redirect("home")
        #     else:
        #         return redirect("cource")
        # elif form_type == 'form1':
        #     if value.is_valid():
        #         value.save()
        #         messages.success(request, "Successfully submited")
        #         return redirect("home")
        #     else:
        #         messages.error(request, "Some exception occur")

        #         return HttpResponse("not ")

@method_decorator(login_required(login_url="/"), name='dispatch')     
class courceDetailsView(View):
    def get(self,request):
        cource=cources.objects.all()
        cform=courceForm()
        return render(request, 'courceDetails.html',{'cource':cource,'form':cform})

class contectView(View):
    def get(self, request):
        return render(request, 'contect.html')

@method_decorator(login_required(login_url="/"), name='dispatch')
class aboutview(View):
    def get(self,request):
        data=studentForm()
        studenter =students.objects.all()
        return render(request,'about.html',{"studentform": data,"student":studenter})