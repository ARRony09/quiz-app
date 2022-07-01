from django.urls import path
from . import views

app_name='app_quiz'

urlpatterns = [
    path('home/',views.home_page,name='home'),
    path('',views.index,name='index'),
    path('addquestions/',views.addquestion,name='addquestion'),
]