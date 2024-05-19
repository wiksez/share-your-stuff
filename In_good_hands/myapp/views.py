from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from myapp.forms import CategoryForm, InstitutionForm, DonationForm, RegistrationForm
from myapp.models import Donation, Institution, Category


# Create your views here.

class LandingPage(View):

    def get(self, request):
        institution = Institution.objects.count()
        quantity = 0
        donation = Donation.objects.all()
        fundation = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        collections = Institution.objects.filter(type=3)
        for elements in donation:
            quantity += int(elements.quantity)
        return render(request, 'index.html', {'institution': institution,
                                              'quantity': quantity, 'fonds': fundation, 'organization': organizations,
                                              'collections': collections})


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('registration')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
            name = request.POST['name']
            surname = request.POST['surname']
            email = request.POST['email']
            pass1 = request.POST['password']
            pass2 = request.POST['password2']
            if pass1 is not None and pass1 == pass2:
                username = email.split('@')[0]
                user = User.objects.create_user(username=username, first_name=name, last_name=surname, email=email,
                                                password=pass1)
                return redirect('login')
            return render(request, 'register.html')


class AddCategory(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'add_category.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'add_category.html', {'form': form})


class AddInstitution(View):
    def get(self, request):
        form = InstitutionForm()
        return render(request, 'add_institution.html', {'form': form})

    def post(self, request):
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'add_institution.html', {'form': form})


class Donations(View):
    def get(self, request):
        form = DonationForm()
        return render(request, 'add_donation.html', {'form': form})

    def post(self, request):
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'add_donation.html', {'form': form})