from django.shortcuts import render
from .forms import VolunteerForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    success = False

    if request.method == 'POST':
        form = VolunteerForm(request.POST)

        if form.is_valid():
            form.save()
            success = True
    else:
        form = VolunteerForm()

    return render(request, 'register.html', {
        'form': form,
        'success': success
    })
