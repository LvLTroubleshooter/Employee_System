from django.shortcuts import render, redirect, get_object_or_404
from .models import Employees
from .forms import EmployeesForm

# Create your views here.
def employees_list(request):
    employees = Employees.objects.all()
    return render(request, 'employeesList.html', {'employees': employees})