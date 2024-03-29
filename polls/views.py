from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list, #("latest_question_list"는 index.html의 %if와 % for question in 부분과 같아야 함)
#     }
#     return HttpResponse(template.render(context, request))

# 와 from django.shortcuts import render + 밑에 함수는 같은 내용
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list} #("latest_question_list"는 index.html의 %if와 % for question in 부분과 같아야 함)
    return render(request, "polls/index.html", context)

# 실습index1 을 만들고, index1.html을 만들어서 하나 동작시켜 보기
def index1(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list} #("latest_question_list"는 index.html의 %if와 % for question in 부분과 같아야 함)
    return render(request, "polls/index1.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#question_id 말고 다른 이름으로 받아도 될까?
# 숫자가 아닌게 들어오면 어떻게 되지? (urls.py path에 int로 지정했기 때문에 정수만 가능)
# 2개 다른 경로로 들어오고 question_id가 표시되는 view 함수를 만들어 봅시다.