from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext


# Create your views here.
def index(request):
    welcome_txt = "<h1>Awesome,we are on polls index</h1>"
    latest_ques = Question.objects.order_by('pub_date')[:5]
    # print(latest_ques)
    # output = welcome_txt+"<h2>"+"<br>".join(item.question_text for item in latest_ques)+"</h2>"
    # return HttpResponse(output)
    context = {'latest_questionnaire': latest_ques}
    return render(request, "./polls/index.html", context)


def details(request, ques_id):
    question = get_object_or_404(Question, pk=ques_id)
    return render(request, "polls/detail.html", {'ques_dtl': question})
    # return HttpResponse("This is detail of question %s" % ques_id)


def results(request, ques_id):
    return HttpResponse("This is the result of question %s" % ques_id)


def vote(request, ques_id):
    return HttpResponse("Votes on question %s = " % ques_id)
