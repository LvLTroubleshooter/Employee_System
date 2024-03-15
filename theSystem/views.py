from django.shortcuts import render, redirect, get_object_or_404
from .models import Employees
from .forms import EmployeesForm

# Create your views here.
def employees_list(request):
    employees = Employees.objects.all()
    return render(request, 'employeesList.html', {'employees': employees})

def employee_create(request):
    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_list')
    else:
        form = EmployeesForm()
    return render(request, 'employeesForm.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = EmployeesForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(employees_list)
    else:
        form = EmployeesForm(instance=employee)
    return render(request, 'employeesForm.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employees_list')
    return render(request, 'employeeDelete.html', {'employee': employee})

    



