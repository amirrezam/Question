from audioop import reverse

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^list/$', views.QuestionList.as_view(success_url="/question/list/"), name='questionList'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateQuestion.as_view(success_url="/question/list/"),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteQuestion.as_view(),name='delete')
]