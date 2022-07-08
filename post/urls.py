from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView, UserGetJobView

urlpatterns = [
    path('', SkillView.as_view()),

    path('job', JobView.as_view()),
    path('<user_type>/job', UserGetJobView.as_view()),
]
