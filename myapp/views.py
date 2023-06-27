from django.shortcuts import render
from .forms import BoodschappenLijst

def index(request):

    form = BoodschappenLijst()

    if request.method == 'POST':
        print(request.POST)
        form = BoodschappenLijst(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'index.html', context)


