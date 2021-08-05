from django.shortcuts import render
from django.http import HttpResponse

from .forms import DailyActivityForm

# Create your views here.
#-------------------------------------
def home(request):

    return render(request, 'edrar/home.html')
    #return HttpResponse("eDRAR Home Page.")

def activity_add(request):

    return render(request, 'edrar/activity_add.html', {'form': DailyActivityForm})