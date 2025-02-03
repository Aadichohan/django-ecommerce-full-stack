from django.contrib import admin
from django.urls import path
from daraz import views

urlpatterns = [
    path('login/', view=views.userLogin, name="login"),
    path('dashboard/', view=views.dashboard, name="dashboard"),
    path('user_list/', view=views.userList, name="user_list"),
    path('edit_user/<int:id>', view=views.userEdit, name="edit_user"),
    path('save_edit_user/', view=views.userEdit, name="save_edit_user"),
]
