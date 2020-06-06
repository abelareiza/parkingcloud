from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Vehicle

# Get questions and display them
def index(request):
  latest_vehicle_list = Vehicle.objects.order_by('-pub_date')
  context = {'latest_vehicle_list': latest_vehicle_list}
  return render(request, 'pages/index.html', context)