from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path('', views.home,name= "home"),
    path('home/', views.home,name= "home"),
    path('DC/', views.DC,name= "DC"),
    path('Faculty/', views.Faculty,name= "Faculty"),
    path('Campus/', views.Campus,name= "Campus"),
    path('Students/', views.Student,name= "Student"),
    path('Academic/', views.Academic,name= "Academic"),
    path('About/', views.About,name= "About"),
    path('Contactus/', views.Contactus,name= "Contactus"),
    path('Grievance/', views.Grievance,name= "Grievance"),
    
]