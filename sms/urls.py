
from django.urls import path
from . import views
from . import hodviews

urlpatterns = [
    path('',hodviews.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dologin',views.dologin,name='dologin'),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user),
    path('add_staff',hodviews.add_staff,name="add_staff"),
    path('add_students',hodviews.add_students,name='add_students'),
    path('profile',hodviews.profile,name='profile'),
    path("add_staff_save",hodviews.add_staff_save,name="add_staff_save"),
    path("add_student_save",hodviews.add_student_save, name="add_student_save")

]
