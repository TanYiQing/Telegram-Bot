from django.urls import path
from App_Victim import views

urlpatterns = [
    path('adddata/', views.register, name="register"),
    path('viewdata/', views.viewdata, name="view"),
    path('viewdata/<ic>', views.victim_detail, name="victim-detail"),
]
