from django.contrib import admin
from django.urls import path
from daraz.views import *

urlpatterns = [
    path('login/', view=userLogin, name="login"),
    # path('dashboard/', view=UserView.dashboard, name="dashboard"),
    path('dashboard/', view=userList, name="dashboard"),
    path('user_list/', view=userList, name="user_list"),
    path('edit_user/<int:id>', view=userEdit, name="edit_user"),
    path('save_edit_user/', view=userEdit, name="save_edit_user"),
]
