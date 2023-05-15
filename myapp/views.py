from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Employee,Profile
from .forms import EmployeeForm, UpdateEmployeeForm
from django.contrib.auth.decorators import login_required
# from .permissions import IsAdminOrReadOnly
from rest_framework import status

from .serializer import EmployeeSerializer
from rest_framework.views import APIView

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

class EmployeeList(APIView):
#    permission_classes = (IsAdminOrReadOnly,)
   def get(self, request, format=None):
      employees = Employee.objects.all()
      serializer = EmployeeSerializer(employees,many=True)
      return Response(serializer.data)
   def post(self, request, format=None):
      data = {
         'name': request.data.get('name'),
         'email': request.data.get('email'), 
         'phone_number': request.data.get('phone_number'), 
         'job_title': request.data.get('job_title'), 
         'salary': request.data.get('salary')
      }
      serializer = EmployeeSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)