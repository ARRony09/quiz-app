from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import addQuestion
from .models import QuesModel
# Create your views here.

def home_page(request):
    return render(request,'App_quiz/home.html',context={})

def index(request):
    if request.method == 'POST':
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
            
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
        }
        return render(request,'App_quiz/result.html',context)

    else:
        questions=QuesModel.objects.all()
        return render(request,'App_quiz/index.html',context={'questions':questions})

def addquestion(request):
    form=addQuestion()
    if request.method=='POST':
        form=addQuestion(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_quiz:addquestion'))
    return render(request,'App_quiz/add_quiz.html',context={'form':form})
