from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # 因为Django 的URL 解析器将请求和关联的参数发送给一个可调用的函数而不是一个类，所以基于类的视图有一个as_view() 类方法用来作为类的可调用入口

    # ex: /polls/5/
    # path('<int:question_id>', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]