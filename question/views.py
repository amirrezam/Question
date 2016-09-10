from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
from question.models import Question


class QuestionList(CreateView):
    model = Question
    fields = ['title', 'body']
    template_name = "questionList.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context


class UpdateQuestion(UpdateView):
    model = Question
    fields = ['title', 'body']
    template_name = "questionUpdate.html"


class DeleteQuestion(DeleteView):
    model = Question
    success_url = "/question/list/"
    template_name = "questionDelete.html"
