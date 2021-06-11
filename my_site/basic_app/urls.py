from django.urls import path, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('add-to-do',views.add_todo,name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo)
]
