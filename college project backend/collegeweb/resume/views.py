from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import resumeForm
from .models import resumeModel
from django.contrib.auth.models import User
# Create your views here.
def resumeUploder(request):
    if request.method=="GET":
        data=resumeForm()
        # data1=resumeModel.objects.all()
        cv=resumeModel.objects.all()
        return render(request, "resume/remumeTemplate.html", {"forms":data, 'cv':cv})
    elif request.method=="POST":
        data=resumeForm(request.POST, request.FILES)    
        # print(resumeModel.languagies)
        if data.is_valid():
            data.save()
            # return render(request,"remumeTemplate.html", {"forms":data})
            # return HttpResponse("the form is successfully submitted")
            return redirect("resumeUploder1")
        else:
            print(data.errors)
            return HttpResponse(data.errors)
        

def cvView(request, pk):
    data=resumeModel.objects.filter(pk=pk)
    # print(data.languagies)
    print(data)
    return render(request, "resume/cv_page.html", {"data":data})



