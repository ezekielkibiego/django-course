from django.shortcuts import render, redirect
from .models import Employee,Profile
from .forms import EmployeeForm, UpdateEmployeeForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def index(request):
    #  context = {'message': 'Hello, world!'}
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})
    
def addEmployee(request):
   if request.method == "POST":
     form = EmployeeForm(request.POST)
     if form.is_valid():
        try:
           form.save()
           return redirect('/')
        except:
           pass
   else: 
      form = EmployeeForm()
   return render(request, 'addEmployee.html', {'form':form})

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    
    employee = Employee.objects.get(id=id)  
    form = UpdateEmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")

def profile(request):
   current_user = request.user
   profile = Profile.objects.filter(user_id=current_user.id).first()

   return render(request, "profile.html", {"profile": profile})