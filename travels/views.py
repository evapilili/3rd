from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TravelLog
from .forms import TravelLogForm

def travel_list(request):
    travels = TravelLog.objects.all()
    return render(request, 'travels/travel_list.html', {'travels': travels})

@login_required
def travel_create(request):
    if request.method == 'POST':
        form = TravelLogForm(request.POST, request.FILES)
        if form.is_valid():
            travel_log = form.save(commit=False)
            travel_log.user = request.user
            travel_log.save()
            return redirect('travel_list')
    else:
        form = TravelLogForm()
    return render(request, 'travels/travel_form.html', {'form': form})

def travel_detail(request, pk):
    travel = get_object_or_404(TravelLog, pk=pk)
    return render(request, 'travels/travel_detail.html', {'travel': travel})
