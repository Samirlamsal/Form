from django.shortcuts import render
from .models import data
from .forms import detail



def form_view(request):
    if request.method=='POST':
        form = detail(request.POST or None)
        if form.is_valid():
            form.save()
    form = detail()
    return render(request, 'form.html', {'form' : form})
