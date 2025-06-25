from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.contrib import messages

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        position = request.POST.get('position')
        salary = request.POST.get('salary')

        if Employee.objects.filter(id=id).exists():
            messages.error(request, 'Employee already exists.')
        else:
            Employee.objects.create(id=id, name=name, position=position, salary=salary)
            messages.success(request, 'Employee added successfully.')
        return redirect('employee_list')
    return render(request, 'employees/add_employee.html')

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('employee_list')

def promote_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        employee.salary += amount
        employee.save()
        messages.success(request, 'Employee promoted successfully.')
        return redirect('employee_list')
    return render(request, 'employees/promote_employee.html', {'employee': employee})
