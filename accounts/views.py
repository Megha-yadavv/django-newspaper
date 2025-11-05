from django.shortcuts import render, redirect
from .form import CustomCreationForm

def sign_up(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')




    form = CustomCreationForm()
    
    return render(request, 'registration/signup.html',  {'form' :form})

def home(request):
    return render(request, 'home.html')