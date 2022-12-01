from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import render, redirect
from users.forms import UserCreationForm

def index(request):
    return render(request, template_name='main/index.html')


class Register(View):
    template_name ='main/register.html'
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
        context = {
            'form': form
        }
        return render(request, self.template_name, context)




