from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic

# def index(request):
#     # displays the latest 5 poll questions in the system, separated by commas,
#     # according to publication date.
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     # output = ','.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list':latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# use render

# use generic instead
class IndexView(generic.ListView):
    # 重写属性
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return the last five published questions
        return Question.objects.order_by('-pub_date')[:5]


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html', context)


# Question 'index' page -- displays the latest few questions.
# Question 'detail' page - displays a question text, with no results but with a form to vote.
# Question 'results' page - displays results for a particular question.
# vote action - handles voting for a particular choice in a particular question.


# -------------------------------------------------------------------------------------------------
# Each view is represented by a simple python function(or method, in the case of class-based views)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
# A shortcut:
# from django.shortcuts import get_object_or_404
# def detail(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # the question_id is from urls.py
    question = get_object_or_404(Question,pk=question_id)
    try:
        # get method returns an object
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print('selected_choice is {}, type is {}'.format(selected_choice, type(selected_choice)))
        print("request.POST return {}".format(request.POST))
    except (KeyError, Choice.DoesNotExist):

        # redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "you didnt select a choice.",})
    else:
        print('dd')
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
