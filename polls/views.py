from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.http import Http404
from django.urls import reverse
from .models import Choice, Question
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        qs=Question.objects.all()
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return Http5ResponseRedirect(reverse("polls:results", args=(question.id,)))














































































# from django.http import HttpResponse,HttpResponseRedirect
# from .models import Question
# from django.template import loader
# from django.shortcuts import get_object_or_404, render
# from django.http import Http404
# from django.views import generic
# from django.urls import reverse
# from .models import Choice, Question
# from django.db.models import F

# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"


# def vote(request, question_id):
#     # same as above, no changes needed.
    # ...







#IndexView
# class IndesView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]

# #DetailView
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"


# def vote(request, question_id):
#     # same as above, no changes needed.



# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list, #("latest_question_list"는 index.html의 %if와 % for question in 부분과 같아야 함)
#     }
#     return HttpResponse(template.render(context, request))

# 와 from django.shortcuts import render + 밑에 함수는 같은 내용
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list} #("latest_question_list"는 index.html의 %if와 % for question in 부분과 같아야 함)
#     return render(request, "polls/index.html", context)

# 실습index1 을 만들고, index1.html을 만들어서 하나 동작시켜 보기
# def index1(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list} #("latest_question_list"는 index.html의 %if와 % for question in 부분과 같아야 함)
#     return render(request, "polls/index1.html", context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

# def detail(request, question_id):
#     question=get_object_or_404(Question, pk=question_id)
#     # choice_count=len(question.choice_set.all())
#     # content_1=question.choice_set.all()[0]
#     question_list =Question.objects.all()
#     context={
#         'question':question
#     }
#     return render(request, "polls/detail.html", context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
    


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
#question_id 말고 다른 이름으로 받아도 될까?
# 숫자가 아닌게 들어오면 어떻게 되지? (urls.py path에 int로 지정했기 때문에 정수만 가능)
# 2개 다른 경로로 들어오고 question_id가 표시되는 view 함수를 만들어 봅시다.