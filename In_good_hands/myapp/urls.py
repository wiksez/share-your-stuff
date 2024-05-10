from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('add_donation/', views.AddDonation.as_view(), name='add_donation'),
    path('login/', views.Login.as_view(), name='login'),
    path('registration/', views.Register.as_view(), name='registration'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('add_institution/', views.AddInstitution.as_view(), name='add_institution'),
    path('add_donation/', views.AddDonation.as_view(), name='add_donation')
]