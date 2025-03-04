from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('textbooks/', views.textbook_list, name='textbook_list'),
    path('textbooks/<str:course_code>/', views.textbooks_by_course_code, name='textbooks_by_course'),

]