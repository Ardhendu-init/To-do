from django.urls import path    
from todo import views
from .views import ListTask
urlpatterns=[
    path('',views.home, name = "home"),
    path('update/<str:pk>/',views.UpdateTask, name = "update-task"),
    path('delete/<str:pk>/',views.DeleteTask, name = "delete-task"),
    path('api/', ListTask.as_view()),
   
]