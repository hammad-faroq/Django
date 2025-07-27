from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic

# Create your views here.
# def index(request):
#     return HttpResponse("THis is my first Django servlet.Dango is very tricky as compared to the noraml java web development because it has some project structure, specific seetings and make migrations and migrations and a lot more but i m=am exploaring django as an advanced framework for web development using python (:)")

# def detail(request, question_id):
#     response="YOu are looking at the question %s."
#     return HttpResponse(response % question_id)
# def result(request,question_id):#previous
#     response="You are looking at the result of the question %s."
#     return HttpResponse(response % question_id)
# def vote(request, question_id):Previous
#     return HttpResponse("You're voting on question %s." % question_id)
# def result(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,"polls/results.html",{"question":question})
class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:2]
class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"
class ResultView(generic.DetailView):
    model=Question
    template_name="polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):#When you submit the Post form without selecting a choice this except gonna run
        return render(request, "polls/detail_4.html",{"question":question,
                                                      "error_message":"You didn't select a choice!"},)
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        #redirecting after handling POst
        return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))#reverse automatically make /polls/args/result to call the result view using urls of polls




# def index(request):Is automatically done in Generic list view
#     latest_question_list = Question.objects.order_by("-pub_date")[:2]
#     # output = ", ".join([q.question_text for q in latest_question_list])#ya kam uder do rha template use kar ka usind DTL and add some html in it
#     # template=loader.get_template("polls/index.html")1
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     # return HttpResponse(template.render(context,request))2
#     return render(request, "polls/index.html", context)#Shot cut render 3
def new_detail(request, question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)#shortcut of the above lines
    # return render(request,"polls/detail.html",{"question":question})
    return render(request,"polls/detail_4.html",{"question":question})

