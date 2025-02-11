from django.shortcuts import render
from django.views import View
from .models import catagory,question,answer
from django.core.serializers import serialize
# Create your views here.
class quizView(View):
    def get(self,request):
        questionset=[]
        catagorys=catagory.objects.all()
        # print(catagorys)
        # # print(catagorys)
        # print(catagorys,"this is catagories")
        # re=catagorys.Catagory.first()
        # re1=re.Question.filter(isCorrect=True)
        # print(re)
        # print(re1)
        data=[]
        # for i in catagorys:
        #     # data={
        #     #     "catagory":i,
        #     #     "questions":getquestion(i)
        #     #     "answer":getanswer()
        #     # }
            
        #     data.append(i)
        #     for j in i.Catagory.all():
        #         data2=[]
        #         data2.append(j)
        #         for k in j.Question.all():
        #             data3=[]
        #             data3.append(k)
        #         data3.append(j.Question.filter(isCorrect=True))
        #         data2.append(data3)
        #         # data2['answers']=data3

        #     data.append(data2)
        # for i in catagorys:
        #     print(i)  
        #     for j in i.Catagory.all():
        #         print(j)
        #         for k in j.Question.all():
        #             print(k)
        # print(data)


        

        # for i in catagorys:
        #     context=[]
        
        #     context.append(i.catagory_name)
        #     context.append(getquestion(i))
        #     data.append(context)
            


        # print(data)
        return render(request,'quiz/quizview.html',{'data':catagorys})


    def post(self,request):
        pass


def getquestion(i):
    # questions=question.objects.filter(topic_name__catagory_name=i).values("name")
    data = serialize("json",question.objects.filter(topic_name__catagory_name=i))
    print(data)
    return data

