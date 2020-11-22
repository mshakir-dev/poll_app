from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse

from .models import Question, Choice

# Get questions and display them
def index(request):
  # It will give all the objects from the Question Model [Order by Date and Only 5]
  # Order_by will help to show the most current at the very top 
  latest_question_list = Question.objects.order_by('-pub_date')[:3]
  context = {'latest_question_list': latest_question_list}
  # print(context)
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  try:
    # Question ID is gonna help to show the specific Question and Answer
    question = Question.objects.get(pk=question_id)
    # context = {'question_detail': question_detail}
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })
  
# Get question and display results
def results(request, question_id):
  # get_object_or_404 --> it is gonna look for the ID if not found then it will return 404 Page
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })


# Vote for a question choice
def vote(request, question_id):
  print(request.POST['choice'])
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def resultsData(request, obj):
  votedata = []

  question = Question.objects.get(id=obj)
  votes = question.choice_set.all()

  for i in votes:
      votedata.append({i.choice_text:i.votes})

  print("Vote Data",votedata)
  return JsonResponse(votedata, safe=False)