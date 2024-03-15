from django.urls import path
from . import views

urlpatterns = [
    path('',views.employees_list, name='employees_list'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:pk>/update/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]