from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create, set_task, delete, show_json, add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create, name='create'),
    path('set-task/<int:pk>', set_task, name='set'),
    path('delete/<int:pk>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name="add_task"),
]