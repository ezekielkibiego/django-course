from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = "__all__"
        # exclude = ['user']
        fields = ['name', 'email', 'phone_number', 'job_title', 'salary' ]

class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = "__all__"
        # exclude = ['user']
        fields = ['name', 'email', 'phone_number', 'job_title', 'salary' ]