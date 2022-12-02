from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.views.generic.edit import CreateView


def index(request):
    return render(request, 'main/index.html')

def adminData(request):
    return render(request, 'main/adminData.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class Register(View):
    template_name = 'main/index.html'
#    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('adminData')

#            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
