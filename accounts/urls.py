from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    # path('signup/',views.register,name='signup'),
    # path('profile/',views.profile, name='profile'),
    # path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('student_register/',views.student_register, name='student_register'),
    path('student_profile/<username>',views.student_profile, name='student_profile'),
    path('edit_student/',views.edit_student, name='edit_student'),
    path('teacher_register/',views.teacher_register, name='teacher_register'),
    path('teacher_profile/<username>',views.teacher_profile, name='teacher_profile'),
    path('edit_teacher/',views.edit_teacher, name='edit_teacher'),
    path('profile/<username>',views.profile, name='profile'),
    ]
