from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), #end_point
    path('questions/', views.QuestionListView.as_view()),
    path('questions/create', views.QuestionCrateView.as_view()),
    path('question/update/<int:pk>', views.QuestionUpdateView.as_view()),
    path('question/update/<int:pk>', views.QuestionDeleteView.as_view()),
]