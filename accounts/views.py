from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import UserCreateForm

# Create your views here.
class SignUp(CreateView):
	form_class = UserCreateForm
	template_name = 'accounts/signup.html'
	success_url = reverse_lazy('login')