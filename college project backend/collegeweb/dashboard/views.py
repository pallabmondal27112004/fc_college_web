from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from baseapp.models import students,cources
from baseapp.forms import studentForm,courceForm
from .models import assignment,assignmentlist
from .forns import doAssignmentForm
import datetime 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from loginapp.models import customeruser
from loginapp.forms import userform
from django.contrib import messages
# Create your views here.
@method_decorator(login_required(login_url="/"), name='dispatch')
class dashboardIndex(View):
    def get(self,request):
        return render(request, "dashboard/index.html")
    def post(self,request):
        pass

class showStudent(View):
    def get(self,request):
        form=studentForm(initial={'student_id':request.user})
        input=request.GET.get('input')
        if input == None:

            allStudent=students.objects.all()
        else:
            allStudent=students.objects.filter(name__icontains=input)

        context={}
        context['form']=form
        context["student"]=allStudent
        return render(request,'dashboard/student.html',context)
    def post(self,request):
        result=studentForm(request.POST,request.FILES)
        if result.is_valid():
            result.save()
            return redirect('studentDetails')
        else:
            return HttpResponse("Not submitted ")

class editStudent(View):
    def get(self,request,pk):
        student=students.objects.get(id=pk)
        student = students.objects.get(id=pk)
        form=studentForm(initial={"student_id": request.user,'name':student.name,'job':student.job,'image': student.image})
        context={}
        context['form']=form
        context['student']=student
        return render(request,'dashboard/studentedit.html',context)
    def post(self, request,pk):
        student = students.objects.get(id=pk)
        result = studentForm(request.POST, request.FILES, instance=student)
        # name=studentForm.cleaned_data['image']
        # if  name is None:
        #     studentForm(initial={'image':None})
        if result.is_valid():
            result.save()
            return redirect('studentDetails')
        else:
            return HttpResponse("Noot submitted ")

class deleteStudent(View):
    def get(self,request,pk):
        student=students.objects.filter(id=pk)
        student.delete()
        return redirect('studentDetails')


class showCource(View):
    def get(self,request):
        form=courceForm(initial={'cource_id':request.user})
        context={}
        context['form']=form
        input =request.GET.get('input')
        if input == None:
            allCource= cources.objects.all()
        else:
            allCource= cources.objects.filter(courceName__icontains=input)

        
        context["cource"]= allCource
        return render(request,'dashboard/cource.html',context)
    def post(self,request):
        result=courceForm(request.POST,request.FILES)
        if result.is_valid():
            result.save()
            return redirect('courceDetails')
        else:
            return HttpResponse("Not submitted ")
        

class editCource(View):
    def get(self,request,pk):
        cource=cources.objects.get(id=pk)
        form=courceForm(initial={"cource_id": request.user,'courceName':cource.courceName,'host':cource.host,'rating':cource.rating,'image': cource.image})
        context={}
        context['form']=form
        context['cource']=cource
        return render(request,'dashboard/courceedit.html',context)
    def post(self, request,pk):
        cource = cources.objects.get(id=pk)
        result = courceForm(request.POST, request.FILES, instance=cource)
        # name=studentForm.cleaned_data['image']
        # if  name is None:
        #     studentForm(initial={'image':None})
        if result.is_valid():
            result.save()
            return redirect('courceDetails')
        else:
            return HttpResponse("Noot submitted ")

class deleteCource(View):
    def get(self,request,pk):
        student=cources.objects.filter(id=pk)
        student.delete()
        return redirect('courceDetails')
    
class assignmentView(View):
    def get(self,request):
        assignments=assignmentlist.objects.all()
        stdAssignment=assignment.objects.all()
        doAssignmentForms=doAssignmentForm(initial={"assignment_id2":request.user,'sent_date':datetime.datetime.today()})
        context={}
        context['assgnList']=assignments
        context['stdAssign']=stdAssignment
        context['doassignment']=doAssignmentForms
        return render(request,'dashboard/assignment.html',context)
    def post(self,request):
        if 'form2' in request.POST:
            re = doAssignmentForm(request.POST, request.FILES)  # Form with files
            if re.is_valid():
                # Access the file from cleaned_data
                efile = re.cleaned_data['file']

                # Save the file manually
                fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Save to MEDIA_ROOT
                filename = fs.save(efile.name, efile)  # Save the file
                file_url = settings.MEDIA_URL + filename  # Generate URL
                
                # Optional: Correct the URL if needed
                file_url = file_url.replace('/dashboard/assignment', '')

                # Save the form instance and assign the file field
                result = re.save(commit=False)
                result.file = file_url  # Assign saved filename or file_url
                result.save()

                print(re)
                return redirect('assignment')

            else:
                return HttpResponse("Not submitted")

                
        else: 
            result=request.POST
            sub=result.get('sub')
            date=result.get('date')
            
            file=request.FILES.get('afile')

            fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Save to MEDIA_ROOT
            filename = fs.save(file.name, file)  # Save the file
            file_url = settings.MEDIA_URL + filename  # Generate URL
            # Fix incorrect URL by replacing the unwanted prefix
            file_url = file_url.replace('/dashboard/assignment', '')

            form=assignmentlist(subject_name=sub,deadline=date,date=datetime.datetime.today(),assignment_file=file_url)
            form.save()
            return redirect("assignment")

            # if result.is_valid():
            #     result.save()
            #     return redirect("assignment")
            # else:
            #     return HttpResponse("Not submitted")


# class editprofile(View):
    # def get(self,request,pk):
    #     user=customeruser.objects.get(id=pk)
    #     userdetails=userform(initial={"first_name":user.first_name,'last_name':user.last_name,'email':user.email,'phome':user.phone,'catagory':user.catagory,'image':user.image})
    #     return render(request,'loginView/editprofile.html',{'form':userdetails})
    # def post(self,request,pk):
    #     print("Post requwsr")
    #     cpassword=request.POST.get('cpassword')
    #     user=customeruser.objects.get(id=pk)
    #     result=userform(request.POST,request.FILES, instance=user)
    #     if result.is_valid():
    #         password = result.cleaned_data['password']
    #         if cpassword==password:
                
    #             user= result.save(commit=False)
    #             user.set_password(password)
    #             user.save()
    #             return redirect("dash")
    #         else:
    #             messages.error(request, 'password is not match')

    #             return redirect("register")
    #     else:
    #         messages.error(request, 'Something went wrong')

    #         return redirect("register")
        
 

       