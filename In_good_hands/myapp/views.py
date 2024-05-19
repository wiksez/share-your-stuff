from django.shortcuts import render, redirect
from django.views import View

from myapp.forms import CategoryForm, InstitutionForm, DonationForm
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


class Register(View):

    def get(self, request):
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