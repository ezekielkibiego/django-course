from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),   
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile,name='profile'),
    path('api/employees/', views.EmployeeList.as_view()),
    ]