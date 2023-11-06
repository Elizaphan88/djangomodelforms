from django.shortcuts import render
from djangoModelForms.forms import WanafunziForm

def home(request):
    stud=WanafunziForm()
    return render(request, 'index.html', {'form': stud})
